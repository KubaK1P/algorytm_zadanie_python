import re

def chatbot_response(user_input):
    responses = {
        r".*\b(hi|hello|hey)\b.*": "Hello! How can I assist you?",
        r".*\b(how are you|how's it going)\b.*": "I'm just a computer program, but I'm functioning well. How can I help you?",
        r".*\b(bye|goodbye)\b.*": "Goodbye! Have a great day!",
        r".*\b(thank you|thanks)\b.*": "You're welcome! If you have any more questions, feel free to ask.",
        r".*\b(thank you|thanks)\b.*": "You're welcome! If you have any more questions, feel free to ask."
    }

    for pattern, response in responses.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return response
    
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Chatbot: Hello! How can I assist you? (Type 'bye' to exit)")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
