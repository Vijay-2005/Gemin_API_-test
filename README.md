# Gemini API Test Project

A simple Python project demonstrating how to use Google's Gemini API for generative AI.

## Prerequisites

- Python 3.6 or higher
- Google Gemini API key

## Installation

1. Clone this repository or download the files
2. Install the required packages:

```bash
pip install google-generativeai
```

## Setup

Before running the code, you need to set up your API key:

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/)
2. Set your API key as an environment variable (recommended):
   - Windows PowerShell: `$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"`
   - Linux/Mac: `export GEMINI_API_KEY="YOUR_API_KEY_HERE"`
   
Alternatively, you can directly configure the API key in the code (not recommended for production):
```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

## Usage

Run the sample script:

```bash
python testapi.py
```

The script will connect to the Gemini API and ask "who made you", then print the response.

## Customization

You can modify the prompt in the `generate_content()` function to ask different questions or provide different prompts to the model.

You can also change the model by modifying the model name:
```python
model = genai.GenerativeModel('gemini-1.5-flash')  # Try other models like 'gemini-pro'
```

## License

[Add your license information here]