planet_list = ["Mercury", "Mars"]

def add_planets():
  planet_list.append("Jupiter")
  planet_list.append("Saturn")
  print(planet_list)

def more_planets():
  planet_list.extend(["Uranus", "Neptune"])
  print(planet_list)

def update_planets():
  planet_list.insert(1, "Venus")
  planet_list.insert(2, "Earth")
  print(planet_list)

def call_all():
  add_planets()
  more_planets()
  update_planets()

import code
code.interact(local=locals())
