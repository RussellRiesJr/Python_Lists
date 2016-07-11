import random

random_numbers = random.sample(range(50), 20)
print(random_numbers)

def squared(random_numbers):
  return [num ** 2 for num in random_numbers]

print(squared(random_numbers))

import code
code.interact(local=locals())
