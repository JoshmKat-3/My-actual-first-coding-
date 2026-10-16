scores = [85, 92, 78, 95, 88]

#print(scores[2])

#scores[0] = 100

#print(scores)

#for score in scores:
#    print(score)

total = 0
average = 0

for score in scores:
    total += score

average = total / len(scores)


print(average)    