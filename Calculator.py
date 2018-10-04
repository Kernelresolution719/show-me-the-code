# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, DECIMAL, PLUS, MINUS, MULTIPLE, DIVIDE, EOF = 'INTEGER', 'DECIMAL', 'PLUS', 'MINUS', 'MULTIPLE', 'DIVIDE', 'EOF'

class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3 + 5", "12 - 5", etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]
 
    def error(self):
        raise Exception('Error parsing input')

    def next_token(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skipspace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.next_token()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.next_token()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skipspace()
                continue
            elif self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            elif self.current_char == '+':
                self.next_token()
                return Token(PLUS, '+')
            elif self.current_char == '-':
                self.next_token()
                return Token(MINUS, '-')
            elif self.current_char == '*':
                self.next_token()
                return Token(MULTIPLE, '*')
            elif self.current_char == '/':
                self.next_token()
                return Token(DIVIDE, '/')
            else:
                self.error()
                return Token(EOF, None)
        return None

    def handle_token(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
        #default is integer?
        left = self.current_token
        self.handle_token(INTEGER)
        operator = self.current_token
        if operator.type == PLUS:
            self.handle_token(PLUS)
        elif operator.type == MINUS:
            self.handle_token(MINUS)
        elif operator.type == MULTIPLE:
            self.handle_token(MULTIPLE)
        elif operator.type == DIVIDE:
            self.handle_token(DIVIDE)

        right = self.current_token
        self.handle_token(INTEGER)

        if operator.type == PLUS:
            result = left.value + right.value
        elif operator.type == MINUS:
            result = left.value - right.value
        elif operator.type == MULTIPLE:
            result = left.value * right.value
        elif operator.type == DIVIDE:
            result = left.value / right.value
        return result

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = raw_input('calculator:> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
 
if __name__ == '__main__':
    main()
