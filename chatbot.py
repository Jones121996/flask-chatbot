import re
import datetime

def chatbot_response(user_input, user_name):
    responses = {
        r"\bhi\b|\bhello\b|\bhey\b": f"Hello {user_name}! How can I assist you?",
        r"\bhow are you\b|\bhow do you do\b": "I'm just a bot, but I'm doing great!",
        r"\bwhat time is it\b|\bcurrent time\b": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
        r"\bbye\b|\bgoodbye\b": f"Goodbye {user_name}! Have a nice day!",
        r"\bhelp\b": "I can answer basic questions like time, greetings, and simple responses."
    }

    user_input = user_input.lower()

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "Sorry, I don't understand."

# Chat loop with user name memory
print("Chatbot (type 'exit' to stop)")
user_name = input("Bot: Hi! What's your name? ")

while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot_response(user_input, user_name))
