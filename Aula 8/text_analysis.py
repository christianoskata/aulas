def word_count(word, text):

    return text.count(word)

def character_count(char, text):

    return text.count(char)

def sentence_count(text):
    print(text.split("s"))
    return len(text.split(" "))

if __name__ == "__main__":
    print(word_count("teste", "teste teste teste teste"))
    print(character_count("t", "teste teste teste teste"))
    print(sentence_count("teste teste teste teste retsr"))
