# AI Knowledge Retrieval Assistant using Endee Vector Database

## Project Overview
This project demonstrates a simple AI assistant that retrieves relevant knowledge using vector similarity search.

The system converts user queries into vector embeddings and finds the most similar document from a knowledge base.

## Use Case
This type of system is used in:

- AI chatbots
- Semantic search systems
- Retrieval Augmented Generation (RAG)
- Knowledge assistants

## System Design

User Query
   ↓
Convert query into vector embedding
   ↓
Search similar vectors
   ↓
Retrieve most relevant document
   ↓
Return answer to user

## Technologies Used

- Python
- Sentence Transformers
- Vector similarity search
- Endee vector database concept

## Setup Instructions

1. Install Python

2. Install dependencies

pip install -r requirements.txt

3. Run the program

python app.py

## Example

You: What is Artificial Intelligence?

Bot: Artificial Intelligence is the simulation of human intelligence in machines.
