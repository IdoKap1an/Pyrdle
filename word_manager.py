import requests
from random import randint


def get_word_list() -> list[str]:
    data = requests.get(
        "https://gist.githubusercontent.com/shmookey/b28e342e1b1756c4700f42f17102c2ff/raw/ed4c33a168027aa1e448c579c8383fe20a3a6225/WORDS")

    text = data.text.splitlines()

    return text


def pick_random_word(word_list=None) -> str:
    if word_list is None:
        word_list = get_word_list()
    index = randint(0, len(word_list) - 1)

    return word_list[index]
