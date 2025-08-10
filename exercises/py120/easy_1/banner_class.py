class Banner:
    def __init__(self, message):

        self.message = message
        self._length = len(message)

    

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return "|" + (" " * (self._length + 2)) + "|"

    def _horizontal_rule(self):
        return "+" + ("-" * ( self._length + 2)) + "+"
        

    def _message_line(self):
        return f"| {self.message} |"



banner = Banner('To boldly go where no one has gone before.')
print(banner)

banner = Banner('')
print(banner)