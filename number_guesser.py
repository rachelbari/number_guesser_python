import random

if __name__=="__main__":
    random_number = random.randint(1,101)
    is_guessed = False
    while is_guessed is False:
        guessed_number_string = input("Guess a number between 1 and 100: ")
        guessed_number_int = int(guessed_number_string)
        if guessed_number_int is random_number:
            print("correct! the number is: {}".format(random_number))
            break
        elif guessed_number_int > random_number:
            print("your guess is too high")
        else:
            print("your guess is too low")
