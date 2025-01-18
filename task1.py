def bot():
    print("The bot: hello!.I am a simple chatbot.Welcome you " )
    print("Type 'Stop' or 'Exit' to leave the chat")
    
    while True:
        
        question = input("User: ").lower()
        if question == "hello" or "hi":
            print("The bot: Hi! How can I help you")
        elif question == "how are you":
            print("The bot: I am just a user created program only, so I am not a human, but thanks for asking! amd How are you")
        elif question == "What type of program does you use":
            print("The bot: The 'Python ' is used for the program ")
        elif question == "exit" or "stop":
            print("The bot: Thank you! See you, have a nice day ")
            break
        else:
            print("The bot: I'm sorry, I don't know the answer for your question.Could you try asking something else? or some other questions ?")
            

bot()