def baseline_classify(text):
    text = text.lower()

    if "bug" in text or "error" in text or "crash" in text:
        return "Complaint | High | Escalate"
    elif "add" in text or "feature" in text:
        return "Feature Request | Medium | Forward"
    elif "great" in text or "good" in text or "love" in text:
        return "Praise | Low | Ignore"
    else:
        return "Question | Low | Respond"
