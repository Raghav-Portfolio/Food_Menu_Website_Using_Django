from django.db import models
from django.contrib.auth.models import User

'''
    Index 0 of each tuple is used in the backend code,
    while index 1 of each tuple(the items starting with a capital letter) is displayed on the website
'''
MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)       

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True) # this creates a dish in the menu
    description = models.CharField( max_length=2000) # details of the dish
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a cook (User) is deleted from the database 
                                                               # then all of their dishes are also deleted simultaneously
                                                               # if this parameter were set to SET_NULL, then the dishes would still be there
                                                               # but there wouldn't be any chef assigned to these dishes, a  new one
                                                               # would have to fill this position
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True) # records when an item (dish) is created
    date_updated = models.DateTimeField(auto_now=True)  # records when an item (dish) is edited  
    
    def __str__(self):
        return self.meal              
# Create your models here.
