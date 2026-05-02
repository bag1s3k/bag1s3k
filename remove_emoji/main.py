import emoji


def custom_emoji_replace(emoji_char, data_dict):
    if emoji_char == "🐤":
        return "Bird"
    elif emoji_char == "🦉":
        return "Owl"

    return "\x00"


with open("README.md", "r+", encoding="utf-8") as f:
    text = f.read()
    f.seek(0)
    f.truncate()

    highlight_emoji = emoji.replace_emoji(text, replace=custom_emoji_replace)
    clean_text = highlight_emoji.replace("\x00 ", "")

    f.write(clean_text)

    print(clean_text)