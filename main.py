class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    x = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    text = '[]()()()'
    if len(text) % 2 != 0:
        print('Несбалансированная последовательность')
    else:
        for item in text:
            flag = False
            if item in x.keys():
                stack.push(item)
            else:
                if stack.isEmpty() is False:
                    if item == x[stack.peek()]:
                        stack.pop()
                    else:
                        print('Несбалансированная последовательность')
                        break
                else:
                    print('Несбалансированная последовательность')
                    flag = True
                    break
        if stack.isEmpty() and not flag:
            print('Сбалансированная последовательность')
