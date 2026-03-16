# AI Knowledge Retrieval Assistant using Endee

## Project Overview
This project demonstrates a simple AI assistant that performs semantic search using vector embeddings. 
The assistant retrieves the most relevant information from a knowledge base based on user queries.

## Use Case
This system demonstrates concepts used in modern AI applications such as:

- Semantic Search
- Retrieval Augmented Generation (RAG)
- AI Knowledge Assistants
- Chatbots

## System Design

User Query
    ↓
Convert query to vector embedding
    ↓
Similarity search
    ↓
Retrieve most relevant knowledge
    ↓
Return response to user

## Technologies Used

- Python
- Sentence Transformers
- Vector embeddings
- Semantic search

## Project Structure

ai-rag-assistant/
    app.py
    knowledge_base.txt
    requirements.txt
    README.md

## Setup Instructions

1. Install Python
2. Install dependencies

pip install -r requirements.txt

3. Run the program

python app.py

## Example

You: What is Artificial Intelligence?

Bot: Artificial Intelligence is the simulation of human intelligence in machines.
