word = input()
num = int(input())

if num > len(word):
    num = num % len(word)

if num > 0:
    print(word[-num::] + word[0:len(word) - num])

elif num < 0:
    print(word[-num::] + word[0:-num])

else:
    print(word)