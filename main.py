import time
charisma = 0
IQ = 50
attack = 20
defense = 20
mainScore = 10
money = 0
def stats():
  print("\nIQ = " +str(IQ))
  print("Attack = " +str(attack))
  print("Defence = " +str(defense))
  print (mainAbility+" = " +str(mainScore))
  print("Money = " +str(money)) 
  time.sleep(4)
def intro():
  global charisma
  global IQ  
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  name = input("What is your name player?")
  time.sleep(1)
  print("Ah yes " + name + ". what a wonderful name!")
  time.sleep(1.5)

  print("Now it's time to choose your ability.") 
  time.sleep(1.5)

  print("But be warned what is done cannot be undone!")
  time.sleep(1.5)

  mainAbility = input("""You can choose fire, water, earth, or wind?\n""").lower()

  while True:
    if mainAbility == "fire" or mainAbility == "water" or mainAbility == "earth" or mainAbility == "wind":
      mainScore += 10
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
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  choice1 = input("""\nYou are currently 7 years olds. Some of orpans spend their free time training their magic or read books to gain knowledge. What would you like to do?
  
  A. Train with your friends to increase your """ +str(mainAbility)+""" mastery.
  
  B. Learn how to read difficult books to increase your knowledge.

Your Choice: """).lower()
  time.sleep(1)
  while True:
    if choice1 == "a":
      mainScore += 30
      attack += 10
      defense += 10
      charisma += 20
      time.sleep(1)
      print("""\nYou trained long and hard everyday with your friends. You kept training for 3 years when ever you found time. You got a few bruises and scars but it helped define your muscules and made you stronger.""")
      break
    elif choice1 == "b":
      IQ += 30
      attack += 10
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
    print("""\nEveryone looked at each other unsure wheather to join you. But one person name Hingy agreed to join you. He was your best friend and you two train a lot with each other. You both have a total of 200 gold that you have earned through the years. You were happy to have a companion and set off to a city called Fargu.""")
    money += 200
    time.sleep(5)
  else:
    print("""\nEveryone looked at each other and they all declined. They were all afraid and didn't believe that you can kill the king one day. I guess it is the consequese of reading all day and not making friends. You only have 100 gold to your name. None the less you go off on your quest alone to your first city called Fargu.""")
    money += 100
    time.sleep(5)

  print("""\nYou walk for 2 hours, you encounter a man by the side of the trail, he offers you a cool spell book. Would you like to purchace it?""")
  time.sleep(2)
  
  #High IQ options
  while IQ ==80:
    choice2 = input("""\n    A. This seems like a scam. Decline his offer.
      
    B. Take your chances. This book may give you new magical ability.
    
You Choice: """).lower()
    break
  while IQ == 80:
    if choice2 == "a":
      print("""\nYou decline his offer. He seems angry but you made the right call. It's to early to take such a risk.""")
      IQ += 10
      break
    elif choice2 == "b":
      print("""\nTake your chances and take the book. But unfortunately it was a scam and you lost all of your money. You try to confront him but he was already gone.""")
      IQ -= 10
      break
    else:
      choice2= input("Invaild response. Please choose option A or B.").lower()
#Low IQ options
  while IQ < 80:
    choice2 = input("""\n    A. Decline his offer?
      
    B. Take the book this book may give you new magical ability.

Your Choice: """).lower()
    break
  while IQ < 80:
    if choice2 == "a":
      print("\nYou decline his offer. You might have missed out on a good deal. But it's too early to make any rash decisions.")
      IQ += 10
      break
    elif choice2 == "b":
      print("""\nTake your chances and take the book. But unfortunately it was a scam and you lost all of your money. You try to confront him but he was already gone.""")
      IQ -= 10
      money = 0
      break
    else:
      choice2= input("Invaild response. Please choose option A or B.").lower()
  time.sleep(4)
def story3(): 
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  print("\nYou finally arrive to Fargu and final goal is to kill the King Waes. But you can't do it alone, you want to find other people to team up with to defeat the King.")
  time.sleep(5)
  print("\nYou see a warrior in the distance and you're thinking of going up to him.")
  time.sleep(2)
  print("\n"+name+": Hey who are you?!")
  time.sleep(1)
  print("""\nWarrior: "I'm Bani, what do you want?" *Casually floating water in his right hand*""")
  time.sleep(2)
  print("\n" +name+": Hey I'm "+ str(name) + """, and I need your help. Can you team up with me? We need to kill the King before he has full control of our nation.""")
  time.sleep(2)
  print("""\nBani: Kill the king you say? Why do you need my help?""")
  time.sleep(1)
  print("\n"+name+ """: Because you're one of a few people I'm going to find here and I see you have water powers so we can combine our powers to fight through this""")
  time.sleep(2)
  print("""\nBani: The king is someone to not be underestimated. He has a whole army by his side.""")
  time.sleep(2)
  print("""\nMy brother is part of his army. The king has his daughter captive in the next country 3 weeks away.I want you help me save her after we kill the king?""") 
  time.sleep(2)
  print("\n"+name+""": I will save your niece after killing the king""")
  time.sleep(3)
  print("""\nBani: Now I must ask you a few questions to test your knowledge. If you are able to answer them correctly I will join you.""")
  time.sleep(5)
  print("\n"+name+""": OK. What are your questions.""")
  time.sleep(2)
  questions = []
  choice3 = input("""\nWhat is the fith plant in our solar system?
    A. Jupiter
    B. Mars
    C. Saturn 
    D. Uranus

Your Choice: """).lower()
  time.sleep(1)
  while True:
    if choice3 == "a":
      print("Correct, next one.")
      choice3 = "correct"
      IQ += 10
      break
    elif choice3 == "b" or choice3 == "c" or choice3 == "d":
      print("Wrong, I'll give you 1 more chance.")
      choice3 = "incorrect"
      IQ -= 10
      break
    else:
      choice3 = input("Wrong, pick something else.").lower()
  questions.append(choice3)
  time.sleep(3)
  
  choice4 = input("""\nNext, what is the pythagorean theorom?
    A.a^2+b^2=c^2
    B.a^2 + b^2 = (a+b)(a-b)
    C.y=mx+b
    D.V=s^3

Your Choice: """).lower()
  time.sleep(1)  
  while True:
    if choice4 == "a":
      print("Correct")
      choice4 = "correct"
      IQ += 10
      break
    elif choice4 == "b" or choice4 == "c" or choice4 == "d":
      print("Wrong.")
      choice4 = "incorrect"
      IQ -= 10
      break
    else:
      choice4 = input("Wrong, pick something else.").lower()
  questions.append(choice4)
  time.sleep(3)
  
  while choice3 == "correct" or choice4 == "correct":
    choice5 = input("""\nWhen did the United States first gain its independence?
    
    A. 1738
    B. 1492
    C. 1776
    D. 1888

Your Choice: """).lower()
    break
  time.sleep(1)
  while choice3 == "correct" or choice4 == "correct":
    if choice5 == "a" or choice5 == "b" or choice5 == "d":
      print("Incorrect")
      choice5 = "incorrect"
      IQ -= 10
      questions.append(choice5)
      break
    elif choice5 == "c":
      print("Correct")
      choice5 = "correct"
      IQ += 10
      questions.append(choice5)
      break
    else:
      choice5 = input("Wrong, pick something else.").lower()
  time.sleep(2)
  correct = questions.count("correct")
  while correct > 1:
    print("""Wow, Your pretty smart. Seems like I'll trust your judgement and fight along side you.""")
    charisma += 20
    break
  while correct < 2: 
    print("\nBani: You are very dumb. If you can not answer such basic questions, how do you ever expect to defeat the king. I am not going to join you in your quest.")
    break 
  time.sleep(4)
def story4():
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  print("After ecountering with Bani, your quest continues.")
  time.sleep(2.5)
  choice6 = input("""/nWe have a month of time to kill, what do you want to do to pass the time? Somthing productive."

  A. Go to library
  B. Go to bed
  C. Train in courtyard
  D. Go to party

  Your Choice: """).lower()
  while True:
    if choice6 == "a":
      print("Good, you can study about ancient aspects. Your magical abilities increased dramaitcally. A")
      mainScore += 10
      IQ += 15
      break
    elif choice6 == "b":
      print("Nice, you wasted your time sleeping. Time is running out, we need to deafet king Waes.")
      break
    elif choice6 == "c":
      print("Cool, you trained for a whole month here you became a better warrior.")
      attack += 30
      defense += 20
      break
    elif choice6 == "d":
      print("""You went to a party and you became more socially active and made a friend named Baolue. He is also a warrior in training with earth abilities. His family has history with the king, his sister got killed in a crossfire within their disputes. He lost his grandfather from battling the king. He agreed to join your side on defeating King Waes.""")
      charisma += 10
      break
    else:
      choice6 = input("Invaid response. Select one of the choices.").lower()
    time.sleep(4)
def story5():
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  print("\nYou feel hungry so you decide to head to a nearby diner.")
  time.sleep(2.5)
  print("""\n*CRASH!!!!!* You see a man fly out of the window of the diner. "AND STAY OUT YOU FREELOADER!!" says a man.""")
  time.sleep(2.5)
  print("""\nYou approach the man who flew out the window he seems drunk""")
  time.sleep(2.5)
  print("""\nHes carrying 4 swords on his side and has a bottle of beer in one hand""")
  time.sleep(2.5)
  print("""\nDrunkman: HEY U!!! I rann outa munny canb u spar mi sum chang.""")
  time.sleep(2.5)
  print("""\nYou look toward the diner theres a wanted poster on the wall, its the drunk man.""")
  time.sleep(2.5)
  print("""\nYou read under the poster "WANTED DEAD OR ALIVE! Yasen wanted for treason against the king, he has killed over 100 of the kings soldiers BEWARE!""")
  time.sleep(2.5)
  print("""\nThis guy seems like a good person to help me defeat the king. I need to get him to join my team.""")
  time.sleep(2.5)
  print("""\nHey you join my team!. 
  Yasen: hrmmmm. If u defeet meee! I wil join u!"""
   +name+""":This will be a piece of cake. Hes so drunk I would never lose.""")
  time.sleep(2.5)
  print("""\n Alright lets fight!""")
  while IQ < 80:
    choice7 = input("""\nHow should I start my first attack?
    A: Hard punch
    B: Flying kick
    C: Kick in the groin""").lower()
    break
  while IQ > 80:
    choice7 = input("""How should I start my first attack?
    A: Hard punch
    B: Flying kick
    C: Kick in the groin
    D: Attack him with your """ + mainAbility+ """ ability. Swords can't block magic
    
    Your Choice: """).lower()  
    break
  while True:
    if choice7 == "a":
      print("""\n You punch him hard in the face. He dodges the punch and hits you on the head with the back of his sword.
      Yasen: Really a punch?""")
      break
    elif choice7 =="b":
      print("""\nYou run and do a flying kick he grabs your leg and swings you to the ground.""")
      break
    elif choice7 == "c":
      print("""\nYou kick him in the groin with all your might. You hear a metal bang. 
    Yasen: I prepared for those kind of attacks.""")
      break
    elif choice7 == "d":
      print("""\nYou attack him with your """ + mainAbility+ """ ability. He trys to block it with his sword. But fails. He is blown back by your attack.""")
      break
    else:
      choice7 = input("Invalid response. Select one of the choices").lower()
  while choice7 != "d":
    print("""Your attacks failed Yasen puts a bandana on his head the arua around him turns dark and serious 
 he positions his 4 sword in the shape of a square. He vanishes into thin air. You feel a sharp pain he struck you in the stomach. """+name+"""GAHHHH!!!
 You feel like your ribs just broke.
 Yasen: I hit you with the back of my swords. Come back when your stronger.""")
  while choice7 == "d":
    print("""Yasen: You have bested me I will  """)
def story6():
  choice8 = input("""Their is a fearsome champion who is very skilled swordsman and a skilled wind user. He fights in the coliseum and he is the number one challenger. Would you like to challenge him now?
  A.
  B.
  
  Your Choice: """).lower()
  if choice8 == "a":
    print("")
  else:
    print("")

      

intro()
stats()
story1()
story2()
stats()
story3()
stats()
story4()
stats()
story5()