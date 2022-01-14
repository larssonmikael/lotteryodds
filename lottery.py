import random
from collections import Counter


def insertion_sort(drawing):
    for i in range(1, len(drawing)):
        key = drawing[i]
        j = i - 1

        while j >= 0 and key < drawing[j]:
            drawing[j + 1] = drawing[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        drawing[j + 1] = key


def feeling_lucky():
    iterations = 1
    lottery_numbers = [1, 2, 3, 4, 5]
    drawing = []
    while drawing != lottery_numbers:
        if len(drawing) == len(lottery_numbers):
            drawing.clear()
        while len(drawing) != len(lottery_numbers):
            while len(drawing) != len(lottery_numbers):
                # if drawing is not []:
                if len(drawing) >> len(lottery_numbers):
                    drawing.pop()
                if len(drawing) >> 5:
                    drawing.remove(len(drawing))
                number = random.randint(1, 50)
                drawing += [number]
                insertion_sort(drawing)
                counts = dict(Counter(drawing))
                duplicates = {key: value for key, value in counts.items() if value > 1}
                if duplicates:
                    drawing.remove(number)
                if drawing != lottery_numbers:
                    iterations += 1
                    # print(iterations)
            if drawing == lottery_numbers:
                print(f"You got 5/5 after {iterations} tries")
                return iterations
                # feeling_extra_lucky()



def feeling_extra_lucky():
    print("END")
    iterations = 1
    star_numbers = [1, 10]
    drawing = []
    while drawing != star_numbers:
        iterations += 1
        print(iterations)
        drawing.clear()
        for i in range(0, 2):
            number = random.randint(1, 10)
            drawing += [number]
            insertion_sort(drawing)
    else:
        print("You hit the jackpot!")
        print(iterations)


def main():
    for i in range(0, 5):
        feeling_lucky()







if __name__ == '__main__':
    main()
