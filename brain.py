import re
import os
from groq import Groq
from body.speak import speak

def brain(txt):
    client = Groq(api_key = os.getenv("GROQ_API_KEY")  # Load from environment variable
)

    system_prompt = (
        "You are Shadow, an AI assistant. "
        "Respond with **concise, accurate, and direct answers** only. "
        "Do **not** explain your reasoning. "
        "Do **not** show thoughts, guesses, or inner monologue. "
        "Do **not** use <think> tags. "
        "Use proper punctuation. "
        "If the question is vague, politely ask for clarification instead of guessing."
    )


    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": txt}
    ]

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.2,
        max_tokens=100,
        top_p=0.9,
        stream=True
    )

    # Buffer for accumulating output and removing <think>...</think>
    output_buffer = ""

    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        output_buffer += content


        # Step 1: Remove <think>...</think> block
    cleaned = re.sub(r"<think>.*?</think>", "", output_buffer, flags=re.DOTALL).strip()
    cleaned = cleaned.replace("user", "sir")
    # Step 2: Truncate after the last full stop
    last_full_stop = cleaned.rfind(".")
    if last_full_stop != -1:
        cleaned = cleaned[:last_full_stop + 1]
    speak(cleaned)

