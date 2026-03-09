import ollama


def summarize_document(extracted_text):

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role":"user",
                "content":f"Summarize this document:\n{extracted_text}"
            }
        ]
    )

    return response['message']['content']


def extract_structured_data(extracted_text):

    prompt = f"""
Extract important information from this document.

Return JSON with:
Name
Date
Amount
Address

Document:
{extracted_text}
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role":"user","content":prompt}]
    )

    return response['message']['content']