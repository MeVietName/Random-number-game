import random


random_number = random.randint(1,100)
print(random_number)
chance = 10
print("Vous avez 10 chance pour trouver le nombre choisi par l'ordinateur")


for i in range (1,10):
    nombre=int(input("Donnez un nombre : "))


    if nombre == random_number:
        print("Correct vous avez trouve le nombre choisi par l'ordinateur")
        break


    if nombre != random_number:


        print(f"Rater vous avez maintenant {chance-1}")
        break


    if chance==0:
        print("Perdu vous avez utilise toutes vos chances")
        break




print(f"Rater vous avez maintenant {chance-1}")