import random
def main():
    game()


def game():
    user_input = int(input("1, 2, or 3?\n"))
    # 1  = rock
    # 2 = paper
    # 3 = scissors
    comp_input = random.randint(1, 3)

    if user_input == 1 and comp_input == 2 or user_input == 2 and comp_input == 3 or user_input == 3 and comp_input == 1:
        print(comp_input)
        print("Comp wins")
    elif user_input == 2 and comp_input == 1 or user_input == 3 and comp_input == 2 or user_input == 1 and comp_input == 3:
        print(comp_input)
        print("User wins")
    else:
        print("Tie!")

if __name__ == '__main__':
    main()