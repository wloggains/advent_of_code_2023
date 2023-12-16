MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_input(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines


def parse_game(game):
    # get the number and the list of games from the string

    game_number, game_list = game.split(":")
    game_number = game_number.split(" ")[1]
    game_list = game_list.split(";")

    parsed_games = []
    for g in game_list:
        parsed_game = {}
        for entry in g.strip().split(","):
            entry = entry.strip()
            num, color = entry.split(" ")
            parsed_game[color] = int(num)
        parsed_games.append(parsed_game)

    return game_number, parsed_games


def get_possible_games(game_list):
    result = set()
    for game in game_list:
        game_number, parsed_games = parse_game(game)
        dq = False
        for g in parsed_games:
            if (
                g.get("red", 0) > MAX_RED
                or g.get("green", 0) > MAX_GREEN
                or g.get("blue", 0) > MAX_BLUE
            ):
                dq = True
        if not dq:
            result.add(int(game_number))

    return result


filename = "day_2_input.txt"


if __name__ == "__main__":
    games = get_input(filename)

    possible_games = get_possible_games(games)

    print(possible_games)
    print(sum(possible_games))
