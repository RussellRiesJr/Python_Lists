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

def add_pluto():
  planet_list.append("Pluto")
  print(planet_list)

def slice_planets():
  rocky_planets = []
  sliceObj = slice(0,4)
  rocky_planets = planet_list[sliceObj]
  print(rocky_planets)

def delete_pluto():
  del planet_list[8]
  print(planet_list)

def call_all():
  add_planets()
  more_planets()
  update_planets()
  add_pluto()
  slice_planets()
  delete_pluto()

import code
code.interact(local=locals())
