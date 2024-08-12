from urllib import request
from random import randint


def get_word_list() -> list[str]:
    data = request.urlopen(
        'https://gist.githubusercontent.com/shmookey/b28e342e1b1756c4700f42f17102c2ff/raw/ed4c33a168027aa1e448c579c8383fe20a3a6225/WORDS'
    )

    word_list = []

    for word in data:
        new_word = str(word.strip())
        new_word = new_word.removeprefix('b')
        new_word = new_word.replace("'", "")
        word_list.append(new_word)

    return word_list


def pick_random_word(word_list=None) -> str:
    if word_list is None:
        word_list = get_word_list()
    index = randint(0, len(word_list) - 1)

    return word_list[index]