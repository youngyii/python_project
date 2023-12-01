def History(filename):
    file = open(filename, "r", encoding="UTF-8")
    res = file.read()
    print(res)
    print()
    file.close()
