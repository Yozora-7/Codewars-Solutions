"""
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""

def points(games):
    total = 0
    for i in games:
        j = i.split(':')
        if j[0] > j[1]:
            total += 3
        elif j[0] == j[1]:
            total += 1
    return total
  
# another example

def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))
