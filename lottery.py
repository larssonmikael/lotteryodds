import random
from collections import Counter

lottery_numbers = [1, 2, 3, 4, 5]
star_numbers = [1, 2, 3, 4]
jackpot = 482000000


def init():
    print(f"\n    We're gonna check the magnitude of out hopium-levels and whether we're lucky enough to win big"
          f" gambling at the Euro-jackpot.")
    print(f"    As of 2022/01/15, the Jackpot pays"
          f" {jackpot} SEK. \n    We pay 18.8 SEK each per drawing. "
          f"\n    Our numbers are {lottery_numbers} + {star_numbers} \n\n    We ride at dawn, bitches \n"
          f"    ________________________")


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


def insertion_sort(drawing):
    for i in range(1, len(drawing)):
        key = drawing[i]
        j = i - 1
        while j >= 0 and key < drawing[j]:
            drawing[j + 1] = drawing[j]
            j = j - 1
        drawing[j + 1] = key


def cost_per_person(iterations):
    # cost = ((iterations * 125) / 5)
    cost = ((iterations * 94) / 5)
    return cost


def payout(iterations):
    # payout_per_sek = (winnings / iterations)
    payout_per_sek = (iterations / 8)
    return payout_per_sek


def feeling_lucky(iterations, attempts):
    winnings = 0
    drawing = []
    star_drawing = []

    while drawing != lottery_numbers:
        if len(drawing) == len(lottery_numbers):
            iterations += 1
            drawing.clear()
        while len(drawing) != len(lottery_numbers):
            number = random.randint(1, 50)
            drawing += [number]
            insertion_sort(drawing)
            counts = dict(Counter(drawing))
            duplicates = {key: value for key, value in counts.items() if value > 1}
            if duplicates:
                drawing.remove(number)
            if drawing == lottery_numbers:
                winnings = winnings + payout(iterations) - cost_per_person(iterations)
                # print(f"\nWe got 5/5 after {iterations} attempts.\nBefore we clocked this win, we spent "
                #       f"{cost_per_person(iterations)} SEK per person.\n"
                #       f"This means our individual net gain is {payout(iterations)} SEK "
                #       f"and we've been going for {iterations} weeks or {iterations/52} years.\n"
                #       f"Net gains: {winnings} SEK"
                #       f"\n--------------------------------------------------")

                counts.clear()
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
                    for var in star_numbers:
                        if len(star_drawing) <= 4:
                            if star_drawing.__contains__(var):
                                star_drawing.remove(var)
                            if len(star_drawing) == 2:
                                winnings = jackpot - cost_per_person(iterations)
                                # winnings = winnings + (jackpot / 8) - cost_per_person(iterations)
                                payout(iterations)
                                print(
                                    f"\nWe have been individually coughing up {cost_per_person(iterations)} "
                                    f"SEK before we hit the jackpot at {jackpot}. \n"
                                    f"\nWe've been going for {iterations} weeks, or {iterations / 52} "
                                    f"years for that matter.")
                                print(f"\nHOWEVER. \n\nWe're splitting the god damn jackpot.\nEach individual net"
                                      f" {winnings / 8} SEK.\n\nHow the fuck about that?"
                                      f"\n--------------------------------------------------")
                                attempts.append(iterations)
                                break

                    else:
                        drawing.clear()
                        star_drawing.clear()


def main():
    init()
    iterations = 1
    attempts = []
    for i in range(0, 50):
        feeling_lucky(iterations, attempts)
        print(i + 1)
    print(f"\n{attempts}\n")
    cal_average(attempts)
    print(f"On average, it takes {cal_average(attempts)} attempts to win the Jackpot.\n")
    print(f"That's gonna cost you on average {cal_average(attempts) * 18.8}")

    print("Gambling is a tough game, don't you think?")


if __name__ == '__main__':
    main()
