from random import randint
import random


def main():
    pass
    CHOICE = ['r', 'p', 's']
    PLAYERS = ['1', 'comp']
    user_ply = []
    ply_round = 0
    ply_win = 0
    com_win = 0
    print("--------------------------------------------------------------------")
    print(r"""THIS IS A GAME OF ROCK, PAPER AND SICSSORS TO PLAY EITHER ENTER
R FOR "ROCK" P FOR "PAPER" AND "S" FOR SCISSORS """)

    while True:
        computer = randint(0, 2)
        com = CHOICE[computer]
        ply_round += 1
        active_player = PLAYER[0]
        isPlayer1_TheActive_Player = True
        if isPlayer1_TheActive_Player:
            for i, players in enumerate(PLAYERS):
                if active_player == PLAYERS[i]:
                    print(
                        "--------------------------------------------------------------------")
                    print(
                        r"Player One Enter your choice [R]ock [P]aper [S]cissors:")
                    ply_1 = input('Enter "Rock","Paper","Scissors :" ')
                    user_ply.append(ply_1)
                    for j, v in enumerate(CHOICE):
                        if CHOICE[j] in ply_1:
                            print(f'You chose {CHOICE[j]}')
                else:
                    print('------------------------------------------')
                    print('Player Two : Computers Turn')
                    user_ply.append(com)
                    for j, v in enumerate(CHOICE):
                        if CHOICE[j] in com:
                            print(f'Compture chose {CHOICE[j]}')
                            isPlayer1_TheActive_Player = False

        if ((user_ply[0] == CHOICE[-1] and user_ply[1] == CHOICE[-1]) or (user_ply[0] == CHOICE[1] and user_ply[1] == CHOICE[1]) or (user_ply[0] == CHOICE[0] and user_ply[1] == CHOICE[0])):
            print('------------------------------------------')
            print(fr'The result of round {ply_round} is a draw')
            user_ply.clear()
            # Checking if rock of player wins at pos 0
        elif (user_ply[0] == CHOICE[0] and user_ply[1] == CHOICE[-1]):
            print('------------------------------------------')
            print(fr'The result of round {ply_round} is a win for P1')
            user_ply.clear()
            ply_win += 1
            # Checking if rock of player wins at pos 1
        elif (user_ply[1] == CHOICE[0] and user_ply[0] == CHOICE[-1]):
            print('------------------------------------------')
            print(fr'The result of round {ply_round} is a win for P2')
            user_ply.clear()
            com_win += 1
            # Checking if scissors of player wins at pos 0
        elif (user_ply[0] == CHOICE[-1] and user_ply[1] == CHOICE[1]):
            print('------------------------------------------')
            print(fr'The result of round {ply_round} is a win for P1')
            user_ply.clear()
            ply_win += 1
            # Checking if scissors of player wins at pos 1
        elif (user_ply[1] == CHOICE[-1] and user_ply[0] == CHOICE[1]):
            print('------------------------------------------')
            print(fr'The result of round {ply_round} is a win for P2')
            user_ply.clear()
            com_win += 1
            # Checking if paper of player wins at pos 0
        elif (user_ply[0] == CHOICE[1] and user_ply[1] == CHOICE[0]):
            print('------------------------------------------')
            print(fr'The result of round {ply_round} is a win for P1')
            user_ply.clear()
            ply_win += 1
        elif (user_ply[1] == CHOICE[1] and user_ply[0] == CHOICE[0]):
            print('------------------------------------------')
            print(fr'The result of round {ply_round} is a win for P2')
            user_ply.clear()
            com_win += 1
        else:
            user_ply.clear()
        if ply_round == 5:
            break
    print('------------------------------------------')
    print()
    if ply_win > com_win:
        print('Game Over : Human won')
        print()
    elif ply_win < com_win:
        print('Game Over : Computer Won')
        print()
    else:
        print('Game Over : Tie')
        print()


if __name__ == "__main__":
    main()
