import random
import requests
import time


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/"
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience'],
    }


def random_anime():
    possible_ids = [5114, 43608, 28977, 9253, 38524, 9969, 15417, 11061, 42938, 34096, 35180, 918, 4181, 2904, 35247,
                    37491, 47778, 19, 40028, 48583, 36838, 40682, 50265, 32935, 50160, 17074, 41084, 33095, 1, 263,
                    1575, 21939, 2921, 48569, 37521, 46102, 45576, 24701, 28891, 11665, 40591, 5258, 23273, 21, 33352,
                    457, 34599, 40748, 245, ]
    anime_id = random.choice(possible_ids)
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/"
    response = requests.get(url)
    anime = response.json()

    return {
      'title': anime['data']['title_english'],
      'year': anime['data']['year'],
      'rank': anime['data']['rank'],
      'no. episodes': anime['data']['episodes'],
    }


def random_planet():
    planet_id = random.randint(1, 60)
    url = f"https://swapi.dev/api/planets/{planet_id}/"
    response = requests.get(url)
    planet = response.json()

    return {
        'name': planet['name'],
        'diameter': planet['diameter'],
        'population': planet['population'],
        'orbital_period': planet['orbital_period']
    }


def pokemon():
    game = int(input("How many rounds would you like to play? ")) # Player chooses the number of rounds to play
    player_score = 0
    computer_score = 0
    while game > 0:
        player_poke1 = random_pokemon()  # Generates 3 random pokemon for the player to choose from
        player_poke2 = random_pokemon()
        player_poke3 = random_pokemon()
        player_choice = int(input(f"Which Pokemon would you like to choose? \n 1: {player_poke1} \n 2: {player_poke2}"
                                  f" \n 3: {player_poke3}? "))
        possible_choices = [1, 2, 3]
        if player_choice not in possible_choices:  # Checks whether choice is inputted correctly
            print("Uh oh, you must choose 1, 2 or 3")
            break
        else:
            if player_choice == 1:
                player_poke = player_poke1
                print(f"You chose {player_poke}")
            elif player_choice == 2:
                player_poke = player_poke2
                print(f"You chose {player_poke}")
            elif player_choice == 3:
                player_poke = player_poke3
                print(f"You chose {player_poke}")
        computer_poke = random_pokemon()
        possible_stats = ["weight", "height", "experience"]
        if game % 2 == 0:  # for even rounds the computer chooses a random stat to play
            stat = random.choice(possible_stats)
            print(f"The computer chose to play {stat}")
        else:  # for odd rounds the player chooses the stat to play
            stat = str(input("Which stat would you like to use, height, weight or experience? ")).lower()
            if stat not in possible_stats:  # Checks whether stat is inputted correctly
                print("Uh oh, you must chose height, weight or experience.")
                break
        player_num = player_poke[stat]
        computer_num = computer_poke[stat]
        if player_num > computer_num:
            print("Yay, you win!")
            player_score += 1
            game = game - 1  # keeps track of number of rounds played
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
        elif player_num < computer_num:
            print("Sorry, you lose :(")
            print(f"The computer's pokemon was: {computer_poke}")
            computer_score += 1
            game = game - 1
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
        else:
            print("You draw!")
            print(f"The computer's pokemon was: {computer_poke}")
            game = game - 1
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
    if game == 0:  # Triggered after 5 rounds of play
        if player_score > computer_score:
            print(f"Game over. Congratulations, you beat the computer! Your score was {player_score}, "
                  f"the computer only scored {computer_score}!")
            y_n = input("Would you like to save your score, y/n?").lower()
            if y_n == "y":
                save_scores()
        elif computer_score > player_score:
            print(f" Game over. Uh oh, you got beaten by a computer. The computer scored {computer_score}, "
                  f"and you only got {player_score} :(")
        elif player_score == computer_score:
            print("Game over, It's a draw!")


def star_wars():
    game = int(input("How many rounds would you like to play? ")) # Player chooses the number of rounds to play
    player_score = 0
    computer_score = 0
    while game > 0:
        player_planet1 = random_planet()  # Generates 3 random planets for the player to choose from
        player_planet2 = random_planet()
        player_planet3 = random_planet()
        player_choice = int(input(f"Which Star Wars planet would you like to choose? \n 1: {player_planet1} \n "
                                  f"2: {player_planet2} \n 3: {player_planet3}? "))
        possible_choices = [1, 2, 3]
        if player_choice not in possible_choices:  # Checks whether choice is inputted correctly
            print("Uh oh, you must choose 1, 2 or 3")
            break
        else:
            if player_choice == 1:
                player_planet = player_planet1
                print(f"You chose {player_planet}")
            elif player_choice == 2:
                player_planet = player_planet2
                print(f"You chose {player_planet}")
            elif player_choice == 3:
                player_planet = player_planet3
                print(f"You chose {player_planet}")
        computer_planet = random_planet()
        possible_stats = ["diameter", "population", "orbital_period"]
        if game % 2 == 0:  # for even rounds the computer chooses a random stat to play
            stat = random.choice(possible_stats)
            print(f"The computer chose to play {stat}")
        else:  # for odd rounds the player chooses the stat to play
            stat = str(input("Which stat would you like to play, diameter, population, or orbital_period? ")).lower()
            if stat not in possible_stats:  # Checks whether stat is inputted correctly
                print("Uh oh, you must chose height, weight or experience.")
                break
        player_num = player_planet[stat]
        computer_num = computer_planet[stat]
        if player_num == "unknown":
            print("Unfortunately, that stat is unknown, new planets to explore coming up :)")
        elif player_num > computer_num:
            print("Yay, you win!")
            player_score += 1
            game = game - 1  # keeps track of number of rounds played
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
        elif player_num < computer_num:
            print("Sorry, you lose :(")
            print(f"The computer's pokemon was: {computer_planet}")
            computer_score += 1
            game = game - 1
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
        else:
            print("You draw!")
            print(f"The computer's pokemon was: {computer_planet}")
            game = game - 1
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
    if game == 0:  # Triggered after 5 rounds of play
        if player_score > computer_score:
            print(f"Game over. Congratulations, you beat the computer! Your score was {player_score}, "
                  f"the computer only scored {computer_score}!")
            y_n = input("Would you like to save your score, y/n? ").lower()
            if y_n == "y":
                save_scores()
        elif computer_score > player_score:
            print(f" Game over. Uh oh, you got beaten by a computer. The computer scored {computer_score}, "
                  f"and you only got {player_score} :(")
        elif player_score == computer_score:
            print("Game over, It's a draw!")


def anime():
    game = int(input("How many rounds would you like to play? ")) # Player chooses the number of rounds to play
    player_score = 0
    computer_score = 0
    while game > 0:
        player_anime1 = random_anime()  # Generates 3 random anime series for the player to choose from
        time.sleep(1) # Have to wait to call the API again because it limits calls per second
        player_anime2 = random_anime()
        time.sleep(2)
        player_anime3 = random_anime()
        player_choice = int(input(f"Which anime would you like to choose? \n 1: {player_anime1} \n "
                                  f"2: {player_anime2} \n 3: {player_anime3}? "))
        possible_choices = [1, 2, 3]
        if player_choice not in possible_choices:  # Checks whether choice is inputted correctly
            print("Uh oh, you must choose 1, 2 or 3")
            break
        else:
            if player_choice == 1:
                player_anime = player_anime1
                print(f"You chose {player_anime}")
            elif player_choice == 2:
                player_anime = player_anime2
                print(f"You chose {player_anime}")
            elif player_choice == 3:
                player_anime = player_anime3
                print(f"You chose {player_anime}")
        time.sleep(1)
        computer_anime = random_anime()
        possible_stats = ["year", "rank", "no. episodes"]
        if game % 2 == 0:  # for even rounds the computer chooses a random stat to play
            stat = random.choice(possible_stats)
            print(f"The computer chose to play {stat}")
        else:  # for odd rounds the player chooses the stat to play
            stat = str(input("Which stat would you like to choose, year, rank, or no. episodes? ")).lower()
            if stat not in possible_stats:  # Checks whether stat is inputted correctly
                print("Uh oh, you must chose height, weight or experience.")
                break
        player_num = player_anime[stat]
        computer_num = computer_anime[stat]
        if player_num > computer_num:
            print("Yay, you win!")
            player_score += 1
            game = game - 1  # keeps track of number of rounds played
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
        elif player_num < computer_num:
            print("Sorry, you lose :(")
            print(f"The computer's pokemon was: {computer_anime}")
            computer_score += 1
            game = game - 1
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
        else:
            print("You draw!")
            print(f"The computer's pokemon was: {computer_anime}")
            game = game - 1
            print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                  f"more round(s) to play.")
    if game == 0:  # Triggered after 5 rounds of play
        if player_score > computer_score:
            print(f"Game over. Congratulations, you beat the computer! Your score was {player_score}, "
                  f"the computer only scored {computer_score}!")
            y_n = input("Would you like to save your score, y/n? ").lower()
            if y_n == "y":
                save_scores()
        elif computer_score > player_score:
            print(f" Game over. Uh oh, you got beaten by a computer. The computer scored {computer_score}, "
                  f"and you only got {player_score} :(")
        elif player_score == computer_score:
            print("Game over, It's a draw!")


def save_scores():
    save_name = input('What is your name? ').title()
    save_score = str(input('What is your score? (BE HONEST!) '))
    text_file = open("highscores.txt", "a")
    text_file.write(str(save_name) + ' has a score of ' + str(save_score) + "\n")
    text_file.close()
    print("\n")
    text_file = open("highscores.txt", "r")
    whole_thing = text_file.read()
    print(whole_thing)
    text_file.close()


def run():
    game_choice = input("Welcome to Top Trumps! Can you beat the computer? \n"
                        "Would you like to play Pokemon Top Trumps, Star Wars "
                        "Planets Top Trumps, or Popular Anime Top Trumps? ").lower()
    choices = ["pokemon", "star wars planets", "popular anime"]
    if game_choice not in choices:
        print("You must choose 'pokemon', 'star wars planets', or 'popular anime'.")
    elif game_choice == 'pokemon':
        pokemon()
    elif game_choice == 'star wars planets':
        star_wars()
    elif game_choice == 'popular anime':
        anime()


run()