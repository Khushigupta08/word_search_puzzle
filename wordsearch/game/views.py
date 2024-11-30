from django.shortcuts import render
from .models import WordSearch
from .utils import generate_grid, place_word, fill_grid, check_win
import random

# Predefined list of words
ALL_WORDS = ['PYTHON', 'DJANGO', 'CODE', 'PROGRAMMING', 'DEVELOPER', 'JAVA', 'HTML', 'CSS', 'JAVASCRIPT', 'REACT']

def create_game(request):
    size = 10  # Example size of the grid
    
    # Randomly select words from ALL_WORDS
    words_list = random.sample(ALL_WORDS, k=min(5, len(ALL_WORDS)))  # Select up to 5 words
    
    # Filter out any words that are longer than the grid size
    words_list = [word for word in words_list if len(word) <= size]
    
    grid = generate_grid(size)

    # Place words on the grid
    for word in words_list:
        place_word(grid, word)
        
    fill_grid(grid)  # Fill remaining cells with random letters
    
    # Convert grid to string representation for storage or display purposes
    grid_str = '\n'.join([''.join(row) for row in grid])
    
    # Save the game instance
    WordSearch.objects.create(grid=grid_str, words=','.join(words_list), found_words='')
    
    return render(request, 'game/game.html', {'grid': grid, 'words': words_list})

def search_game(request):
    current_game = WordSearch.objects.last()  # Get the last created game (for example)
    
    if request.method == 'POST':
        word_found = request.POST['word'].upper()  # Convert to uppercase to match
        
        # Get current found words
        found_words_list = current_game.found_words.split(',') if current_game.found_words else []
        
        original_words_list = current_game.words.split(',')
        
        if word_found not in original_words_list:
            return render(request, 'game/game.html', {'grid': current_game.grid.splitlines(), 'words': original_words_list, 'found_words': found_words_list, 'message': "Wrong word! Try again."})

        if word_found not in found_words_list:
            found_words_list.append(word_found)

        current_game.found_words = ','.join(found_words_list)
        current_game.save()
        
        if check_win(original_words_list, found_words_list):
            return render(request, 'game/game.html', {'grid': current_game.grid.splitlines(), 'words': original_words_list, 'found_words': found_words_list, 'message': "Congratulations! You win!"})

        return render(request, 'game/game.html', {'grid': current_game.grid.splitlines(), 'words': original_words_list, 'found_words': found_words_list})

    return render(request, 'game/game.html', {'grid': current_game.grid.splitlines(), 'words': [], 'found_words': []})