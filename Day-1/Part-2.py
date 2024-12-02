file = open("../Day-1/Day-1.txt","r")

sum = 0
first_list = []
second_list = {}

for line in file:
    first_list.append(line[0:5])
    if line[8:13] in second_list: 
        second_list[line[8:13]] += 1
    else: 
        second_list.update({line[8:13]: 1})

i = 0
for i, num in enumerate(first_list):
    if second_list.get(first_list[i]) == None:
        continue
    sum += abs(int(first_list[i]) * int(second_list.get(first_list[i])))
    i += 1

print("calculated sum", sum)
