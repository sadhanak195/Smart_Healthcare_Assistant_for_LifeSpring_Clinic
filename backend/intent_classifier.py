def detect_intent(text: str) -> str:
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    for word in greetings:
        if word in text:
            return "greeting"

    return "general_query"

