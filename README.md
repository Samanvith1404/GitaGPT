# Talk to Krishna

Talk to Krishna is a narrative-based AI system that frames human dilemmas using the Bhagavad Gita as contextual grounding — without advice, prescriptions, or religious authority.

The system listens to long personal stories, extracts causal conflicts, maps them to the Krishna–Arjuna dialogue, and presents a neutral reflective frame.

---

## Core Principles

- No advice or prescriptions  
- No divine impersonation  
- No moral instruction  
- No emotional manipulation  
- Human agency is always preserved  

---

## Architecture

User Story  
→ Chunking LLM (causal problem extraction)  
→ Vector Database (Bhagavad Gita)  
→ LLM-1 (Krishna–Arjuna conversation + user mapping)  
→ LLM-2 (decision framing)  
→ LLM-3 (final structured neutral output with sloka references)

---

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env
```

---

## Data Ingestion

Run once to ingest the Bhagavad Gita into Weaviate:

```bash
python data_ingestion/ingest_gita.py
```

---

## Running the Pipeline

```python
from pipeline.process import process

output = process(user_story)
print(output)
```

---

## Design Philosophy

This system is intentionally non-directive.  
It does not tell the user what to do.  
It does not interpret religious truth.  

It only reframes the situation using classical context.

---

## Disclaimer

This project is intended for reflection and research purposes only.  
It does not provide mental health, legal, or religious advice.
