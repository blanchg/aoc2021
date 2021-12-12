import os
import math

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)
total = 0

for line in lines:
    stack = []
    for c in line:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                total += 3
                break
        elif c == '[':
            stack.append(c)
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                total += 57
                break
        elif c == '{':
            stack.append(c)
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                total += 1197
                break
        elif c == '<':
            stack.append(c)
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                total += 25137
                break
print(total)

scores = []
for line in lines:
    total = 0
    stack = []
    for c in line:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack = []
                break
        elif c == '[':
            stack.append(c)
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack = []
                break
        elif c == '{':
            stack.append(c)
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                stack = []
                break
        elif c == '<':
            stack.append(c)
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                stack = []
                break
    if not stack:
        continue
    points = [' ', '(', '[', '{', '<']
    stack = list(reversed(stack))
    for c in stack:
        total = total * 5 + points.index(c)
    print("".join(stack), total)

    scores.append(total)

print(sorted(scores)[math.floor(len(scores) / 2)])