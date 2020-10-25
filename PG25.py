damage = int(input())
zombies = [x for x in (map(int, input().split()))]
result = [0]
i = 0
while True:
    c = zombies[i] // damage
    d = zombies[i] % damage
    if d == 0:
        result.append(c)
    elif c == 0 or zombies[i] == damage:
        result.append(1)
    else:
        result.append(c+1)
    if i == len(zombies)-1:
        break
    i += 1
result.remove(0)

for i in range(len(result)-1):
    stack = result[i+1] + result[i]
    result[i+1] = stack

print(result[-1])
print(" ".join(list(map(str, result))))
