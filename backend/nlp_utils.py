import re

NOISE_PATTERNS = [
    r"\bsection\b",
    r"\bintroduction\b",
    r"\bdefinition\b",
    r"\bticketing\b",
    r"\bfare rules\b",
    r"\bterms\b",
    r"\bconditions\b",
    r"\bforce majeure\b",
    r"\bpolicy\b",
    r"\bprocedures\b"
]

def clean_sentence(sentence):
    # Remove numbering like 4.2, 5.1 etc
    sentence = re.sub(r"\d+(\.\d+)*", "", sentence)

    # Remove bullets and special chars
    sentence = re.sub(r"[•▪◦]", "", sentence)

    # Normalize spaces
    sentence = re.sub(r"\s+", " ", sentence).strip()

    # Remove noisy headings
    for pattern in NOISE_PATTERNS:
        if re.search(pattern, sentence.lower()):
            return ""

    return sentence

def split_sentences(text):
    raw = re.split(r"(?<=[.!?])\s+", text)
    cleaned = []

    for s in raw:
        s = clean_sentence(s)
        if 40 <= len(s) <= 160:  # ideal sentence length
            cleaned.append(s)

    return cleaned

def score_sentence(sentence, keywords):
    score = 0
    words = sentence.lower().split()
    for k in keywords:
        if k in words:
            score += 2
    return score
