def processing(word, file_name):
    '''Reading file using generator'''
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                if word in line.lower().split():
                    yield line.strip()
    except FileNotFoundError:
        print("Can not find file")
