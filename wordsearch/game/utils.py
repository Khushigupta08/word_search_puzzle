import random

def generate_grid(size):
    return [['' for _ in range(size)] for _ in range(size)]

def place_word(grid, word):
    size = len(grid)
    placed = False
    
    while not placed:
        direction = random.choice(['horizontal', 'vertical', 'diagonal'])
        
        if direction == 'horizontal':
            row = random.randint(0, size - 1)
            col = random.randint(0, size - len(word))  # Ensure col is valid
            if col >= 0 and all(grid[row][col + i] == '' for i in range(len(word))):
                for i in range(len(word)):
                    grid[row][col + i] = word[i]
                placed = True
                
        elif direction == 'vertical':
            col = random.randint(0, size - 1)
            row = random.randint(0, size - len(word))  # Ensure row is valid
            if row >= 0 and all(grid[row + i][col] == '' for i in range(len(word))):
                for i in range(len(word)):
                    grid[row + i][col] = word[i]
                placed = True
                
        elif direction == 'diagonal':
            row = random.randint(0, size - len(word))  # Ensure row is valid
            col = random.randint(0, size - len(word))  # Ensure col is valid
            if row >= 0 and col >= 0 and all(grid[row + i][col + i] == '' for i in range(len(word))):
                for i in range(len(word)):
                    grid[row + i][col + i] = word[i]
                placed = True

def fill_grid(grid):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '':
                grid[r][c] = random.choice(alphabet)

def check_win(words, found_words):
    return set(words) == set(found_words)