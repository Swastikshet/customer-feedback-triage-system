from triage_ai import classify_feedback
from baseline import baseline_classify

print("=== Customer Feedback Triage System ===")

while True:
    user_input = input("\nEnter customer feedback (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Exiting program...")
        break

    print("\n--- Baseline System Output ---")
    print(baseline_classify(user_input))

    print("\n--- Azure OpenAI System Output ---")
    print(classify_feedback(user_input))
