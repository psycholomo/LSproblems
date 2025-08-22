def find_person(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():

        if value == 'antonia':
            print('hello')
            print(kwargs['profession'])

print(find_person(name="antonia", profession="scientist"))
