with open(r"Inputs\2015 Day 1 - Not Quite Lisp.txt", "r") as f:
    parentheses = f.read()

ans = 0

for char in parentheses:
    ans += 1 if char == '(' else -1

print(ans)