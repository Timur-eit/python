import os

folder = r"./PythonPrim/Textfiles"

answ = set()

search = input("Введите поисковое слово или подстроку: ")


for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    # print(filepath)

    with open(filepath, "r") as fp:
        for line in fp:
            if search in line:
                answ.add(filename)

for i in answ:
    print(i)
