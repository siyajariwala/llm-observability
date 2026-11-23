from dotenv import load_dotenv
from groq import Groq
import time

load_dotenv()

# Initialize the Groq client - use client to send requests to the Groq API
client = Groq()

# Define a function to ask questions to the Groq API
def ask(question):
    #start the timer to measure the time taken for the request
    start = time.time()
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": question}],
    )
    #stop the timer and print the time taken
    end = time.time()
    latency = end - start 
    tokens_in = response.usage.prompt_tokens
    tokens_out = response.usage.completion_tokens
    trace = {
        "prompt": question,
        "response": response.choices[0].message.content,
        "model": "openai/gpt-oss-20b",
        "latency_s": round(latency, 3),
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
    }
    print(trace)
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    print(ask("Say hi "))
    