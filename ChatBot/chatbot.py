import openai

# Set up the OpenAI API key
openai.api_key = "api-key"

def chatbot_conversation():
    print("Welcome to the ChatGPT chatbot! Type 'exit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Make a call to the ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        # Extract the response content
        bot_reply = response.choices[0].message['content']
        print(f"Chatbot: {bot_reply}")

# Run the chatbot
chatbot_conversation()
