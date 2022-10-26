import time
Charisma = 0
IQ = 50
attack = 20
defense = 20
fire = 0
water = 0
earth = 0
wind = 0
money = 0
def stats():
  print(Charisma)
  print(IQ)
  print(attack)
  print(defense)
  print (fire)
  print(water)
  print(earth) 
  print(wind)
  print(money) 
def intro():
  global Charisma
  global IQ  
  global defense 
  global fire
  global water
  global earth
  global wind 
  global mainAbility
  global mainScore
  global Money
  name = input("What is your name player?")
  time.sleep(1)
  print("Ah yes " + name + ". what a wonderful name!")
  time.sleep(1.5)

  print("Now it's time to choose your ability.") 
  time.sleep(1.5)

  print("But be warned what is done cannot be undone!")
  time.sleep(1.5)

  mainAbility = input("""You can choose fire, water, earth, or wind?""").lower()

  while True:
    if mainAbility == "fire":
      fire += 10
      mainScore = fire
      break
    elif mainAbility == "water":
      water += 10
      mainScore = water
      break
    elif mainAbility == "earth":
      earth += 10
      mainScore = earth
      break
    elif mainAbility == "wind":
      wind += 10
      mainScore = wind
      break
    else:
      mainAbility = input("""I didn't quite get that. You can only pick fire, water, earth or wind so choose wisely.""").lower()
  time.sleep(1.5)

  print("""Great chioce! Now it is time to start the adventure!""")
  time.sleep(1.5)
  
def story1():
  print("""\nYour journey begins in a country called Vextop ruled by an evil tyrant named King Waes.""")
  time.sleep(4)
  
  print("""\nThe king heavily exploits the commoners for cheap labor. They make up 60% of the population and have low magical abilities. The nobles are people with great magical power. They use their power to take advantage of the commoners and makeup 10% of the population. The rest of the population is the middle class who live a somewhat peaceful life.""")
  time.sleep(10)
  
  print("""\nYou unfortunately live in an orphanage with commoners, but you possess great potential. You hope to liberate the people of Vextop by killing the king.""")
  time.sleep(6)

def story2():
  global Charisma
  global IQ 
  global defense 
  global fire
  global water
  global earth
  global wind
  global mainAbility
  global mainScore
  global money
  choice1 = input("""\nYou are currently 7 years olds. Some of orpans spend their free time training their magic or read books to gain knowledge. What would you like to do?)
  
  A. Train with your friends to increase your """ +str(mainAbility)+""" mastery.
  
  B. Learn how to read difficult books to increase your knowledge.""").lower()
  
  while True:
    if choice1 == "a":
      mainScore += 30
      defense += 10
      Charisma += 20
      time.sleep(1)
      print("""\nYou trained long and hard everyday with your friends. You kept training for 3 years when ever you found time. You got a few bruises and scars but it help  ed define your muscules and made you stronger.""")
      break
    elif choice1 == "b":
      IQ += 30
      defense += 10
      time.sleep(1)
      print("""\nWith great knowledge comes great responsibility. You are now able to read a variety amount of books and know how to speak formaly. You spend 3 years studing you learned the ability the read people and effective battle stategies during conflict.""")
      break
    else:
      choice1 = input("You must choose option A or B. So pick one! ").lower()
  time.sleep(7)

  print("""\nYou decide that it is about time leave the orphanage and start to travel through the country to gain new skills and alies. Before leave you ask everyone to if they would join you on your quest.""")
  time.sleep(8)
  if choice1 == "a":
    print("""\nEveryone looked at each other unsure wheather to join you. But one person name Hingy agreed to join you. He was your best friend and you two train a lot with each other. You were happy to have a companion and set off to a city called Fargu.""")
    money += 100
    time.sleep(5)
  else:
    print("""\nEveryone looked at each other and they all declined. They were all afraid and didn't believe that you can kill the king one day. I guess it is the consequese of reading all day and not making friends. None the less you go off on your quest alone to your first city called Fargu.""")
    money += 100
    time.sleep(5)
  
  print("""\nYou walk for 2 hours, you encounter a man by the side of the trail, he offers you a cool spell book. Would you like to purchace it?""")
  time.sleep(2)
  
  #High IQ options
  while IQ ==80:
    choice2 = input("""\nA. This seems like a scam. Decline his offer."
      
B. Take your chances. This book may give you new magical ability.""").lower()
    break
  while IQ == 80:
    if choice2 == "a":
      print("""\nYou decline his offer. He seems angry but you made the right call. It's to early to take such a risk.""")
      break
    elif choice2 == "b":
      print("""\nTake your chances and take the book. But unfortunately it was a scam and you lost all of your money. You try to confront him but he was already gone.""")
      break
    else:
      choice2= input("Invaild response. Please choose option A or B.").lower()

#Low IQ options
  while IQ < 80:
    choice2 = input("""\nA. Decline his offer?"
      
      B. Take the book this book may give you new magical ability.""").lower()
    break
  while IQ < 80:
    if choice2 == "a":
      print("You decline his offer. You missed out on a good deal")
    elif choice2 == "b":
      print("""\nTake your chances and take the book. But unfortunately it was a scam and you lost all of your money. You try to confront him but he was already gone.""")
    Money = 0
  else:
      choice2= input("Invaild response. Please choose option A or B.").lower()

def story3(): 
  print("You finally arrive to Fargu and final goal is to kill the King Waes. But you can't do it alone, you want to find other people to team up with to defeat the King.")
  time.sleep(5)
  print("You see a warrior in the distance and you're thinking of going up to him.")
  time.sleep(2)
  print("Me:Hey who are you?!")
  time.sleep(1)
  print("""Warrior: "I'm Bani, what do you want?" *Casually floating water in his right hand*""")
  time.sleep(2)
  print("Hey I'm "+ name +"")



stats()
intro()
story1()
story2()