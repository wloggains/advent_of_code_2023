from pprint import pprint


def part1():
    with open("day4input.txt") as f:
        lines = [l.strip() for l in f.readlines()]


    ## get card
    sum = 0
    for card in lines:
        card_number, numbers = card.split(":")
        winning_numbers, got_numbers = numbers.split("|")
        print(winning_numbers)
        winning_numbers = [w for w in winning_numbers.strip().split(" ") if w != '']
        print(winning_numbers)

        print(got_numbers)
        got_numbers = [g for g in got_numbers.strip().split(" ") if g != '']

        print(got_numbers)
        score = 0
        for n in got_numbers:
            if n in winning_numbers:
                print(f"{n} is in both.")
                score += 1

        print(score)
        total_score = pow(2, score-1) if score > 0 else 0
        print(total_score)
        sum += total_score

    return sum


def part2():
    with open("day4input.txt") as f:
        lines = [l.strip() for l in f.readlines()]


    sum = 0
    card_scores = {}
    for card in lines:
        card_number, numbers = card.split(":")
        card_number = card_number.split(" ", 1)[1].strip()

        winning_numbers, got_numbers = numbers.split("|")
        winning_numbers = [w for w in winning_numbers.strip().split(" ") if w != '']
        got_numbers = [g for g in got_numbers.strip().split(" ") if g != '']
        score = 0
        for n in got_numbers:
            if n in winning_numbers:
                score += 1

        card_scores[card_number] = {"score" : score, "count": 1}

    total = 0

    for num, card in card_scores.items():
        score = card['score']
        num = int(num)
        count = card['count']
        for i in range(1, score+1):
            card_scores[str(num+i)]['count'] += count
            print(f"Add {count} to {str(num+i)}")

    for key, card in card_scores.items():
        total += card['count']
    return total



if __name__ == "__main__":
    print(part2())