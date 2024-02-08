class Caretaker:
    def __init__(self):
        self.memento = list()
        self.origin = Origin()

    def run(self):
        self.origin.state = "green"
        self.memento.append(self.origin.save())
        self.origin.state = "red"
        self.memento.append(self.origin.save())
        for mem in self.memento:
            print(self.origin.load(mem))


class Origin:
    def __init__(self):
        self.state = "yellow"
        self._save_line = 0

    def save(self):
        self._save_line += 1
        return Memento(self.state, self._save_line)

    @staticmethod
    def load(memento):
        saved_lines = list()
        with open("memento_save.txt", "r") as file:
            for line in file:
                saved_lines.append(line.strip())
        return saved_lines[memento.line - 1]


class Memento:
    def __init__(self, state, line):
        self.state = state
        self.line = line
        self._save_state_in_file(state)

    def get_state(self):
        return self.state

    @staticmethod
    def _save_state_in_file(state):
        with open("memento_save.txt", "a") as file:
            file.write(state + "\n")


if __name__ == '__main__':
    care = Caretaker()
    care.run()
