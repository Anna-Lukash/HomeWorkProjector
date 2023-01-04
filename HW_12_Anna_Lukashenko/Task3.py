'''Write a program that will simulate user score in a game. Create a list with 5 player's names. After that simulate 100 games for each player. As a result of the game create a list with player's name and his score (0-1000 range). And save it to a CSV file. File should looks like this:
Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345'''
import csv
from random import randint
players_names = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']

with open('game.csv', 'w') as a:
    writer = csv.DictWriter(a, fieldnames = ['Player name', 'Score'])
    writer.writeheader()
for i in range(0,100):
    for i in players_names:
        with open('game.csv', 'a') as g:
            writer = csv.writer(g)
            writer.writerow([i, str(randint(1,1000))])
            


    

    
    
    


                   