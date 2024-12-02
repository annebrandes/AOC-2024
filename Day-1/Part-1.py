file = open("../Day-1/Day-1.txt","r")

sum = 0
first_list = []
second_list = []

for line in file:
    first_list.append(line[0:5])
    second_list.append(line[8:13])

first_list.sort()
second_list.sort()

i = 0
for i, num in enumerate(first_list):
    sum += abs(int(first_list[i]) - int(second_list[i]))
    i += 1

print("calculated sum", sum)
