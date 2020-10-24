score = []
for i in range(20):
    score.append(int(input("Enter score: ")))
    a = score[i]
    if a > 10 or a < 0:
        print("Score is out of range.")
        quit()

print("Original list:")
print(score)

for i in range(11):
    print(i, "*"*score.count(i))
