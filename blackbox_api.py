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
        "messages": messages,
        "agentMode": {},
        "trendingAgentMode": {},
        "isMicMode": False,
        "maxTokens": 1024,
        "playgroundTopP": 0.9,
        "playgroundTemperature": 0.5,
        "isChromeExt": False,
        "githubToken": None,
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "clickedForceWebSearch": False,
        "visitFromDelta": False,
        "mobileClient": False,
        "userSelectedModel": None,
        "validated": BLACKBOX_API_KEY,
    }

    try:
        response = requests.post(
            BLACKBOX_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        result = response.text

        if result.startswith("$@$"):
            parts = result.split("$@$")
            if len(parts) > 2:
                result = parts[-1]

        return result.strip()

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
    prompt = f"Look at this screenshot and answer the following question: {question}"
    return send_to_blackbox(prompt, image_base64)
