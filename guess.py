import random as rd

MIN_NUMBER = 1
MAX_NUMBER = 100


class SecretNumber:
    '''
    This is a random number from 1 to 100 inclusively.
    You can compare an object of this class with other numbers using < or >.
    The object will preserve the amount of attempts (comparisons).
    '''

    def __init__(self):
        self.__secret = rd.randint(MIN_NUMBER, MAX_NUMBER)
        self.__attempts = 0

    @property
    def attempts(self):
        return self.__attempts

    def __gt__(self, number):
        self.__attempts += 1
        return self.__secret > number

    def __lt__(self, number):
        self.__attempts += 1
        return self.__secret < number


def binary_search(secret):
    '''
    This function returns the number of attempts
    to guess a Secret Number secret.

    The binary search method is used here.
    '''

    left, right = MIN_NUMBER, MAX_NUMBER

    while left < right:
        middle = (left+right) // 2
        if secret > middle:
            left = middle + 1
        else:
            right = middle

    return secret.attempts


if __name__ == "__main__":
    # RUN
    attepts_list = [binary_search(SecretNumber()) for i in range(1000)]
    print(
        'A mean number of attempts through 1000 games is',
        sum(attepts_list) / len(attepts_list)
        )
