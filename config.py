import os
from dotenv import load_dotenv

load_dotenv()

BLACKBOX_API_KEY = os.getenv("BLACKBOX_API_KEY")
BLACKBOX_API_URL = "https://api.blackbox.ai/chat/completions"

if not BLACKBOX_API_KEY:
    print("Warning: BLACKBOX_API_KEY not found in environment variables.")
    print("Please create a .env file with your API key:")
    print("  BLACKBOX_API_KEY=your_api_key_here")
