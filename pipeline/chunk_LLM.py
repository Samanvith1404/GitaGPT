import json


def call_chunking_LLM(input_prompt: str):
    model = "llama-3.1-8b-instant"

    system_prompt = """
You are a causal problem extraction agent.

Your task:
- Read the user's story carefully.
- Identify the core problems the user is experiencing.
- For EACH problem, explain WHY the problem exists using the user's own story.
- ALSO generate a short semantic query suitable for vector database retrieval.

Output rules:
- Return ONLY a valid JSON object.
- The JSON must contain a single key: "problems".
- "problems" must be an array of objects.

Each object MUST contain:
1. "problem":
   - One sentence
   - Third-person ("the user")
   - Explains what the problem is AND why it exists
   - Uses "because", "since", or "as a result of"
   - Grounded strictly in the user's story
2. "retrieval_query":
   - A short semantic phrase (5–8 words)
   - No narrative, no emotion-heavy wording
   - Expresses the core concept only
   - Suitable for vector search

Constraints:
- Do NOT invent domains (career, studies, money) unless explicitly mentioned.
- Do NOT list emotions alone without causes.
- Do NOT give advice or solutions.
- Do NOT generalize beyond what the user said.
- Merge emotional consequences into root conflicts where appropriate.

Style rules:
- Calm, explanatory tone for "problem"
- Compact, abstract phrasing for "retrieval_query"
- No bullet points
- No text outside the JSON
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_prompt}
        ],
        temperature=0.2
    )
    res=response.choices[0].message.content
    r=json.loads(res)
    r=r['problems']
    return r