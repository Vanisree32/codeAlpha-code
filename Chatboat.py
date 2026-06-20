def reply(message):

    responses = {
        "hello": "Hi!",
        "how are you": "I am fine, thanks!",
        "what is your name": "I am CodeAlpha Bot",
        "bye": "Goodbye!"
    }

    return responses.get(
        message.lower(),
        "Sorry, I don't understand."
    )


print("=== BASIC CHATBOT ===")

while True:

    user = input("You: ")

    response = reply(user)

    print("Bot:", response)

    if user.lower() == "bye":
        break
