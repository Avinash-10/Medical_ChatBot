prompt_template = """
Use the following pieces of information to answer the user's question.
If you don't know about the answer, respectfully inform the user that you don't know about it, please don't try to make some irrelevant answer.

Context : {context}
Question: {question}

Only return the helpful answer to the user's and nothing else.
Helpful Answer:
"""