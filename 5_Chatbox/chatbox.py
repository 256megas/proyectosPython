# pip install google-generativeai
# https://medium.com/@BenjaminExplains/build-an-ai-chatbot-in-python-easy-and-free-8667b7b4232c

import google.generativeai as ai

# API Key
API_KEY = ''

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new modelcomo
chat = model.start_chat()

# Loop until the user types 'bye'
while True:
    # Get user input
    message = input('You: ')
    # End chat if 'bye' is entered
    if (message.lower() == 'bye' or message.lower() == 'adios'):
        print('Chatbot: Goodbye!')
        break
    # Send message to AI and print the response
    response = chat.send_message(message)
    print('Chatbot:', response.text)
