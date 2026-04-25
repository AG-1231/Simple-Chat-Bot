import random
 

responses = {
    "hello": [
        "hey! how's it going?",
        "hi there!",
        "hello! what's up?",
    ],
    "hi": [
        "hey! how's it going?",
        "hi there!",
        "hello! what's up?",
    ],
    "how are you": [
        "i'm doing great, thanks for asking!",
        "pretty good! how about you?",
        "all good on my end. you?",
    ],
    "your name": [
        "i'm just a simple chatbot, i don't have a real name.",
        "you can call me bot if you want.",
        "i don't have a name. you can give me one if you'd like.",
    ],
    "what can you do": [
        "i can answer simple questions! try asking me about the weather, jokes, or the time.",
        "not much honestly. ask me something and we'll find out.",
        "i know a few things. give me a question and i'll try.",
    ],
    "weather": [
        "i can't actually check the weather, but i hope it's nice where you are!",
        "no idea, i'm stuck inside this terminal. how's it looking out there?",
    ],
    "joke": [
        "why don't scientists trust atoms? because they make up everything.",
        "i told my computer i needed a break. now it won't stop sending me kit-kat ads.",
        "why do programmers prefer dark mode? because light attracts bugs.",
        "what do you call a fake noodle? an impasta.",
    ],
    "time": [
        "i don't have a clock on me, check your phone!",
        "no idea what time it is. i live outside of time.",
    ],
    "bye": [
        "bye! take care.",
        "see you later!",
        "catch you later!",
    ],
    "goodbye": [
        "bye! take care.",
        "see you later!",
        "take it easy!",
    ],
    "thanks": [
        "no problem!",
        "anytime!",
        "happy to help.",
    ],
    "thank you": [
        "no problem!",
        "anytime!",
        "you're welcome!",
    ],
    "who made you": [
        "someone typed me into existence. pretty wild.",
        "a human wrote my code. i'm not that fancy.",
    ],
    "age": [
        "i was just born today, honestly.",
        "i don't age. perks of being code.",
    ],
    "favorite color": [
        "probably black. i live in a terminal after all.",
        "i like green. very matrix-y.",
    ],
    "help": [
        "try asking me things like: tell me a joke, how are you, what's the weather, who made you.",
        "i understand basic questions. just type something and see what happens!",
    ],
}
 

fallbacks = [
    "hmm, i'm not sure about that one.",
    "good question, i don't really know.",
    "that's beyond my pay grade.",
    "i didn't quite get that. try asking something else.",
    "not sure what to say to that honestly.",
]
 
 
def get_response(message):
    message = message.lower().strip()
 
    
    for keyword, replies in responses.items():
        if keyword in message:
            return random.choice(replies)
 
    
    return random.choice(fallbacks)
 
 
def main():
    print("\n  simple chatbot")
    print("  type 'help' to see what i can do, 'quit' to exit\n")
 
    while True:
        user_input = input("  you: ").strip()
 
        if not user_input:
            continue
 
        if user_input.lower() in ("quit", "exit", "q"):
            print("  bot: alright, bye!\n")
            break
 
        reply = get_response(user_input)
        print(f"  bot: {reply}\n")
 
 
main()
