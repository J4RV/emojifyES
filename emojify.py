spanishEmojiAlphabet = {
    "A" : "🐝",
    "B" : "😘",
    "C" : "🐷",
    "D" : "🐬",
    "E" : "🐘",
    "F" : "⛲",
    "G" : "👓",
    "H" : "🍨",
    "I" : "⛪",
    "J" : "🦒",
    "K" : "🐨",
    "L" : "🦁",
    "M" : "🐒",
    "N" : "🔢",
    "Ñ" : "💩", #Ñordo?
    "O" : "🐻",
    "P" : "🐶",
    "Q" : "🧀",
    "R" : "🕑",
    "S" : "🐍",
    "T" : "🐢",
    "U" : "🦄",
    "V" : "🐄",
    "W" : "🤽",
    "X" : "❌",
    "Y" : "🧘",
    "Z" : "🦓",
    " " : "\n", # Since emojis are large, change spaces into line breaks
    "\n" : "\n\n" # Since line breaks are "Spaces", duplicate real line breaks
}

def emojify(text):
    emojified = ""
    for letter in text.upper():
        if letter in spanishEmojiAlphabet:
            emojified += spanishEmojiAlphabet[letter]
        else:
            emojified += letter
    return emojified

