
class IfGenerator:
    def __init__(self):
        self.code = ''
        self.statement = False
        self.level = 0

    def _close_line(self):
        if self.code:
            if self.statement:
                if not self.code.endswith(':'):
                    self.code += ':'
                self.level += 1
                self._new_line()
                self.statement = False
            else:
                self._new_line()

    def _new_line(self):
        self.code += '\n'
        self.code += '\t' * self.level

    def add_if(self, condition: str = ''):
        self._close_line()
        self.statement = True
        self.code += 'if '
        self.code += condition.strip()

    def add_elif(self, condition: str = ''):
        if self.statement:
            raise Exception('Add at least one line of code to the current statement')
        self.level_down()
        self._close_line()
        self.statement = True
        self.code += 'elif '
        self.code += condition.strip()

    def add_else(self):
        if self.statement:
            raise Exception('Add at least one line of code to the current statement')
        self.level_down()
        self._close_line()
        self.code += 'else:'
        self.statement = True

    def add_line(self, code: str):
        self._close_line()
        self.code += code
        if code.endswith(':'):
            self.level_up()

    def and_(self, condition: str = ''):
        if self.statement:
            self.code += ' and '
            self.code += condition.strip()
        else:
            raise Exception("Can't add 'and' outside if-elif-else statement")

    def or_(self, condition: str = ''):
        if self.statement:
            self.code += ' or '
            self.code += condition.strip()
        else:
            raise Exception("Can't add 'and' outside if-elif-else statement")

    def level_up(self) -> int:
        self.level += 1
        return self.level

    def level_down(self) -> int:
        if self.level > 0:
            self.level -= 1
            return self.level
        else:
            raise Exception("It is not possible to set the level less than 0")

    def set_level(self, level: int):
        if level >= 0:
            self.level = level
        else:
            raise Exception("It is not possible to set the level less than 0")

    def current_level(self) -> int:
        return self.level



