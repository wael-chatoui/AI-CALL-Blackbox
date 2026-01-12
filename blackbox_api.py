import requests
from config import BLACKBOX_API_KEY, BLACKBOX_API_URL


def send_to_blackbox(question: str, image_base64: str = None) -> str:
    """
    Send a question (optionally with an image) to the Blackbox API.

    Args:
        question: The user's question
        image_base64: Base64-encoded image of the screen (optional)

    Returns:
        The AI's response text
    """
    if not BLACKBOX_API_KEY:
        return "Error: BLACKBOX_API_KEY not configured. Please set it in your .env file."

    headers = {
        "Authorization": f"Bearer {BLACKBOX_API_KEY}",
        "Content-Type": "application/json",
    }

    messages = []

    if image_base64:
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_base64}"
                    }
                },
                {
                    "type": "text",
                    "text": question
                }
            ]
        })
    else:
        messages.append({
            "role": "user",
            "content": question
        })

    payload = {
        "model": "grok",
        "messages": messages,
        "max_tokens": 1024,
        "temperature": 0.7,
    }

    try:
        response = requests.post(
            BLACKBOX_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        if not response.ok:
            error_detail = response.text[:500] if response.text else "No response body"
            return f"Error: API returned {response.status_code}. Details: {error_detail}"

        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"].strip()
        else:
            return response.text.strip()

    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Blackbox API: {e}"


def chat_with_screen(question: str, image_base64: str) -> str:
    """
    Send a question about the screen to Blackbox AI.

    Args:
        question: What the user wants to know about the screen
        image_base64: Base64-encoded screenshot

    Returns:
        AI's analysis/response
    """
    prompt = f"Regarde cette capture d'écran et réponds en français à la question suivante: {question}"
    return send_to_blackbox(prompt, image_base64)
