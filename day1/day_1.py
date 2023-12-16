# Lesson learned on this one:
# Take the time to learn regex, especially around pattern matching

# New thing used : the overlapped flag

# Due to the numbers being able to overlap, using a forloop or trying to come up with a clever way to replace them took an hour just to be wrong
# with the findall combined with overlap, it took less than 5 minutes.

sum = 0

num_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

import regex as re

with open("day_1_input.txt", "r") as f:
    for line in f:
        line = line.strip()

        number = 0
        matching_numbers = re.findall(
            "\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True
        )

        for x, num in enumerate(matching_numbers):
            if num in num_words:
                matching_numbers[x] = num_words[num]

        number = int(matching_numbers[0] + matching_numbers[-1])
        sum += number

print(sum)
