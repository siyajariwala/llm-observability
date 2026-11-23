# LLM Observability

A lightweight tool that records what an LLM app is doing (prompts, responses,
latency, token usage) so teams can see how their AI features perform in production.

> **Status: early development.** Right now the repo has a small test chatbot
> and the first version of per-call recording. The API server, database,
> and dashboard are not built yet.

## The problem
Teams ship LLM features but can't see what happens after launch: slow
responses, surprise costs, and answers that may be made up. This project is
a small version of tools like Langfuse and LangSmith, built to learn how
they work inside.

## Planned architecture
SDK -> FastAPI ingestion API -> PostgreSQL
(later: Redis queue + worker for cost and hallucination checks, dashboard)

## Run it
Requires Python 3.9+ and a Groq API key.

1. Clone the repo and create a virtual environment:
   python3 -m venv venv && source venv/bin/activate
2. Install dependencies:
   pip install groq python-dotenv
3. Create a `.env` file in the project root:
   GROQ_API_KEY=your_key_here
4. Run the test chatbot:
   python3 sdk/chatbot.py

## Design decisions
See [DECISIONS.md](DECISIONS.md) (coming soon).
