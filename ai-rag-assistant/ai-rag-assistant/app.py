from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load knowledge base
with open("knowledge_base.txt", "r") as file:
    documents = file.read().split("\n\n")

# Create embeddings
doc_embeddings = model.encode(documents)

print("AI Knowledge Assistant (type 'exit' to stop)\n")

while True:

    query = input("You: ")

    if query.lower() == "exit":
        print("Bot: Goodbye!")
        break

    query_embedding = model.encode([query])

    scores = np.dot(doc_embeddings, query_embedding.T)

    best_match = np.argmax(scores)

    if scores[best_match] < 0.4:
        print("Bot: Sorry, I couldn't find relevant information.\n")
    else:
        print("Bot:", documents[best_match], "\n")
