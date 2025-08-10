import random
class GuessingGame:
    def __init__(self):
        number_range = range(1,101)
        self.number_to_guess = random.choice(number_range)
        self._guesses = 7
    def play(self):
        print(self.number_to_guess)
    
    @property
    def guesses(self):
        return self._guesses

    def number_of_guesses(self):
        return self._guesses
    
    def guess(self, user_guess):
        if self._guesses <= 0:
            return "No more guesses left."
        
        if user_guess < self.number_to_guess:
            self._guesses -= 1
            return "Higher! You have {} guesses left.".format(self._guesses)
        elif user_guess > self.number_to_guess:
            self._guesses -= 1
            return "Lower! You have {} guesses left.".format(self._guesses)
        else:
            return "Congratulations! You've guessed the number."

game = GuessingGame()
game.play()