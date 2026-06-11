from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

INTENTS = {
    "task": [
        "create a task",
        "add a task",
        "finish assignment",
        "add to my todo list",
        "I need to do something",
        "schedule work"
    ],

    "memory": [
        "remember my name",
        "remember my goal",
        "save this information",
        "store this fact",
        "my goal is AI Engineer"
    ],

    "reminder": [
        "remind me tomorrow",
        "set reminder",
        "don't let me forget",
        "remind me about interview",
        "notify me later"
    ],

    "chat": [
        "what is machine learning",
        "tell me a joke",
        "how are you",
        "explain transformers",
        "general conversation"
    ]
}


intent_embeddings = {}

for intent, examples in INTENTS.items():

    emb = model.encode(
        examples,
        convert_to_numpy=True
    )

    intent_embeddings[intent] = np.mean(
        emb,
        axis=0
    )


def classify_intent(message):

    user_embedding = model.encode(
        message,
        convert_to_numpy=True
    )

    best_intent = None
    best_score = -1

    for intent, embedding in intent_embeddings.items():

        score = cosine_similarity(
            [user_embedding],
            [embedding]
        )[0][0]

        if score > best_score:
            best_score = score
            best_intent = intent

    return {
    "intent": best_intent,
    "score": float(best_score)
    }