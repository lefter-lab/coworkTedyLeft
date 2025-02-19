import yt_dlp
import openai
from itertools import permutations
import sys

def generate_combinations():
    while True:
        # Въведете броя на буквите
        num_letters = int(input("Въведете броя на буквите: "))

        # Въведете самите букви
        letters = input(f"Въведете {num_letters} букви, разделени с интервал: ").split()

        # Въведете дължината на генерираните думи
        word_length = int(input("Въведете дължината на генерираните думи: "))

        # Генериране на всички уникални комбинации
        combinations = set(permutations(letters, word_length))

        # Превръщане на комбинациите в списък и сортиране по азбучен ред
        combination_list = sorted(["".join(combo) for combo in combinations])

        # Изпълнение на цикъл за печат на 5 думи на ред
        total_combinations = len(combination_list)
        print(f"\nОбщо комбинации: {total_combinations}")
        for i, combo in enumerate(combination_list, 1):
            print(f"{i}. {combo}")
            if (i % 5 == 0) and (i != total_combinations):
                next_action = input("Натиснете Enter за следващата страница или Esc за изход. Натиснете 'ь' за нов брой букви: ")
                if next_action == '\x1b':  # '\x1b' е ASCII код за Escape
                    print("Програмата е прекратена.")
                    sys.exit()
                elif next_action == 'ь':
                    break
        else:
            continue
        break

if __name__ == "__main__":
    generate_combinations()
