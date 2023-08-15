from .category import Category
from .item import Item

hat = Item(
    "Hat",
    'The epitome of "hat-titude"! This hat will keep you warm and stylish.',
    Category.CLOTHES,
    3.2,
    0.34,
)

boots = Item(
    "Boots",
    "Sturdy and durable boots designed to withstand various terrains.",
    Category.CLOTHES,
    5.6,
    1.75,
)

sword = Item(
    "Sword",
    "Look, it’s 2023. Who carries a sword? YOU DO! Swipe right for chivalry and left for dragons.",
    Category.WEAPON,
    13.2,
    6.4,
)

bow = Item(
    "Bow",
    "This is my bow. There are many like it, but this stringy wonder is mine.",
    Category.WEAPON,
    10.7,
    4.8,
)

bread = Item(
    "Bread",
    "A wholesome loaf, rich with yeast and hearty grains. Butter not included, but let's be honest - it's essential.",
    Category.FOOD,
    2.7,
    0.78,
)

apple = Item(
    "Apple",
    "A juicy apple, perfect for a quick and healthy snack. Just don't eat the seeds!",
    Category.FOOD,
    0.34,
    0.27,
)

BASIC_ITEMS = [hat, boots, sword, bow, bread, apple]
