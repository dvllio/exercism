import re

def is_isogram(string):
    cleanString = re.sub("[ -]", "", string).lower()
    return len(set(cleanString)) == len(list(cleanString))