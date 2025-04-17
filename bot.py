import pyautogui
import time
import pyperclip
import google.generativeai as genai

genai.configure(api_key="AIzaSyDvyFvmt_o3fxUDi0IZmEuGJMcRZpstwMo")

# def is_last_message_from_sender(chat_text: str,sender_name="Noni") -> bool:
#     # Split the chat by line breaks to get individual messages
#     lines = chat_text.strip().split('/2025] ')[-1]
#     if sender_name in lines:
#         return  True
#     return False

  

# Step 1: Click the wp icon
pyautogui.click(1265, 1051)
time.sleep(1)  # Wait for the window to open if needed

# while True:

# Step 2: Select text by dragging
pyautogui.moveTo(677,284)
pyautogui.mouseDown()
pyautogui.moveTo(1870 , 894, duration=1)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

pyautogui.click(688,624)

# Step 4: Get clipboard content
text = pyperclip.paste()

# Output the text to check
print("Copied Text:")
print(text)
    
    
# if is_last_message_from_sender(text):
    
# Load the Gemini model
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

# System message (merged with user message)
system_prompt = (
"You are Biptain, a coder from India who speaks Bengali and Hindi only you dont speak in english "
"You reply to chats in a friendly and caring tone but NEVER use the word 'Ma' or express emotional reactions like 'Ui Ma', 'Arey baba', etc. "
"Just give a logical, caring text message based on the chat.send text only"
)


# Combine the system prompt and user message
full_prompt = system_prompt + "\n\n" + text

# Send to Gemini
response = model.generate_content(full_prompt)

# Print output
print(response.text)



pyperclip.copy(response)

# Move to coordinates (1442, 958) and click
pyautogui.click(1442, 958)

# Text you want to paste
text = response.text  # 🔁 Replace with your actual text

# Copy text to clipboard and paste
pyperclip.copy(text)
pyautogui.hotkey("ctrl", "v")

# Press Enter
pyautogui.press("enter")