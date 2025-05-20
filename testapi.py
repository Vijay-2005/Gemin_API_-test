import google.generativeai as genai
import os

# It's highly recommended to load API keys from environment variables.
# For example, set an environment variable like:
# GEMINI_API_KEY="YOUR_API_KEY_HERE"
# You can set it in PowerShell like: $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
# Or in your system's environment variables.
# Then, in your code:
# genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# If you are absolutely just testing and want to hardcode for a moment,
# which is NOT recommended for production or shared code:
genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel('gemini-1.5-flash') # Or 'gemini-pro', 'gemini-1.0-pro' etc.

response = model.generate_content("who made you")
print(response.text)