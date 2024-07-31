from colorama import Fore, Back, Style
def draw_board(board):
    for i in range(3):
        print(Fore.RED + " | ".join(board[i]) + Style.RESET_ALL)
        print(Fore.CYAN + "---------" + Style.RESET_ALL)
        # print(Fore.RED + 'X' + Style.RESET_ALL)
        # print(Fore.BLUE + 'O' + Style.RESET_ALL)
        # print(Back.YELLOW + ' ' + Style.RESET_ALL)

def ask_and_make_move(player, board):
    try:
        x, y = ask_move(player, board)
        make_move(player, board, x, y)
    except:
        print('Неверно')
        ask_and_make_move(player, board)

def ask_move(player,board):
   # try:
        x, y = input(f'{player}, введите координаты х и у (начало 0 0): ').strip().split()
        x, y = int(x), int(y)
        if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == ' '):
            return (x, y)
        else:
            print('Клетка занята. Попробуйте еще раз.')
            ask_move(player, board)
   # except:
   #     print('Неверный ввод')
       # ask_and_make_move(player, board)


def make_move(player, board, x, y):
    if board[x][y] != ' ':
        print('Клетка занята')
        return False
    board[x][y] = player
    return True

def check_win(player, board):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
    return False

def tic_tac_toe():
    while True:
        board = [[' ' for i in range(3)] for j in range(3)]
        player = input('За кого играем? Х или 0: ').upper()
        while True:
            draw_board(board)
            ask_and_make_move(player, board)
            if check_win(player,board):
                print(f'{player} выиграли!')
                # draw_board(board)
                break
            tie_game = False
            for row in board:
                for cell in row:
                    if cell == ' ':
                        tie_game = True
            if not tie_game:
                break
            player = '0' if player == 'X' else 'X'
        restart = input('Хотите сыграть еще раз? (д/н) ')
        if restart.lower() != 'д':
            break

tic_tac_toe()