class Person:
    def __init__(self, name):
        self._name = name
    

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name is not None:
            self._name = new_name
        else:
            raise ValueError("name must be a valid string")
