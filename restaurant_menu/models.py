# Commit 6:
from django.db import models
# Commit 6: importing the User module
from django.contrib.auth.models import User

# Commit 6: These are the choices for the meal_type column
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

# Commit 6: These are the choices for the status column
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


# Commit 6: Creating the table
class Item(models.Model):
    # Commit 6: Creating the columns of the table
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Commit 6: This column will have specific choices
    meal_type = models.CharField(max_length=2000, choices=MEAL_TYPE)
    # Commit 6: Creating a column author that will be related
    # to the user table
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # Commit 6: Creating a column that has two options Unavailable=0
    # Available=1
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.meal
