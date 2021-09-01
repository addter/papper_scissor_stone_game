import random
chance = 10
your_point = 0
cpu_point = 0
no_of_chance = 0
number = ["p","s","st"]

print("paper,scissor,stone game")
print("you will only get 10 chances")
print("enter paper for p, scissor for s and stone for st")

while no_of_chance<chance:
    inpu = input()
    inp = inpu.lower()
    com = random.choice(number)
    if inp == com:
        print("no one won and game has become tie")
        no_of_chance += 1
    elif inp == "p" and com == "s":
        print("cpu won")
        cpu_point += 1
        print(f" your point {your_point} and cpu point {cpu_point}")
        no_of_chance += 1
    elif inp == "p" and com == "st":
        print("you won")
        your_point += 1
        print(f" your point {your_point} and cpu point {cpu_point}")
        no_of_chance += 1
    elif inp == "s" and com == "p":
        print("you won")
        your_point += 1
        print(f" your point {your_point} and cpu point {cpu_point}")
        no_of_chance += 1
    elif inp == "s" and com == "st":
        print("cpu won")
        cpu_point += 1
        print(f" your point {your_point} and cpu point {cpu_point}")
        no_of_chance += 1
    elif inp == "st" and com == "p":
        print("cpu won")
        cpu_point += 1
        print(f" your point {your_point} and cpu point {cpu_point}")
        no_of_chance += 1
    else:
        print("you won")
        your_point += 1
        print(f" your point {your_point} and cpu point {cpu_point}")
        no_of_chance += 1
print("Game Over")
if your_point>cpu_point:
    print(f"you won and your point is {your_point} and cpu point is {cpu_point}")
elif cpu_point>your_point:
    print(f"cpu won and cpu point is {cpu_point} and your point is {your_point}")
else:
    print(f"game has became tie your point and cpu point are {your_point} and {cpu_point} respectively")
