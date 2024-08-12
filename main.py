import word_manager

word_list = word_manager.get_word_list()


def wordle():
    chosen_word = word_manager.pick_random_word(word_list)

    for attempt in range(6):
        print(chosen_word)


if __name__ == '__main__':
    wordle()
