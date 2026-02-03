# GameFroze-AI
# GameFroze-AI 🎮🤖

**GameFroze-AI** is a fine-tuned Large Language Model designed specifically to assist developers working with the **Godot Engine**.  
The model is trained to understand Godot-related concepts, scripting patterns, and common development workflows.

It is deployed on **:contentReference[oaicite:0]{index=0}** and served via a lightweight **FastAPI** backend, with a web-based interface for easy interaction.


## What is GameFroze-AI?

GameFroze-AI helps game developers by:
- Answering Godot Engine–specific questions
- Assisting with scripting logic and debugging ideas
- Explaining engine concepts in a developer-friendly way
- Acting as an AI assistant tailored for game development workflows

This is **not a generic chatbot** — it is adapted for a focused domain.



##  Model Details

- **Base Model:** LLM (fine-tuned)
- **Training Type:** Supervised fine-tuning
- **Dataset Size:** ~3.8k custom Godot-focused samples
- **Domain:** Godot Engine (game development)
- **Inference Hardware:** CPU (Hugging Face Spaces)



##  Deployment

- **Model Hosting:** Hugging Face  
- **Demo Environment:** Hugging Face Spaces (CPU-based)
- **Backend API:** FastAPI
- **Frontend:** Web application (custom UI)

The system is designed so that:





##  Live Demo

- **Hugging Face Space:** *(add your Space link here)*  
- **Hugging Face Model:** *(add your model link here)*  

> Note: The demo runs on CPU, so responses may take a few seconds.



##  Tech Stack

- Python  
- FastAPI  
- Hugging Face (Model + Spaces)  
- REST API  
- Godot-focused dataset  



##  Running Locally (Backend Only)

```bash
git clone https://github.com/Sonai12345ss/GameFroze-AI.git
cd GameFroze-AI
pip install -r requirements.txt
uvicorn main:app --reload
