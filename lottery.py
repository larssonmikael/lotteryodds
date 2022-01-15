import random
from collections import Counter


def insertion_sort(drawing):
    for i in range(1, len(drawing)):
        key = drawing[i]
        j = i - 1
        while j >= 0 and key < drawing[j]:
            drawing[j + 1] = drawing[j]
            j = j - 1
        drawing[j + 1] = key


def cost_per_person(iterations):
    cost = ((iterations * 94) / 5)
    print(f"This means we're paying {cost} per week per person")
    return cost


def payout(iterations):
    payout_per_sek = (3492377 / iterations)
    print(f"This also means that for each SEK we spent, we've won {payout_per_sek} SEK.")
    return payout_per_sek


def feeling_lucky(iterations):
    lottery_numbers = [1, 2, 3, 4, 5]
    star_numbers = [1, 2, 3, 4]
    drawing = []
    star_drawing = []
    while drawing != lottery_numbers:
        if len(drawing) == len(lottery_numbers):
            drawing.clear()
        while len(drawing) != len(lottery_numbers):
            number = random.randint(1, 50)
            drawing += [number]
            insertion_sort(drawing)
            counts = dict(Counter(drawing))
            duplicates = {key: value for key, value in counts.items() if value > 1}
            if duplicates:
                drawing.remove(number)
            if drawing != lottery_numbers:
                if len(drawing) == len(lottery_numbers):
                    iterations += 1
                # print(iterations)
            if drawing == lottery_numbers:
                print(f"We got 5/5 after {iterations} attempts. We spent {cost_per_person(iterations)} SEK. \n"
                      f"As of 2022/01/15, 5/5 pays out 3.492.377 SEK. \n"
                      f"This means out net gain is {payout(iterations)} SEK for the privilege."
                      f"")
                # feeling_extra_lucky(iterations)
                counts.clear()
                # drawing.clear()
                if star_drawing != star_numbers:
                    if len(star_drawing) == len(star_numbers):
                        star_drawing.clear()
                    while len(star_drawing) != len(star_numbers):
                        star_number = random.randint(1, 10)
                        star_drawing += [star_number]
                        insertion_sort(star_drawing)
                        counts = dict(Counter(star_drawing))
                        duplicates = {key: value for key, value in counts.items() if value > 1}
                        if duplicates:
                            star_drawing.remove(star_number)
                    if star_drawing == star_numbers:
                        print(
                            f"You hit the jackpot after {iterations} attempts. "
                            f"Since we're paying 94 SEK for five weeks,"
                            f"we are coughing up {(iterations * 94) / 5} SEK before we hit the jackpot. ")
                    else:
                        drawing.clear()
                        star_drawing.clear()

                    # feeling_lucky(iterations)


# def feeling_extra_lucky(iterations):
#     iterations = iterations
#     star_numbers = [1, 2, 3, 4]
#     star_drawing = []
#     while star_drawing != star_numbers:
#         if len(star_drawing) == len(star_numbers):
#             star_drawing.clear()
#         while len(star_drawing) != len(star_numbers):
#             number = random.randint(1, 10)
#             star_drawing += [number]
#             insertion_sort(star_drawing)
#             counts = dict(Counter(star_drawing))
#             duplicates = {key: value for key, value in counts.items() if value > 1}
#             if duplicates:
#                 star_drawing.remove(number)
#             if [star_drawing] != star_numbers:
#                 print(f"Sorry, no jackpot. So far you've tried {iterations} times.")
#                 feeling_lucky(iterations)
#             if star_drawing == star_numbers:
#                 print(f"You hit the jackpot after {iterations} tries. Since we're paying 94 SEK for five weeks,"
#                       f"we are coughing up {(iterations * 94) / 5} SEK before we hit the jackpot. ")


# def feeling_extra_lucky(iterations):
#     print("END")
#     iterations = iterations
#     star_numbers = [1, 4]
#     star_drawing = []
#     while star_drawing != star_numbers:
#         iterations += 1
#         print(iterations)
#         star_drawing.clear()
#         for i in range(0, 2):
#             number = random.randint(1, 10)
#             star_drawing += [number]
#             insertion_sort(star_drawing)
#     else:
#         print("You hit the jackpot!")
#         print(iterations)


def main():
    # for i in range(0, 5):
    iterations = 0
    feeling_lucky(iterations)


if __name__ == '__main__':
    main()

# if len(drawing) >> len(lottery_numbers):
#     drawing.pop()
#     print("do i evet get in here?")
# if len(drawing) >> 5:
#     print("Am i here?")
#     drawing.remove(len(drawing))
