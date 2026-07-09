"""
Basic Rule-Based Chatbot
------------------------
A simple chatbot that responds to predefined user inputs.
Author: SARAN S
Language: Python 3
"""

def chatbot():
    print("=" * 40)
    print("      🤖 BASIC RULE-BASED CHATBOT")
    print("=" * 40)
    print("Type one of the following:")
    print("  • hello")
    print("  • how are you")
    print("  • what is your name")
    print("  • who created you")
    print("  • bye")
    print("-" * 40)
    
    while True:
        user = input("\nYou: ").strip().lower()
        if user == "hello":
            print("Bot: Hi! Nice to meet you. 😊")
        elif user == "how are you":
            print("Bot: I'm fine, thanks for asking!")
        elif user == "what is your name":
            print("Bot: My name is AlphaBot.")
        elif user == "who created you":
            print("Bot: I was created using Python.")
        elif user == "bye":
            print("Bot: Goodbye! Have a great day. 👋")
            break
        else:
            print("Bot: Sorry, I don't understand that.")
            print("Bot: Try typing 'hello' or 'help'.")
            
# Start the chatbot

if __name__ == "__main__":
    chatbot()
