#MODULES

import my_module

my_module.sumValue(1,1,1)
my_module.printValue("HolaCarlitos!")

from my_module import sumValue, printValue

sumValue(1,1,1)
printValue("Hola Carlitos!")

import math
import random

print(math.pi)
print(math.pow(2,3))
print(random.random())

from math import pi as piValue

print(piValue)