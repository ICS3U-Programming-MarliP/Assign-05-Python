#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 28, 2023
# This program asks the user for a number correlating
# to a farm animal then using a function, finds and displays
# the sound said animal makes.


def farm_animal_sound(user_animal):
    match user_animal:
        case 1:
            animal_sound = "Oink"
        case 2:
            animal_sound = "Neigh"
        case 3:
            animal_sound = "Baa"
        case 4:
            animal_sound = "Cluck"
        case 5:
            animal_sound = "Cockledoodledoo"
        case 6:
            animal_sound = "Bleat"
        case 7:
            animal_sound = "Moo"
        case 8:
            animal_sound = "Hee haw"
        case 9:
            animal_sound = "Woof"
        case 10:
            animal_sound = "Meow"

    return animal_sound


def main():
    print(
        "Hello! Welcome to the farm animal sound program! You will be asked to input a number correlation with a farm animal and the program will output the sound it makes. Below is the list of animals.\n\nPig - 1\nHorse - 2\nSheep - 3\nChicken - 4\nRooster - 5\nGoat - 6\nCow - 7\nDonkey - 8\nDog - 9\nCat - 10\n"
    )

    while True:
        user_animal_str = str(input("Please enter the animal number here: "))

        try:
            user_animal = int(user_animal_str)
            if user_animal < 1 or user_animal > 10:
                print("\nPlease enter a number corresponding to a farm animal.\n")
            else:
                animal_sound = farm_animal_sound(user_animal)
                print("\n{}!".format(animal_sound))
                break
        except:
            print("\nPlease enter a number corresponding to a farm animal.\n")


if __name__ == "__main__":
    main()
