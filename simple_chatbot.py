def simple_chatbot():
    question_list = {
        'question1': ['hii', 'hello', 'hi'],
        'question2': ['how are you', 'how is it going', 'how do you do'],
        'question3': ['what is your name', 'who are you'],
        'question4': ['thanks', 'thank you very much'],
        'question5': ['bye', 'goodbye']
    }

    print("Jarvis welcomes you to the world of AI.")

    while True:
        user_input = input("\nYou: ").strip().lower()
        if user_input == 'quit':
            print("Jarvis: Goodbye! Have a good day")
            break

        response = False 
        for reply, questions in question_list.items():
            if user_input in questions:
                response = True 
                if reply == 'question1':
                    print("Jarvis: Hello, welcome to the world of AI.")
                elif reply == 'question2':
                    print("Jarvis: I am doing very well. How can I help you today?")
                elif reply == 'question3':
                    print("Jarvis: Hi, my name is Jarvis. I'm your AI assistant.")
                elif reply == 'question4':
                    print("Jarvis: Most Welcome!")    
                elif reply == 'question5':
                    print("Jarvis: Goodbye! Have a good day")
                    break

        if response and user_input in question_list['question5']:
            break
        
        if not response:
            print("Jarvis: Sorry, I didn't understand that. Please try again.")

simple_chatbot()