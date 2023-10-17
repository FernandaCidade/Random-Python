# Retorna a combinação completa de 6 valores, aleatórios e diferentes entre si.
import random
from random import sample

megaSena = random.sample(range(1,60),6)
print("Os números para a MegaSena são: ",megaSena)
