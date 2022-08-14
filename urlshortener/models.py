from django.db import models

class Shortener(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)    
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]
        db_table = 'shortener' # Set a name for db
        verbose_name = 'Shortener' 
        verbose_name_plural = 'Shorteners'

    def __str__(self):
        return f'{self.long_url} to {self.short_url}' # That shows db data properly.
        
