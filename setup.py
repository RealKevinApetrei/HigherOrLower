# External Module Imports
import tkinter as tk # UI Module
import random # "Random" Module
from pathlib import Path # Path Module


# Developer Configuration #
range_decrease_rate = 5 # Range Decrease Rate per round (Default: 5)
starting_score = 0 # Starting Score (Default: 0)
number_range = 100 # Starting Number Range (Default: 100)
score_changer_range = 10 # +/-(1 - {score_changer_range}) per outcome. (Add/Remove Score)

build_version = "v2.00" # Current build version
# Developer Configuration


class Score: # Scoring System
    def __init__(self, score=starting_score): # Starting Score
        self.score = score

    def add_score(self): # Add Score (Winner Result)
        self.score += random.randint(1, score_changer_range) # +1-{config.score_changer_range} points

    def remove_score(self): # Remove Score (Loser Result)
        self.score -= random.randint(1, score_changer_range) # -1-{config.score_changer_range} points


def hilo_number(): # Random Number (1-{config.number_range})
    return random.randint(1, number_range)


def play(): # Play game (game_ui())
    menu.destroy() # Destroy Menu UI
    game_ui() # Run Game


# Pre-defined variables/objects
Player = Score() # Initialise Player Object (Score System)
number_picked = hilo_number() # Initialise Number Variable
previous_number_picked = 0 # Initialise Previous Number Variable (0)                                                          
build_version = build_version # Build Version (e.g. v1.0, v2.0-alpha)


def end_game(): # End game
    # Previous Score File (WRITE)
    previous_score_file = open("Data/previous_score.txt", "w") # Open Previous Score File
    previous_score_file.write(str(Player.score)) # Write game score
    previous_score_file.close() # Close file
    # Previous Score File (WRITE)

    # Total games played (READ/WRITE) (+1)
    games_played_file = open("Data/games_played.txt", "r") # Open Games Played File (READ)
    current_games_played = games_played_file.readline() # Read current games played
    games_played_file.close() # Close file

    games_played_file = open("Data/games_played.txt", "w") # Open Games Played File (WRITE)

    games_played_file.write(str(int(current_games_played) + 1)) # Write (+1) games played
    games_played_file.close() # Close file
    # Total games played (READ/WRITE) (+1)

    # High Score File (READ/WRITE) (SET NEW SCORE)
    high_score_file = open("Data/high_score.txt", "r") # Open High Score File (READ)
    current_high_score = high_score_file.readline() # Read current high score
    high_score_file.close() # Close file
    
    high_score_file = open("Data/high_score.txt", "w") # Open High Score file (WRITE)

    print(str(Player.score))

    if Player.score > int(current_high_score): # If score is higher than High Score
        high_score_file.write(str(Player.score)) # Write new High Score
        high_score_file.close() # Close file
    else:
        high_score_file.close() # Close file
    # High Score File (READ/WRITE) (SET NEW SCORE)

    ui.destroy() # Destroy Game UI
    exit() # Exit program


def higher(): # Higher Button Function (higher_button)
    # GLOBAL VARIABLES
    global previous_number_picked
    global number_picked
    
    global number_range

    global current_score_ui
    global number_picked_ui
    global number_range_end_ui
    global previous_number_picked_ui

    global current_score_label
    # GLOBAL VARIABLES


    number_range -= range_decrease_rate # Decrease Range (Increase Difficulty)


    if number_range < 3: # Check End Game
        end_game() # End Game Function

    
    previous_number_picked = number_picked # Switch (number_picked) to (previous_number_picked)
    number_picked = hilo_number() # Pick new random number (hilo_number())

    if number_picked > previous_number_picked: # If new number IS higher than previous number (If correct)
        Player.add_score() # Add score to Player
        current_score_label.config(fg="green") # Change Score Label to GREEN
    else: # If new number is NOT higher than previous number (If wrong)
        Player.remove_score() # Remove score from Player
        current_score_label.config(fg="red") # Change Score Label to RED

    # NEW UI VARIABLE VALUES

    current_score_ui.set(Player.score) # Set new value (Current Score)
    number_picked_ui.set(number_picked) # Set new value (Number Picked)
    number_range_end_ui.set(f"<-- {number_range}") # Set Value (Number Range End)
    previous_number_picked_ui.set(previous_number_picked) # Set Value (Previous Number Picked)

    # NEW UI VARIABLE VALUES


def lower(): # Loclass Score: # Scoring System
    # GLOBAL VARIABLES
    global previous_number_picked
    global number_picked
    
    global number_range

    global current_score_ui
    global number_picked_ui
    global number_range_end_ui
    global previous_number_picked_ui

    global current_score_label
    # GLOBAL VARIABLES


    number_range -= range_decrease_rate # Decrease Range (Increase Difficulty)


    if number_range < 3: # Check End Game
        end_game() # End Game Function

    
    previous_number_picked = number_picked # Switch (number_picked) to (previous_number_picked)
    number_picked = hilo_number() # Pick new random number (hilo_number())

    if number_picked < previous_number_picked: # If new number IS lower than previous number (If correct)
        Player.add_score() # Add score to Player
        current_score_label.config(fg="green") # Change Score Label to GREEN
    else: # If new number is NOT lower than previous number (If wrong)
        Player.remove_score() # Remove score from Player
        current_score_label.config(fg="red") # Change Score Label to RED

    # NEW UI VARIABLE VALUES

    current_score_ui.set(Player.score) # Set new value (Current Score)
    number_picked_ui.set(number_picked) # Set new value (Number Picked)
    number_range_end_ui.set(f"<-- {number_range}") # Set Value (Number Range End)
    previous_number_picked_ui.set(previous_number_picked) # Set Value (Previous Number Picked)

    # NEW UI VARIABLE VALUES


def game_ui(): # Main Game UI
    # GLOBAL VARIABLES
    global ui

    global current_score_ui
    global number_picked_ui
    global number_range_end_ui
    global previous_number_picked_ui

    global current_score_label
    # GLOBAL VARIABLES


    # UI SETTINGS
    ui = tk.Tk() # Initialise UI
    ui.title(f"HiLo {build_version}") # UI Title
    ui.geometry("500x750") # UI Resolution
    ui.resizable(0, 0) # UI Resizable (False)
    # UI SETTINGS

    # TEXTVARIABLES

    current_score_ui = tk.StringVar() # for current_score_label / Player.score
    number_picked_ui = tk.StringVar() # for number_picked_label / number_picked
    number_range_end_ui = tk.StringVar() # for number_range_end_label / number_range
    previous_number_picked_ui = tk.StringVar() # for previous_number_picked_label / previous_number_picked

    current_score_ui.set(Player.score) # Set Value (Current Score)
    number_picked_ui.set(number_picked) # Set Value (Number Picked)
    number_range_end_ui.set(f"<-- {number_range}") # Set Value (Number Range End)
    previous_number_picked_ui.set(previous_number_picked) # Set Value (Previous Number Picked)

    # TEXT VARIABLES

    # UI

    # -- Labels --
    current_score_label = tk.Label(ui, textvariable=current_score_ui, font="fixedsys 35 bold") # Current Score (current_score_ui)
    current_score_label.place(x=250, y=80, anchor="center")
    
    number_range_start_label = tk.Label(ui, text="1 -->", font="system 25 bold").place(x=100, y=225) # Start of Range (1)
    number_picked_label = tk.Label(ui, textvariable=number_picked_ui, font="times 45 bold underline").place(x=250, y=250, anchor="center") # Current Number Picked (number_picked_ui)
    number_range_end_label = tk.Label(ui, textvariable=number_range_end_ui, font="system 25 bold").place(x=300, y=225) # End of Range (number_range_end_label)

    previous_number_picked_label = tk.Label(ui, textvariable=previous_number_picked_ui, font="times 15 bold underline").place(x=250, y=320, anchor="center") # Previous Number Picked (previous_number_picked_ui)

    # -- Buttons --
    higher_button = tk.Button(ui, text="HIGHER", font="times 15 bold", command=higher).place(x=75, y=500) # Higher Button (higher())
    lower_button = tk.Button(ui, text="LOWER", font="times 15 bold", command=lower).place(x=325, y=500) # Lower Button (lower())

    # UI

    ui.mainloop() # UI Loop


def menu_ui(): # Menu UI
    # GLOBAL VARIABLES
    global menu
    # GLOBAL VARIABLES

    menu = tk.Tk() # Initialise UI
    menu.title(f"HiLo {build_version}") # UI Title
    menu.geometry("300x400") # UI Resolution
    menu.resizable(0, 0) # UI Resizable (False)

    # TEXT VARIABLES

    # Previous Game Score
    previous_game_score_ui = tk.StringVar() # for previous game score

    previous_score_file = open("Data/previous_score.txt", "r") # Open Previous Score File
    previous_game_score_ui.set(previous_score_file.readline()) # Read previous game score and set Variable
    previous_score_file.close() # Close file
    # Previous Game Score

    # Games Played 
    games_played_ui = tk.StringVar() # for total games played

    games_played_file = open("Data/games_played.txt", "r") # Open Games Played File
    games_played_ui.set(games_played_file.readline()) # Read games player score and set Variable
    games_played_file.close() # Close file

    # Games Played

    # High Score
    high_score_ui = tk.StringVar() # for High Score

    high_score_file = open("Data/high_score.txt", "r") # Open High Score File
    high_score_ui.set(high_score_file.readline()) # Read High Score and set Variable
    high_score_file.close() # Close file

    # High Score

    # TEXT VARIABLES

    # UI

    # -- Labels --

    high_score_label = tk.Label(menu, text="High Score", font="times 20 underline").place(x=150, y=50, anchor="center") # Label:"High Score"
    high_score_value_label = tk.Label(menu, textvariable=high_score_ui, font="fixedsys 25 bold").place(x=150, y=120, anchor="center") # High Score (high_score_ui)

    previous_game_score_label = tk.Label(menu, text="Previous Score", font="arial 15 underline").place(x=150, y=150, anchor="center") # Label: "Previous Score"
    previous_game_score_value_label = tk.Label(menu, textvariable=previous_game_score_ui, font="arial 20 bold").place(x=150, y=180, anchor="center") # Previous Score (previous_game_score_ui)

    games_played_label = tk.Label(menu, text="Games Played", font="arial 15 underline").place(x=150, y=220, anchor="center") # Label: "Total Games Played"
    games_played_value_label = tk.Label(menu, textvariable=games_played_ui, font="arial 20 bold").place(x=150, y=250, anchor="center") # Total Games Played (games_played_ui)

    # -- Buttons --

    play_button = tk.Button(menu, text="PLAY", font="system 15 bold", command=play).place(x=150, y=350, anchor="center") # Play Button (play())

    # UI

    menu.mainloop() # UI Loop

menu_ui() # Run Menu UI 


#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
