import string

def abbreviate(words):
    
    for a in string.punctuation:
        if a == "'":
            pass
        else:
            words = words.replace(a, ' ')

    return ''.join([word[0].upper() for word in words.split()])