import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load Azure credentials from .env
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT = os.getenv("DEPLOYMENT_NAME")


def classify_feedback(text):
    """
    Classify customer feedback into Category, Urgency Level, and Suggested Action.
    """

    prompt = f"""
You are a Customer Feedback Triage System.

Your job is to analyze customer feedback and return:

Category: Complaint / Feature Request / Praise / Question
Urgency Level: Low / Medium / High
Suggested Action: Respond / Escalate / Ignore / Forward
Reasoning: Brief explanation

Feedback: "{text}"

Return strictly in this format:

Category:
Urgency Level:
Suggested Action:
Reasoning:
"""

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are an expert customer support triage assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
