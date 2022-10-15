import time
SP = 10

Trust = 0
Charisma = 0
IQ = 0
attack = 20
defense = 20
fire = 0
water = 0
earth = 0
wind = 0
def intro():
  global Trust
  global Charisma
  global IQ 
  global attack 
  global defense 
  global fire
  global water
  global earth
  global wind 

  name = input("What is your name player?")
  time.sleep(1)
  print("Ah yes " + name + ". what a wonderful name!")
  time.sleep(1.5)

  print("Now it's time to choose your ability.") 
  time.sleep(1.5)

  print("But be warned what is done cannot be undone!")
  time.sleep(1.5)

  mainAbility = input("You can choose fire, water, earth, or wind?")

  while True:
    if mainAbility == "fire":
      fire += 10
      break
    elif mainAbility == "water":
      water += 10
      break
    elif mainAbility == "earth":
      earth += 10
      break
    elif mainAbility == "wind":
      wind += 10
      break
    else:
      mainAbility = input("Invalid Response. Please choose fire, water, earth or wind.")
  time.sleep(1.5)

  print("Great chioce! Now it is time to start the adventure!")
  time.sleep(1.5)
  
def story1():
  global Trust
  global Charisma
  global IQ 
  global attack 
  global defense 
  global fire
  global water
  global earth
  global wind
  print("You have now been spawned into a kingdom of free for all.")
  time.sleep(1.5)
  print("The main objective is to aquire the stone of power before anyone else.")
  time.sleep(1.5)
  print("However, you might go through some obsticles on your way to getting the stone.")
  time.sleep(1.5)
  print("syed its been like 2 hours im done ima go to bed gn")

intro()
story1()