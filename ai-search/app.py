questions = [
    "What is Java?",
    "What is Python?",
    "What is Artificial Intelligence?",
    "What is Machine Learning?"
]

answers = [
    "Java is a programming language used for building applications.",
    "Python is used for AI, data science, and web development.",
    "Artificial Intelligence is the simulation of human intelligence in machines.",
    "Machine learning is a part of AI where systems learn from data."
]

query = input("Ask a question: ").lower()

for i in range(len(questions)):
    if query in questions[i].lower():
        print("Answer:", answers[i])
        break
else:
    print("Sorry, answer not found.")
