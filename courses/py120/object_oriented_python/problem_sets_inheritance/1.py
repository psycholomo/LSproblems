class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

class BullDog(Dog):

    def __init__(self):
        super().__init__()
    def sleep(self):
        return 'snoring!'
teddy = BullDog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!class Dog:
