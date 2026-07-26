import  random

knowledge_base={
    "greeting": {
        "keywords": ["hello","hi","hey"],
        "responses": ["Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Good to see you."]
    },
    "how_are_you": {
        "keywords": ["how are you", "How do you do", "what's up"],
        "responses": [
            "I'm just a bunch of if else statements, but I'm doing great! How about you?",
            "Running smoothly, thanks for asking!",
             "Thanks for asking! i dont have feelings, but i am here to help you"]
    },
"name": {
        "keywords": ["name", "do you have a name", "what should i call you"],
        "responses": [
            "I am DecodeBot, a simple rule based chatbot built for Project 1.",
            "You can call me DecodeBot!",
            "I am DecodeBot,  a simple rule based chatbot created by NOOR FATIMA"
        ]
    },
    "help": {
        "keywords": ["help", "what can you do", "commands"],
        "responses": [
            "I can greet you, tell you about myself, tell a joke, or say goodbye. Try me!",
        ]
    },
    "joke": {
        "keywords": ["joke", "make me laugh", "funny"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I told my computer I needed a break, and it froze.",
            "Why did the math book look sad? Because it has too many problems"
        ]
    },
    "thanks": {
        "keywords": ["thank you", "thanks", "great job"],
        "responses": [
            "You're welcome!",
            "Anytime! Happy to help",
            "I am glad i could help"
        ]
    },
}

def sanitize(text):
    return text.lower().strip()

def get_response(user_input):
    for intent, data in knowledge_base.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return random.choice(data["responses"])

    return "I do not understand that yet. Try typing 'help' to see what I can do."

EXIT_COMMANDS = ["exit", "quit", "bye", "goodbye"]

def run_chatbot():
    print("DecodeBot: Hello! Type 'exit' to quit.")

    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize(raw_input_text)

        if clean_input in EXIT_COMMANDS:
            print("DecodeBot: Goodbye! Have a great day.")
            break

        reply = get_response(clean_input)
        print("DecodeBot:", reply)


run_chatbot()


