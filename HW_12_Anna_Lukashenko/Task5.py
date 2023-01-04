'''Считать файл hw.csv и посчитать средний рост, средний вес в см и кг соответственно'''
import csv
def hw_csv_average():
    #open and read csv file, convert it to list
    with open('hw.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    height = []
    weight = []
    #iterate through a list of dictionaries and adding weight and height in two separate lists
    for i in data:
        height.append(float(i[' "Height(Inches)"']))
        weight.append(float(i[' "Weight(Pounds)"']))
    return f" Average height is: {round(sum(height)/len(height),2)} cm,\n Average weight is: {round(sum(weight)/len(weight),2)} kg."
print(hw_csv_average())

