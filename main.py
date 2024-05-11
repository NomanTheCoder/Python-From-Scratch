def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        ":)": "😘",
        ":(": "🤣",
        ":/": "😒",
        ":@": "😁",
        ":£": "😍",
        "help": """
        For Information Please Type info
        """,
        "info": """
        for This emoji 😘 Please Type:)
        for This emoji 🤣 Please Type:(
        for This emoji 😒  Please Type:/
        for This emoji 😁 Please Type:@
        for This emoji 😍 Please Type:£
        """
    }
    output = ""
    for emo in words:
        output += emoji.get(emo, emo) + " "
    return output

while True:
    message = input(">")
    if message.lower() == "quit":
        break
    print(emoji_converter(message))