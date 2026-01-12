# Screen AI Assistant

A voice-controlled AI assistant that can see your screen and answer questions about it, powered by Blackbox AI.

## Features

- Voice input using speech recognition
- Real-time screen capture
- AI-powered screen analysis via Blackbox API
- Text-to-speech responses

## Requirements

- Python 3.10+
- Microphone
- Blackbox API key

## Installation

### 1. Clone or navigate to the project

```bash
cd screen-ai-assistant
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install system dependencies (Linux)

```bash
sudo apt install portaudio19-dev python3-pyaudio espeak
```

### 4. Configure your API key

Create a `.env` file in the project root:

```
BLACKBOX_API_KEY=your_api_key_here
```

## Usage

Run the assistant:

```bash
python main.py
```

Then:
1. Wait for "Listening..." prompt
2. Speak your question about what's on your screen
3. The AI will capture your screen, analyze it, and respond via voice
4. Say "exit" or "quit" to stop

## Example Questions

- "What application is open on my screen?"
- "Can you read the text in this window?"
- "What error message do you see?"
- "Describe what's on my screen"

## Project Structure

```
screen-ai-assistant/
├── main.py              # Application entry point
├── voice_input.py       # Speech recognition module
├── screen_capture.py    # Screen capture utilities
├── blackbox_api.py      # Blackbox API client
├── text_to_speech.py    # Text-to-speech module
├── config.py            # Configuration loader
├── requirements.txt     # Python dependencies
├── .env                 # API key (create this)
└── README.md            # This file
```

## Troubleshooting

### "No module named pyaudio"

Install PortAudio first:
```bash
# Ubuntu/Debian
sudo apt install portaudio19-dev
pip install pyaudio

# Arch Linux
sudo pacman -S portaudio
pip install pyaudio

# macOS
brew install portaudio
pip install pyaudio
```

### "BLACKBOX_API_KEY not found"

Create a `.env` file with your API key:
```bash
echo "BLACKBOX_API_KEY=your_key" > .env
```

### Speech recognition not working

- Check your microphone is connected and working
- Ensure you have internet connection (Google Speech API requires it)
- Speak clearly and wait for "Listening..." prompt

## License

MIT
# AI-CALL-Blackbox
