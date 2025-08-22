def register(username,/, age=0,*, password='hello'):
    print(username, password, age)

register('hello',5,password="hello")