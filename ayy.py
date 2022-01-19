import random
random_number = random.randint(1,101)

player_number = int(input("Choose a number between 1 to 100: "))

while player_number != random_number:
    if player_number < random_number:
        print("You are far from the number. Add more numbers to it.")
        player_number = int(input("Choose a number again:"))

    if player_number > random_number:
        print("You are far again. Reduce numbers to it.")
        player_number = int(input("Choose a nuber again: "))
    
    if player_number == random_number:
        print("You got the number!")

else:
    print("You got the number!")
