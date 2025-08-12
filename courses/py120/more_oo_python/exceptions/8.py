def get_age(name):
    students = {'John': 25, 'Jane': 22, 'Doe': 30}
    try:
        return students[name]
    except KeyError:
        print("name is not in the dictionary")
        



print(get_age("Joh"))