'''2. Create file with some content. As example you can take this one
    Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу,
Create second file and copy content of the first file to the second file in upper case.'''

with open("text.txt", "w") as t:
    t.write("Тому що ніколи тебе не вирвеш,\nніколи не забереш,\nтому що вся твоя свобода,\nскладається з меж,\nтому що в тебе немає \nжодного вантажу,\nтому що ти ніколи не слухаєш \nоскільки знаєш і так, \nщо я скажу")
#1 solution
with open("text.txt", "r") as t:
    for line in t:
        with open("text_upper.txt","a") as t_u:
            t_u.write(line.upper())
#2 solution   
with open("text.txt", "r") as t:
    with open("text_upper.txt","a") as t_u:
        t_u.write(t.read().upper())