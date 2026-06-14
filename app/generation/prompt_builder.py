def build_prompt(query, contexts):

    context_text = "\n\n".join(contexts)

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is explicitly present, provide it.

If the answer is not explicitly present but can be reasonably inferred, state the inference and explain why.

If the answer cannot be determined, say:
"The document does not provide enough information."

Context:
{context_text}

Question:
{query}

Answer:
"""

    return prompt