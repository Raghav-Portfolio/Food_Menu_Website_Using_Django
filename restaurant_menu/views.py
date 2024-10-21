from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = Item.objects.order_by() #queryset will store a list of data
    template_name = "index.html" # template_name is a standard variable in views that removes the need for a 'return' function
                                 # and also connects this class to the front page of the website

    def get_context_data(self, **kwargs): #predefined method that is being overwritten
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context 
    
    
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'
    