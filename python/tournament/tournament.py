def tally(rows):
    score = {}
    for x in rows:
        row = x.split(';')
        team1 = row[0]
        team2 = row[1]
        if team1 not in score:
            score[team1] = [0,0,0,0,0]
        if team2 not in score:
            score[team2] = [0,0,0,0,0]
        if row[2] == "win":
            score[team1][0] += 1
            score[team1][1] += 1
            score[team1][4] += 3
            score[team2][0] += 1
            score[team2][3] += 1
        elif row[2] == "loss":
            score[team1][0] += 1
            score[team1][3] += 1
            score[team2][0] += 1
            score[team2][1] += 1
            score[team2][4] += 3
        elif row[2] == "draw":
            score[team1][0] += 1
            score[team1][2] += 1
            score[team1][4] += 1
            score[team2][0] += 1
            score[team2][2] += 1
            score[team2][4] += 1

    sorted_alpha = dict(sorted(score.items(), key=lambda a: a[0]))
    sorted_points = dict(sorted(sorted_alpha.items(), key=lambda a: a[1][4], reverse=True))

    header = "{0:<31}".format("Team"),"| MP ","|  W ","|  D ","|  L ","|  P"
    scoreboard = [''.join(header)]
    for y in sorted_points:
        line = "{0:<31}".format(y),"|  ",str(score[y][0])," |  ",str(score[y][1])," |  ",str(score[y][2])," |  ",str(score[y][3])," |  ",str(score[y][4])
        scoreboard.append(''.join(line))    
    return scoreboard