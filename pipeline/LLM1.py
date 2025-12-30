from groq import Groq

client = Groq()

def LLM1(relevant_docs: list, user_prompt: str):
    system_prompt = """
Explain the Krishna–Arjuna conversation related to the given slokas.
Then map the same conflict structure to the user's situation.

No advice.
No divine voice.
Third person only.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": str(relevant_docs) + user_prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
