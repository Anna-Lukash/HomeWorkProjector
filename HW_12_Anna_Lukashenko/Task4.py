import csv
with open('game.csv', 'r') as file:
    reader = csv.DictReader(file)
    game_records = list(reader)

    
high_score = {}
high_score['Josh'] = max([int(i['Score']) for i in game_records if i['Player name'] == "Josh"])
high_score['Luke'] = max([int(i['Score']) for i in game_records if i['Player name'] == "Luke"])
high_score['Kate'] = max([int(i['Score']) for i in game_records if i['Player name'] == "Kate"])
high_score['Mark'] = max([int(i['Score']) for i in game_records if i['Player name'] == "Mark"])
high_score['Mary'] = max([int(i['Score']) for i in game_records if i['Player name'] == "Mary"])
print(high_score)
high_score_list = sorted(high_score.items(), key=lambda x:x[1],reverse=True)

header = ['Name', 'Score' ]
with open('high.csv', mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
with open('high.csv', mode='a') as file:
    writer2= csv.writer(file)
    for i in high_score_list:
        writer2.writerow(i)
    
    
  
