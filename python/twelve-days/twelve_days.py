def recite(start_verse, end_verse):
    nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"}

    gifts = {
    12: "twelve Drummers Drumming, ",
    11: "eleven Pipers Piping, ",
    10: "ten Lords-a-Leaping, ",
    9: "nine Ladies Dancing, ",
    8: "eight Maids-a-Milking, ",
    7: "seven Swans-a-Swimming, ",
    6: "six Geese-a-Laying, ",
    5: "five Gold Rings, ",
    4: "four Calling Birds, ",
    3: "three French Hens, ",
    2: "two Turtle Doves, ",
    1: "a Partridge in a Pear Tree."}

    verses = []

    for i in range(start_verse, end_verse+1):
        string = "On the "+nth[i]+" day of Christmas my true love gave to me: "
        if i == 1:
            string += gifts[1]
        else:
            for j in range(i,1,-1):
                string += gifts[j]
            string += "and "+gifts[1]
        verses.append(string)
    return verses