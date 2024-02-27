class Expression:
    def interprete(self):
        pass


class Terminal(Expression):
    def __init__(self, expression):
        self.expression = int(expression)

    def interprete(self):
        return self.expression


class Parser:
    @staticmethod
    def parse(expression):
        tokens = []
        temp = ""
        for token in expression:
            if token.isdigit():
                temp += token
                continue
            else:
                tokens.append(temp)
                temp = ""
            tokens.append(token)
        if temp:
            tokens.append(temp)
        return tokens


class NonTerminal(Expression):
    def __init__(self, expression):
        self.tokens = expression
        self.OPERATORS = ['+', '*']

    def interprete(self):
        while len(self.tokens) != 1:
            for i, token in enumerate(self.tokens):
                left = i - 1
                right = i + 1
                if left >= 0 and right < len(self.tokens):
                    if token == '*':
                        self.tokens[left] = self.mul(Terminal(self.tokens[left]), Terminal(self.tokens[right]))
                        self.tokens.pop(right)
                        self.tokens.pop(i)

            for i, token in enumerate(self.tokens):
                left = i - 1
                right = i + 1
                if left >= 0 and right < len(self.tokens):
                    if token == '+':
                        self.tokens[left] = self.add(Terminal(self.tokens[left]), Terminal(self.tokens[right]))
                        self.tokens.pop(right)
                        self.tokens.pop(i)

        return self.tokens[0]

    def mul(self, left, right):
        return left.interprete() * right.interprete()

    def add(self, left, right):
        return left.interprete() + right.interprete()


if __name__ == '__main__':
    EXPRESSION = "1+2226*156"
    terminal = NonTerminal(Parser.parse(EXPRESSION))
    print(terminal.interprete())
