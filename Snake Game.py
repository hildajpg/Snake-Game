import random
import os
import time

def print_board(board, score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Snake Game")
    print("Score: ", score)
    for row in board:
        print(" ".join(row))

def update_snake(snake, direction):
    if direction == 'up':
        snake[0] -= 1
    elif direction == 'down':
        snake[0] += 1
    elif direction == 'left':
        snake[1] -= 1
    elif direction == 'right':
        snake[1] += 1
def check_collision(snake, board):
    if snake[0] < 0 or snake[0] >= len(board) or snake[1] < 0 or snake[1] >= len(board[0]):
        return True
    if board[snake[0]][snake[1]] == 'X':
        return True
    return False

def main():
    board_size = 20
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    snake = [board_size//2, board_size//2]
    board[snake[0]][snake[1]] = 'O'
    direction = 'up'
    score = 0

    while True:
        food = [random.randint(0, board_size-1), random.randint(0, board_size-1)]
        while board[food[0]][food[1]] != ' ':
            food = [random.randint(0, board_size-1), random.randint(0, board_size-1)]
        board[food[0]][food[1]] = 'F'
        while True:
            print_board(board, score)
            time.sleep(0.1)

            direction = input("Enter direction (up/down/left/right): ").lower()
            if direction == 'quit':
                return

            update_snake(snake, direction)

            if check_collision(snake, board):
                print("Game Over! Your final score is:", score)
                return

            if snake == food:
                score += 1
                board[food[0]][food[1]] = ' '
                break

            board[snake[0]][snake[1]] = 'O'
            tail = [snake[0], snake[1]]
            while board[tail[0]][tail[1]] == 'O':
                board[tail[0]][tail[1]] = ' '
                if direction == 'up':
                    tail[0] += 1
                elif direction == 'down':
                    tail[0] -= 1
                elif direction == 'left':
                    tail[1] += 1
                elif direction == 'right':
                    tail[1] -= 1
                    
if __name__ == "__main__":
    main()