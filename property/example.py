from properties import Properties
from properties_functions import *

ps = Properties()

player = ps.create_entity()

set_transform(ps, player, position=(100, 200), rotation=45, scale=(2,2))

transform = get_transform(ps, player)
print(transform)