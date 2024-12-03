import re

file = open("../Day-3/Day-3.txt","r")
content = file.read()
p1 = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(p1, content)

total = 0
p2 = r'mul\((\d+),(\d+)'
for pair in matches:
    match = re.search(p2, pair)
    num1 = int(match.group(1))
    num2 = int(match.group(2))
    total += num1 * num2

print(total)