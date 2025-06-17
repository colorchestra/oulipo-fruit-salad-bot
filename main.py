#!/usr/bin/python3
from mastodon import Mastodon
import config
import random

fruits = [
    "🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🫐", "🍈", "🍒", "🍑", "🥭", "🍍", "🥝", "🍋‍🟩"
]
fruit_salad = ""
masto = Mastodon(
    password_string = config.mastodon_password_string,
    api_url = config.api_url,
)

fruit_salad_long = random.randint(5, 16)
for i in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    fruit_salad = fruit_salad + fruits[random.randint(0, 15)]

masto.status_post(
    status=fruit_salad,
)