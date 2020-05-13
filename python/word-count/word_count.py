import string

def count_words(sentence):
    count = {}

    for a in string.punctuation:
        if a == "'":
            pass
        else:
            sentence = sentence.replace(a, ' ')

    phrase = [word.strip("'") for word in sentence.lower().split()]

    for b in phrase:
        if b in count:
            count[b] += 1
        else:
            count[b] = 1
    return count