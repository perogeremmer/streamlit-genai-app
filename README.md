# Kenari Streamlit Chatbot

A simple chatbot app built with Streamlit and the OpenAI SDK, using [Kenari](https://kenari.id/v1) as the OpenAI-compatible API gateway.

## Features

- Multi-turn chat with session memory
- Configurable model (default: `deepseek-v4-1-flash`)
- Clear chat button in the sidebar

## Requirements

- Python 3.10+

## How to Run

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file at the project root and add your Kenari API key:

```env
KENARI_API_KEY=your_api_key_here
```

4. Run the app:

```bash
streamlit run app.py
```

5. Open the app at http://localhost:8501.

## Notes

- The `.env` file is gitignored and must not be committed.
- Enter your Kenari API key in `.env`, or the app will show a warning and stop.
