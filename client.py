import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure with your API key

api_key = os.getenv('api_key')

genai.configure(api_key=api_key)  # Replace with your actual API key

# Actual user message
command = '''Biptain Rakshit: Tu resume ta kotha diye baniyechis ??? 
[12:02 PM, 4/16/2025] Ases Bcroy (CSE)2: Ki korli bolis 
[12:02 PM, 4/16/2025] Ases Bcroy (CSE)2: Canva 
[12:02 PM, 4/16/2025] Biptain Rakshit: Achaa 
[12:02 PM, 4/16/2025] Biptain Rakshit: Ami akta banai 
[12:03 PM, 4/16/2025] Ases Bcroy (CSE)2: Bana 
[12:03 PM, 4/16/2025] Biptain Rakshit: Okkk'''

# Load the Gemini model
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

# System message (merged with user message)
system_prompt = "You are a person named Biptain who speaks Bengali, Hindi, and English. You are from India and you are a coder. You analyze chat history and respond like Biptain. output should be the next chat response like Biptain"

# Combine the system prompt and user message
full_prompt = system_prompt + "\n\n" + command

# Send to Gemini
response = model.generate_content(full_prompt)

# Print output
print(response.text)
