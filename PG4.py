pokemon = float(input("Enter level pokemon: "))
pokeball = input("Enter level pokeball: ").lower()
distance = float(input("Enter distance: "))

if pokeball == "h":
    pokeball = 0.01

elif pokeball == "m":
    if 0 <= pokemon <= 40:
        pokeball = 0.03
    elif 41 <= pokemon <= 60:
        pokeball = 0.05
    elif 61 <= pokeball <= 100:
        pokeball = 0.08

elif pokeball == "l":
    if 0 <= pokemon <= 40:
        pokeball = 0.05
    elif 41 <= pokemon <= 60:
        pokeball = 0.03
    elif 61 <= pokeball <= 100:
        pokeball = 0.1

s = 100 - (pokemon * distance * pokeball)
if s < 0:
    s = 0.0
elif s > 100:
    s = 100
print("%.2f percent." % s)
