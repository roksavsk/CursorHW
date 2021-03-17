#Task 1

with open("task1.txt", "r") as file:
    content = file.readlines()
    dictionary = {}
    for i in range(0, len(content), 2):
        content[i] = content[i].replace("\n", "")
        content[i + 1] = content[i + 1].replace("\n", "")
        dictionary.update({content[i]: content[i + 1]})
    print(dictionary)

#Task 1.2
    with open('task1.2.txt', 'w') as file:
        for item in dictionary.values():
            file.write(f'{item} ')

#Task 2
import pickle

with open("task2", "rb") as file:
    list1 = pickle.load(file)
    average = sum(list1)/len(list1)
    print(average)

#Task 3
import openpyxl

class Open:
    def __init__(self, name):
        self.file = openpyxl.load_workbook(name)

    def __enter__(self):
        return self.file

    def  __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with Open("test.xlsx") as file:
    print(file.active["A1"].value)
