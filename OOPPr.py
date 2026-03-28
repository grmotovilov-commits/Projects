class Stack:
    def __init__(self, word):
        self.array = list(word)
        self.check = list("{([])}")
    def delete(self):
        main = []
        i = 0
        temp = set(self.check)
        for i in self.array:
            if i not in temp:
                continue
            else:
                main.append(i)
        return main
    def result(self):
        main = self.delete()
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in main:
            if char not in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if pairs[char] != last:
                    return False
        return len(stack) == 0



ex = Stack("ab{cd(ef[ghj)}")
print(ex.result())
oi = Stack("ab(cd{ef[gh]j})")
print(oi.result())
