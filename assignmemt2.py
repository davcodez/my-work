def convert_to_emoji(text):
    emoji_dict = {
        ":)": "😃",
        ":(": "😞",
        "<3": "❤️",
        ":D": "😄",
        ":P": "😛",
        ":O": "😮",
        ";)": "😉",
        "xD": "😆",
        ":|": "😐",
        ":*": "😘",
        ":$": "🤑",
        ":@": "😡",
        ":S": "😕",
        ":|": "😐",
        ":/": "😕",
        ":')": "😂",
        ">:(": "😠",
        ":poop:": "💩",
        ":fire:": "🔥"
    }

    for key, value in emoji_dict.items():
        text = text.replace(key, value)

    return text


text = input("Enter some text: ")
converted_text = convert_to_emoji(text)
print("Converted text:", converted_text)
