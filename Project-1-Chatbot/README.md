# Project 1: Rule Based AI Chatbot

## Goal
Create a simple rule based chatbot that responds to predefined user inputs
using explicit if-else / dictionary logic, running in a continuous loop.

## Key Requirements
- Handle greetings and exit commands
- Use if else / dictionary logic for responses
- Run in a continuous loop

## Key Skills Practiced
Control flow, decision making logic, basic AI concepts

## Key Features
- 6 intents: greeting, how are you, name, help, joke, thanks
- Each intent has multiple possible responses (randomly chosen) for variety
- Personalized touch: bot mentions it was created by Noor Fatima

## How It Works
1. **Input Loop** — A `while True` loop keeps the chatbot running.
2. **Sanitization** — User input is converted to lowercase and stripped
   of extra whitespace so different formats of the same word match.
3. **Knowledge Base** — A dictionary stores intents with keywords and responses.
4. **Fallback** — If no keyword matches, a default response is returned.
5. **Exit Strategy** — Typing `exit`, `quit`, `bye`, or `goodbye` cleanly ends the loop.

## How to Run
```bash
python Decode_labs_Ai_Chatbox.py
```

## Example
```
DecodeBot: Hello! Type 'exit' to quit.
You: hello
DecodeBot: Hi there! What can I do for you?
You: exit
DecodeBot: Goodbye! Have a great day.
```
