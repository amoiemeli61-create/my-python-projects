# Game Settings
players = []
score1 = 0
score2 = 0
rounds = ""
player_name = ""
player_name2 = ""
symbol = ""
symbol2 = ""

while True:
    # Main Menu
    print(
        "tic_tac_toe_play🎮"
        "\n"
        "1. Start Game"
        "\n"
        "2. How to Play"
        "\n"
        "3. Scoreboard"
        "\n"
        "4. Exit"
    )

    choice = input("Enter your choice: ")
    if not choice.isdigit():
        print("Please enter numbers only.")
        continue
    choice = int(choice)
    if choice == 1:
        # Game Menu
        while True:
            print(
                "Start Game✨"
                "\n"
                "1. Player_Name & Symbol"
                "\n"
                "2. Number of Rounds"
                "\n"
                "3. Start Playing"
                "\n"
                "4. Back to Main Menu"
            )
            select = input("Select an option: ")
            if not select.isdigit():
                print("Please enter numbers only.")
                continue
            select = int(select)
            start_game = False

            if select == 1:
                # Player Settings
                while True:
                    while True:
                        player_name = input("Enter Player 1 name: ")
                        if player_name == "":
                            print("Name cannot be empty. Please enter your name.")
                            continue
                        break

                    while True:
                        symbol = input("Enter Player 1 symbol(X / O / * / $ / ~ / +): ")
                        if symbol == "":
                            print("Symbol cannot be empty. Please choose a symbol.")
                            continue
                        if (
                            symbol == "X"
                            or symbol == "O"
                            or symbol == "*"
                            or symbol == "$"
                            or symbol == "~"
                            or symbol == "+"
                        ):
                            break
                        else:
                            print(
                                "Invalid symbol! Please choose one of the allowed symbols (X, O, *, $, ~, +)."
                            )
                            continue

                    while True:
                        player_name2 = input("Enter Player 2 name: ")
                        if player_name2 == "":
                            print("Name cannot be empty. Please enter your name.")
                            continue

                        while True:
                            symbol2 = input(
                                "Enter Player 2 symbol(X / O / * / $ / ~ / + ): "
                            )
                            if symbol2 == "":
                                print("Symbol cannot be empty. Please choose a symbol.")
                                continue
                            if (
                                symbol2 == "X"
                                or symbol2 == "O"
                                or symbol2 == "*"
                                or symbol2 == "$"
                                or symbol2 == "~"
                                or symbol2 == "+"
                            ):
                                break
                            else:
                                print(
                                    "Invalid symbol! Please choose one of the allowed symbols (X, O, *, $, ~, +)."
                                )
                            continue

                        if symbol == symbol2:
                            print(
                                "This symbol is already taken! Please choose a different one."
                            )
                            continue
                        break

                    play = [player_name, symbol, player_name2, symbol2]
                    players.append(play)
                    print(players)
                    break

            if select == 2:
                # Round Settings
                while True:
                    rounds = input("How many rounds do you want to play? ")
                    if rounds == "":
                        print("Please enter the number of rounds.")
                        continue
                    if not rounds.isdigit():
                        print("Please enter numbers only.")
                        continue
                    rounds = int(rounds)
                    if rounds < 1:
                        print("Please enter a valid number of rounds (1 or more).")
                        continue
                    break

            if select == 3:
                # Check Game Settings
                if (
                    player_name == ""
                    or player_name2 == ""
                    or symbol == ""
                    or symbol2 == ""
                    or rounds == ""
                ):
                    print(
                        "Please set up both players and the number of rounds before starting the game!"
                    )
                else:
                    start_game = True

            if start_game == True:
                # Game Rounds
                for j in range(1, rounds + 1):
                    print("Round", j)
                    current_turn = 1

                    # Initialize Game Board
                    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

                    while True:
                        print(
                            f"{board[0]}  |  {board[1]}  |  {board[2]} "
                            "\n"
                            "---|-----|---"
                            "\n"
                            f"{board[3]}  |  {board[4]}  |  {board[5]}"
                            "\n"
                            "---|-----|---"
                            "\n"
                            f"{board[6]}  |  {board[7]}  |  {board[8]}"
                        )

                        # Player 1 Turn
                        if current_turn == 1:
                            call_number1 = input(
                                f"{player_name}:Choose a number(1_9): "
                            )
                            if not call_number1.isdigit():
                                print("Please enter numbers only.")
                                continue
                            call_number1 = int(call_number1)
                            if 1 > call_number1 or call_number1 > 9:
                                print("Please enter a number between 1 and 9.")
                                continue
                            if board[call_number1 - 1] != str(call_number1):
                                print(
                                    "This cell is already taken! Please choose another number."
                                )
                                continue

                            current_turn = 2
                            board[call_number1 - 1] = symbol

                            # Check Player 1 Win
                            if (
                                board[0] == board[1] == board[2] == symbol
                                or board[3] == board[4] == board[5] == symbol
                                or board[6] == board[7] == board[8] == symbol
                                or board[0] == board[3] == board[6] == symbol
                                or board[1] == board[4] == board[7] == symbol
                                or board[2] == board[5] == board[8] == symbol
                                or board[0] == board[4] == board[8] == symbol
                                or board[2] == board[4] == board[6] == symbol
                            ):
                                score1 += 1
                                print(player_name, "Wins! 🏆")
                                break

                            # Check Draw
                            if (
                                board[0] != "1"
                                and board[1] != "2"
                                and board[2] != "3"
                                and board[3] != "4"
                                and board[4] != "5"
                                and board[5] != "6"
                                and board[6] != "7"
                                and board[7] != "8"
                                and board[8] != "9"
                            ):
                                print("The game is a Draw!")
                                break

                        # Player 2 Turn
                        if current_turn == 2:
                            call_number2 = input(
                                f"{player_name2}:Choose a number(1_9): "
                            )
                            if not call_number2.isdigit():
                                print("Please enter numbers only.")
                                continue
                            call_number2 = int(call_number2)
                            if 1 > call_number2 or call_number2 > 9:
                                print("Please enter a number between 1 and 9.")
                                continue
                            if board[call_number2 - 1] != str(call_number2):
                                print(
                                    "This cell is already taken! Please choose another number."
                                )
                                continue

                            current_turn = 1
                            board[call_number2 - 1] = symbol2

                            # Check Player 2 Win
                            if (
                                board[0] == board[1] == board[2] == symbol2
                                or board[3] == board[4] == board[5] == symbol2
                                or board[6] == board[7] == board[8] == symbol2
                                or board[0] == board[3] == board[6] == symbol2
                                or board[1] == board[4] == board[7] == symbol2
                                or board[2] == board[5] == board[8] == symbol2
                                or board[0] == board[4] == board[8] == symbol2
                                or board[2] == board[4] == board[6] == symbol2
                            ):
                                score2 += 1
                                print(player_name2, "Wins! 🏆")
                                break

                            # Check Draw
                            if (
                                board[0] != "1"
                                and board[1] != "2"
                                and board[2] != "3"
                                and board[3] != "4"
                                and board[4] != "5"
                                and board[5] != "6"
                                and board[6] != "7"
                                and board[7] != "8"
                                and board[8] != "9"
                            ):
                                print("The game is a Draw!")
                                break

            if select == 4:
                break

    # How to Play
    if choice == 2:
        print(
            "🎮 TIC TAC TOE - HOW TO PLAY"
            "\n"
            "1. This game is for 2 players."
            "\n"
            "2. Each player can choose their own name and symbol."
            "\n"
            "3. Players must choose different symbols."
            "\n"
            "4. Players take turns choosing a number from 1 to 9."
            "\n"
            "5. Players can only choose empty cells."
            "\n"
            "6. The first player to get 3 matching symbols in a row wins."
            "\n"
            "7. Winning combinations can be horizontal, vertical, or diagonal."
            "\n"
            "8. If all 9 cells are filled and nobody wins, the game is a draw."
        )

    # Scoreboard
    if choice == 3:
        print("Final Score 🏆")
        print(player_name, ":", score1, "\n", player_name2, ":", score2)

        if score1 > score2:
            print(player_name, "Overall Winner🥇")
        if score2 > score1:
            print(player_name2, "Overall Winner🥇")
        if score1 == score2:
            print("The game is a tie!")

    # Exit Game
    if choice == 4:
        break
