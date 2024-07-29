import random
import string


def generate_random_word(length=6):
    # Define the characters to be used in the random word
    characters = (
        string.ascii_letters + string.digits
    )  # You can add more characters if you want

    # Generate a random word of the specified length
    random_word = "".join(random.choice(characters) for _ in range(length))
    print(random_word)
    return random_word


