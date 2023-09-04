hash_map = {
            "(":")",
            "[":"]",
            "{":"}",
        }

s = "([{()}])"

class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.start = -1
        self.top = -1
    
    def push(self, value):
        if self.isEmpty():
            self.start = 0
            self.top = 0
            self.stack.append(value) 
        
        else:
            self.top += 1
            self.stack.append(value) 
    
    def peek(self):
        element = self.stack[self.top]
        return element

    def pop(self):
        if self.isEmpty():
            return False
        else:
            self.top -= 1
            return self.stack.pop()
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def __str__(self) -> str:
        values = [str(x) for x in self.stack]
        
        return " ".join(values)
        
s1 = Stack()
i = 0
valid = True

while i < len(s):
    if s[i] == "(" or s[i] == "[" or s[i] == "{":
        s1.push(s[i])
    else:
        last_bracket = s1.peek()
        if s[i] == hash_map[last_bracket]:
            s1.pop()
        else:
            valid = False
            break
        
    
    i += 1


print(valid)