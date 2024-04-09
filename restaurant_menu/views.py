from django.shortcuts import render
# Commit 7:
from django.views import generic
from .models import Item, MEAL_TYPE


# commit 7: Create a class view base
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    # Commit 8:
    # Commit 9:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


# Commit 7:
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_Item_detail.html"
