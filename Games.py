import pygame
import sys
import numpy as np

# تنظیمات اولیه
pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# صفحه بازی
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# تابع برای رسم خطوط
def draw_lines():
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# تابع برای رسم X و O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 30, row * SQUARE_SIZE + 30),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 30, row * SQUARE_SIZE + SQUARE_SIZE - 30), LINE_WIDTH)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE - 30, row * SQUARE_SIZE + 30),
                                 (col * SQUARE_SIZE + 30, row * SQUARE_SIZE + SQUARE_SIZE - 30), LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3, LINE_WIDTH)

# تابع برای بررسی برنده
def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return None

# تابع Minimax برای بهترین حرکت کامپیوتر
def minimax(board, depth, is_maximizing):
    score = check_winner()
    if score == 1:  # بازیکن X
        return -10 + depth
    elif score == 2:  # کامپیوتر O
        return 10 - depth
    if np.all(board != 0):  # مساوی
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i][j] == 0:
                    board[i][j] = 2  # حرکت کامپیوتر
                    score = minimax(board, depth + 1, False)
                    board[i][j] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i][j] == 0:
                    board[i][j] = 1  # حرکت بازیکن
                    score = minimax(board, depth + 1, True)
                    board[i][j] = 0
                    best_score = min(score, best_score)
        return best_score

# تابع برای پیدا کردن بهترین حرکت کامپیوتر
def find_best_move():
    best_score = float('-inf')
    move = (-1, -1)
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == 0:
                board[i][j] = 2  # حرکت کامپیوتر
                score = minimax(board, 0, False)
                board[i][j] = 0
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# تابع برای بازی
def main():
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(WHITE)
    draw_lines()

    player = 1
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == 0:
                    board[clicked_row][clicked_col] = player
                    draw_figures()

                    winner = check_winner()
                    if winner:
                        game_over = True
                        print(f"Player {winner} wins!")

                    # نوبت کامپیوتر
                    if not game_over:
                        move = find_best_move()
                        board[move[0]][move[1]] = 2  # حرکت کامپیوتر
                        draw_figures()

                        winner = check_winner()
                        if winner:
                            game_over = True
                            print("Computer wins!")

        pygame.display.update()

if __name__ == "__main__":
    main()