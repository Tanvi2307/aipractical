print("Chatbot: Hello! I am your chatbot.") 
print("Chatbot: Type 'bye' to exit.") 

while True: 
    user = input("You: ").lower().strip() 

    if "hello" in user or "hi" in user: 
        print("Chatbot: Hello! How can I help you?") 

    elif "name" in user: 
        print("Chatbot: I am a simple rule based chatbot.") 

    elif "how are you" in user: 
        print("Chatbot: I am fine. Thank you!") 

    elif "your age" in user: 
        print("Chatbot: I am just a computer program.") 

    elif "help" in user: 
        print("Chatbot: Sure! How can I help you?") 

    elif "thank" in user: 
        print("Chatbot: You are welcome!") 

    elif "bye" in user: 
        print("Chatbot: Goodbye! Have a nice day.") 
        break 
    else: 
        print("Chatbot: Sorry, I don't understand.")