from django.db import models

class WordSearch(models.Model):
    grid = models.TextField()  # Store the grid as a string
    words = models.TextField()  # Store words as a comma-separated string
    found_words = models.TextField(default='')  # Store found words as a comma-separated string

    def __str__(self):
        return f"WordSearch({self.id})"