with open(r"Inputs\2015 Day 1 - Not Quite Lisp.txt", "r") as f:
    parentheses = f.read()

ans = 0

for index, char in enumerate(parentheses):
    if ans == -1:
        print(index)
        break
    
    ans += 1 if char == '(' else -1

