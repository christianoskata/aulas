def reverse_string(text):
    return text[::-1]

def capitalize_string(text):
    return text.capitalize()

def replace_spaces(text, replace):
    return text.replace("a", replace)

if __name__ == "__main__":

    print(reverse_string("ABCD"))
    print(capitalize_string("abcd test"))
    print(replace_spaces("Uma maça", "_"))