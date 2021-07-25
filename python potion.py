import random
health=50
difficulty=int(input("ENTER THE LEVEL OF DIFFICULTY"))
potion_health=int(random.randint(25,50)/difficulty)
health=potion_health+health
print(health)
