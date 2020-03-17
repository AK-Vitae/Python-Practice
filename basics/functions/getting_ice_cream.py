# Importing a function
import basics.functions.ice_cream as i
from basics.functions.ice_cream import get_ice_cream as mi

i.get_ice_cream('large', 'chocolate', 'oreos', 'sprinkles', 'cookie dough')
i.get_ice_cream('small', 'vanilla', 'chocolate syrup', "m&m's")

mi('large', 'pistachio', 'oreos', 'sprinkles', 'cookie dough')
mi('medium', 'strawberry', 'chocolate syrup', "m&m's")
