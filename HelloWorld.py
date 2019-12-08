print('Hello aaaaa!')

a = 4+7
print(a)

players = [29, 58, 66, 71, 87]
print(players[2])

players.append(120)
print(players)

players[:2] = [0, 0]
print(players)

#players[:2] = []

print(players)

age = 17

if age < 21:
    print("Cant drink alcohol")


name = "Lucy"

if name is "Alex":
    print("Hi Alex")
elif name is "Lucy":
    print("Hello Lucy")
else:
    print("Hi no name")
