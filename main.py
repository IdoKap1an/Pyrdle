import word_manager
from colorama import Back
import time
import os


def wordle():
    word_list = word_manager.get_word_list()
    # print(word_list)

    chosen_word = word_manager.pick_random_word(word_list)
    # print(chosen_word)

    list_of_colored_letters_lists = []

    for attempt in range(1, 6+1):
        os.system("cls")
        print(f"Attempt {attempt}/6\n")

        for i in range(len(list_of_colored_letters_lists)):
            for letter in list_of_colored_letters_lists[i]:
                print(letter, end="")
            print()

        time.sleep(1)

        # Validating Input
        user = ""
        while len(user) != 5 or user not in word_list:
            user = input("Enter a valid word: ").lower()

        print()

        # Correct - Return
        if user == chosen_word:
            print(f"Great job! The word was indeed {chosen_word}")
            return

        # Wrong - Continue
        else:

            index_dict = {}
            correct_indexes = []

            # Check for CORRECT and NOT_IN_WORD indexes
            for index in range(5):

                find_index = chosen_word.find(user[index], )

                if find_index == index or user[index] == chosen_word[index]:
                    index_dict[index] = index
                    correct_indexes.append(index)

                else:
                    if find_index != -1:
                        index_dict[index] = find_index
                        continue
                    index_dict[index] = -1

            # print(index_dict)

            # Add the correct colors
            colored_letter_list = []

            for i in range(5):
                # Letter is correct
                if index_dict[i] == i:
                    colored_letter_list.append(f'{Back.GREEN}{user[i]}')
                    continue

                # Letter might be in word
                for j in range(5):
                    # Letter is in word

                    if index_dict[i] == j:
                        # If letter was already used
                        if j not in correct_indexes:
                            correct_indexes.append(j)
                            colored_letter_list.append(f'{Back.YELLOW}{user[i]}')
                            break
                        else:
                            colored_letter_list.append(f'{Back.RESET}{user[i]}')


                # Letter is incorrect
                if index_dict[i] == -1:
                    colored_letter_list.append(f'{Back.RESET}{user[i]}')


            colored_letter_list.append(Back.RESET)

            # Print the colors
            for letter in colored_letter_list:
                print(letter, end="")

            list_of_colored_letters_lists.append(colored_letter_list)
            print()

        print()

    # Didn't guess the correct word
    print(f"The word was {chosen_word}, Yikes!")


if __name__ == '__main__':
    while True:
        os.system("pause")
        os.system("cls")
        wordle()
