import time
charisma = 0
IQ = 50
attack = 20
defense = 20
mainScore = 10
money = 0
party = []
def stats():
  print("\nIQ = " +str(IQ))
  print("Charisma ="+str(charisma))
  print("Attack = " +str(attack))
  print("Defence = " +str(defense))
  print (mainAbility+" = " +str(mainScore))
  print("Money = " +str(money)) 
  print("Party members:")
  print(party)
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
  name = input("""What is your name player?
""")
  party.append(name)
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
  time.sleep(5)

  print("""\nYou decide that it is about time leave the orphanage and start to travel through the country to gain new skills and alies. Before leave you ask everyone to if they would join you on your quest.""")
  time.sleep(5)
  if choice1 == "a":
    print("""\nEveryone looked at each other unsure wheather to join you. But one person name Hingy agreed to join you. He was your best friend and you two train a lot with each other. You both have a total of 200 gold that you have earned through the years. You were happy to have a companion and set off to a city called Fargu.""")
    party.append("Hingy")
    charisma += 20
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
    time.sleep(2)
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
      time.sleep(2)
#Low IQ options
  while IQ < 80:
    choice2 = input("""\n    A. Decline his offer?
      
    B. Take the book this book may give you new magical ability.

Your Choice: """).lower()
    time.sleep(2)
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
      time.sleep(2)
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
  time.sleep(3)
  print("\n"+name+": Hey who are you?!")
  time.sleep(1)
  print("""\nWarrior: "I'm Bani, what do you want?" *Casually floating water in his right hand*""")
  time.sleep(3)
  print("\n" +name+": Hey I'm "+ str(name) + """, and I need your help. Can you team up with me? We need to kill the King before he has full control of our nation.""")
  time.sleep(3)
  print("""\nBani: Kill the king you say? Why do you need my help?""")
  time.sleep(1)
  print("\n"+name+ """: Because you're one of a few people I'm going to find here and I see you have water powers so we can combine our powers to fight through this""")
  time.sleep(3)
  print("""\nBani: The king is someone to not be underestimated. He has a whole army by his side.""")
  time.sleep(3)
  print("""\nMy brother is part of his army. The king has his daughter captive in the next country 3 weeks away.I want you help me save her after we kill the king?""") 
  time.sleep(3)
  print("\n"+name+""": I will save your niece after killing the king""")
  time.sleep(2)
  print("""\nBani: Now I must ask you a few questions to test your knowledge. If you are able to answer them correctly I will join you.""")
  time.sleep(3)
  print("\n"+name+""": OK. What are your questions.""")
  time.sleep(1)
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
    party.append("Bani")
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
  choice6 = input("""\nWe have a month of time to kill, what do you want to do to pass the time? Somthing productive."

  A. Go to library
  B. Go to bed
  C. Train in courtyard
  D. Go to party

  Your Choice: """).lower
  time.sleep(2)
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
      attack += 10
      defense += 10
      break
    elif choice6 == "d":
      time.sleep(2)
      print("""\nYou went to a party and you became more socially active and made a friend named Baolue. He is also a warrior in training with earth abilities. His family has history with the king, his sister got killed in a crossfire within their disputes. He lost his grandfather from battling the king. He agreed to join your side on defeating King Waes.""")
      charisma += 20
      break
    else:
      choice6 = input("Invaid response. Select one of the choices.").lower()
      time.sleep(2)
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
  if charisma == 0: 
    print("\nYou feel hungry so you decide to head to a nearby diner.")
  elif charisma == 20:
    print("""\nYou feel hungry so you decide to head to a nearby diner with your party member.""")
  else:
    print("""\nYou feel hungry so you decide to head to a nearby diner with your party members.""")
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
    C: Kick in the groin
  
Your Choice: """).lower()
    time.sleep(2)
    break
  while IQ > 80:
    choice7 = input("""How should I start my first attack?
    A: Hard punch
    B: Flying kick
    C: Kick in the groin
    D: Attack him with your """ + mainAbility+ """ ability. Swords can't block magic
    
    Your Choice: """).lower()  
    time.sleep(2)
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
      print("""\nYou attack him with your """ +mainAbility+ """ ability. He trys to block it with his sword. But fails. He is blown back by your attack.""")
      break
    else:
      choice7 = input("Invalid response. Select one of the choices").lower()
      time.sleep(2)
  while choice7 != "d":
    print("""\nYour attacks failed Yasen puts a bandana on his head the arua around him turns dark and serious. He positions his 4 sword in the shape of a square. He vanishes into thin air. You feel a sharp pain he struck you in the stomach.""")
    time.sleep(3)
    print("\n"+name+""":GAHHHH!!!
 You feel like your ribs just broke.""")
    time.sleep(3)
    print("""\nYasen: I hit you with the back of my swords. Come back when your stronger.""")
    time.sleep(3)
    break
  while choice7 == "d":
    print("""Yasen: You have bested me I will join your effort to defeat the king. """)
    party.append("Yasen")
    charisma += 20
    attack += 10
    defense += 10
    break
  time.sleep(4)
def story6():
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  choice8 = input("""\nThere is a fearsome champion who is a very skilled swordsman and a skilled wind user. He fights in the coliseum and he is the number one challenger. The winner wins 1000 gold. Would you like to challenge him now?
  
  A. Yes, I'm going to challenge him.
  B. No, I'll pass. I am not ready right now.
  
  Your Choice: """).lower()
  while choice8 != "a" and choice8 != "b":
    choice8 = input("Invaid response. Please choose A or B.").lower()
  time.sleep(2)
  while choice8 == "a" or choice8 == "b":
    if choice8 == "b":
      print("""\nYou choose not to fight in the the coliseum and continue your journey """)
      time.sleep(4)
      print("\n")
      break
    else:
      print("""\nThe next fight starts tommorow I should get some rest for the fight""")
      time.sleep(2)
      print("\n*The next morning*")
      time.sleep(2)
      print("\nI walked with a serious attitude with the swordsman accross me as the crowd roars.")
      time.sleep(2)
      print("\n"+name+""":What is your name?""")
      time.sleep(2)
      print("""\nChampion:My name is Yawg.""")
      time.sleep(2)
      print("\n"+name+""":I'm """+name+"."  )
      time.sleep(2)
      print("\nYawg:I don't care.")
      time.sleep(2)
      print("""\nReferee:"Ok I want a fair fight, first man who gets knocked out, loses. Ready, On my gun shot.""")
      time.sleep(2)
      print("\n3")
      time.sleep(1)
      print("2")
      time.sleep(1)
      print("1")
      time.sleep(1)
      print("BANG!")
      choice11 = input("""\nThe fight begins, What is your first move?

  A. Attack with your """+mainAbility+""" ability
  B. Intimmidate the swordsman and wait for him to make the first move.
  C. Charge at him and punch him.
  D. Throw sand in his eyes

  Your choice: """).lower()
      while True:
        if choice11 == "a":
          print("""\nYou start swirling up a ball of """+mainAbility+""" and blast it at him.""")
          time.sleep(2)
          print("\nThe blast hits him but he stands there unphased.")
          break
        elif choice11 == "b":
          print("""\nBring it on punk!!! I'll let you go first.""")
          time.sleep(2)
          print("\n*Yawg charges at you as you try running away*")
          time.sleep(2)
          print("\n*but he catches up to you and slashes you in the face with his sword*")
          break
        elif choice11 == "c":
          print("""\nAHHHHHHHHHHH *he dodges your punch and counter attacks you with an uppercut*""")
          break
        elif choice11 == "d":
          print("""\nYou throw sand in his eyes and starts to flaring his sword around. You go behind him and snach his sword.""")
          time.sleep(2)
          print("""\nYawg: That was a dirty trick.""")
          time.sleep(2)
          print("\n"+name+""": I dont care, cry about it.""")
          time.sleep(2)
          break
        else:
          choice11 = input("\nInvaid response. Please choose A, B, C, or D").lower()
      time.sleep(2)

      while choice11 == "d":
        print("\n"+name+""": You start taunting him with his sword and he starts looking all scared.""")
        choice12 = input("""\nI need to prepare for the next attack. What should I do:
  A. Wait for him to attack and block his attack with the sword.
  B. Play dead
  C. Offer him money to win.
  D. Slash him with your sword
        
  Your choice: """).lower()
        break
      while choice11 == "d":
        if choice12 == "a":
          print("""\nYawg creates a torrnado and you try to  block it but it fails. You get blowned across the coliseum and slam your head against the wall.""")
          time.sleep(3)
          battle = "Lose"
          break
          print("\nYou lose the match and Yawg wins")
          time.sleep
        elif choice12 == "b":
          print("""\nYou play dead. He doesn't fall for it and punches you in the gut and you get knocked out.""")
          battle = "Lose"
          break
        elif choice12 == "c":
          print("""\nYou offer him money to lose the fight on purpose. He feels insulted and blows a gust of wind at you and it throws you to the wall and you get knocked out.""")
          battle = "Lose"
          break
        elif choice12 == "d":
          print("""\nYou slash him in the face with the sword and he falls to his knees.""")
          time.sleep(2)
          print("""\nYou are about to slice his head but he starts beging for his life.""")
          time.sleep(2)
          print("\n"+name+":Either surrender now, or I'll kill you.")
          time.sleep(2) 
          print("\nYawg: I surrender.")
          time.sleep(2)
          print("\n*Yawg gets up and walks out of the coliseum*")
          battle = "win"
          break
        else:
          choice12 = input("""\nInvalid response. Please choose A, B, C, or D""").lower()
      while choice11 == "a" or choice11 == "b" or choice11 == "c":
        print("""\nYour attack failed. Prepare for a counterattack.""")
        choice12 = input("""\nI need to prepare for the next attack. What should I do:
  
  A. Wait for him to attack and dodge
  B. Play dead
  C. Offer him money to win.
  D. Beg for forgivness
        
  Your choice: """).lower()
        break
      while choice11 == "a" or choice11 == "b" or choice11 == "c":
        battle = "Lose"
        if choice12 == "a":
          print("""\nYou end up getting hit with a second attack and fail to recognize that one and get knocked out""")
          break
        elif choice12 == "b":
          print("""\nYou play dead. He doesn't fall for it and punches you in the gut and you get knocked out.""")
          break
        elif choice12 =="c":
          print("""\nYou offer him money to lose the fight on purpose. He feels insulted and blows a gust of wind at you and it throws you to the wall and you get knocked out.""")
          break
        elif choice12 == "d":
          print("""\nYou beg for your life and he laughs""")
          time.sleep(2)
          print("""\nHe begins to punch and kick you until you lose conciousness""")
          break
        else:
          choice12 = input ("""Invalid response. Please choose A, B, C, or D.""").lower()
        time.sleep(3)
      if battle == "win":
        print("""\nYou leave the coliseum and Yawg is chasing after you""")
        time.sleep(2)
        print("""\nYawg: That was some fight in there. where are you heading next.""")
        print("\n"+name+""": My goal is to defeat King Waes to liberate the people of Vextop.""")
        print("""Yawg: I will be honored to join you. Since defeated me, I shall now be your sword in battle.""")
        print("\n"+name+"""You will be a great addition to my party. Let patch up our wounds and get some rest""")
        print("\nYawg: Alright captain!")
        party.append("Yawg")
        charisma += 20
        attack += 20
        defense += 20
        IQ += 10
        time.sleep(2)
      else:
        print("""\nYou lost the fight and go back home to heal my wounds and get some rest.""")
      break  
          
def story7(): 
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  print("""After dealing with all those fighters you decide to take a rest under a tree in a nearby forest.""")
  time.sleep(2)
  print("""\n*bushes rustle behind you*""")
  time.sleep(2)
  print("""\nYou get up quickly and look around you. Theres something in the bush.""")
  time.sleep(2)
  print("""\nA wolf jumps out of the bushes.""")
  time.sleep(1.5)
  print("""\nWolf: What are you doing in my forest?""")
  time.sleep(1.5)
  print("\n"+name+""":HOLY SHIT A TALKING WOLF!""")
  time.sleep(2)
  print("""\nWolf: Calm down. My name is wolf. I was cursed by a magic user. I was once a general in king waes army. He was walking down the stairs while I was walking up and I blocked his way. He got one of his magic users to turn me into a wolf.""")
  time.sleep(2)
  print("""\nI ran away into the forest and never looked back. I miss my family.""")
  time.sleep(2)
  print("\n"+name+""": Woah I didnt know that kind of magic existed.""")
  time.sleep(2)
  print("\n"+name+""": Actualy we are on our way to defeat the king. Do you want to join us?""")
  time.sleep(2)
  print("""\nWolf: We just met, how could I trust you?""")
  time.sleep(2)
  choice9 = input("""\nI need to get the wolf's trust. I should:
  
    A: If we defeat the king we can help remove your curse.
    B: We have the same goal lets defeat the king.
    C: I will fight you if you dont join us.
  
  Your choice: """).lower()
  while True:
    if choice9 == "a":
      print("""\nWolf: Wait really? You can really help me remove the curse? Thank you. I will join your team.""")
      party.append("Wolf")
      charisma += 20
      IQ += 20
    elif choice9 == "b":
      print("""\nWolf: It is true we have the same goal but I dont want to risk my life.""")
    elif choice9 == "c": 
      print("""\nWolf: Its pointless to fight me I still wont join you.""")
    else:
      choice9 = input("Invaid reponse. Please choose A,B or C.").lower()
    break
def story8():
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  print("""We are almost ready to face the king, we are setting a plan of a attack 1 month from now.""")
  time.sleep(3)
  choice10 = input("""What are you guys planning to do for the first 3 weeks?
    A. Train as a team
    B. Go to a stripclub
    C. Research battle tactics
    D. Buy a new spellbook 
    
Your Chioce: """).lower()
  time.sleep(2)
  while True:
    if choice10 == "a":
      print("""Great, You and your party will go to a courtyard in Fargu""")
      attack += 10
      defense += 10
      break
    elif choice10 == "b":
      print("""Nice, you can go there and start twerking with your team.""")
      break
    elif choice10 == "c":
      print("""You guys can go to library and read books on battling and how to use teammwork.""")
      IQ += 15
      break
    elif choice10 == "d":
      print("Great, you can buy a spellbook from a magical workshop.")
      mainScore += 20
    else:
      choice10 = input("Invaid response. Please choose A, B, C or D.").lower()
  print("After a long journey, me and my party are set to defeat King Waes once and for all and give the citizens freedom and stop the unequal treatmeant of the social classes.""")
  time.sleep(3)
  print("\nWe all get our gear ready and we walk to his kingdom.")
  time.sleep(2)
  print("\n*You are about to give a speech to your team*")
  time.sleep(2)
  print("\nWE TRAINED LONG AND HARD FOR THIS DAY TO COME.")
  time.sleep(2)
  print("\nOUR POWERS WILL BE THE ONLY WAY WE CAN DEFEAT KING WAES.")
  time.sleep(2)
  print("\nKING WAES CANNOT GET AWAY WITH HIS CRIMES TOWARDS THE LOWERCLASS.")
  time.sleep(2)
  print("\nWe set out for the attack")
  time.sleep(4)
  
def story9():
  global charisma
  global IQ 
  global attack
  global defense 
  global mainAbility
  global mainScore
  global money
  global name
  print("We have arrived at the kings royal palace.")
  time.sleep(2)
  print("Our plan of attack is to blast through the palace gates.")
  time.sleep(2)
  print("\n" + name + """: KING WAES, WE ARE HERE TO TAKE YOUR HEAD AND BRING A END TO YOUR TYRANNY!""")
  time.sleep(2)
  print("King Waes takes his crown off, and gets his sword from his rack.")
  time.sleep(2)
  print("He walks out of his palace with his sword.")
  time.sleep(2)
  print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⣶⣶⣶⣶⣾⣿⣿⣿⣶⣶⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣄⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⣀⣠⣴⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⣿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠤⠤⠤⠄⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣁⣀⣀⣀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⠀⠀⡜⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠃⠈⠀⠀⢡⠸⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠙⠛⠛⠉⠉⠁⢀⠄⠀⠀⠘⢀⠈⠛⠛⠛⠛⠉⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⢠⡉⠒⠢⡠⠔⠈⣑⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⢸⠰⣿⣿⣿⢿⢾⣿⣿⣿⡷⠁⠄⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⢸⠀⠍⠈⠀⠒⠒⠒⠒⠒⠂⠘⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠦⢤⣀⣀⣀⣀⡠⠤⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
  print("King Waes: You challenged me you commeners. I will show you true power to you peasents.")
  time.sleep(2)
  print("""I can hear the country's citizens voices in the background cheering us on.""")
  time.sleep(2)
  print("""It gave me more confidence, I feel powerful. I will do anything to take hm down once an for all.""")
  time.sleep(2)
  print("""*deep staring each other*""")
  time.sleep(2)
  print("I'll make the first move.")
  time.sleep(2)
  choice11 = input("""How do you start your first attack?
  
  A. Run for your life.
  B. Go for the first swing with your sword.
  C. Let him make the first move.
  D. Use your""" +mainAbility + """ability on him.
  
    Your choice: """).lower()
  while True:
    if choice11 == "a":
      print("\nYou exit the courtyard and make a run for it.")
      time.sleep(2)
      print("""\nKing Waes: Never turn your back to the enemy in a fight!""")
      time.sleep(2)
      print("""\nKing Waes throws his sword and it goes through your heart killing you.""")
      time.sleep(3)
      print("""\nYour party sees you dead on the floor. They all scream and run as they panic.""")
      time.sleep(2)
      print("\nKing Waes laughs as he kills all of the party members one by one.")
      time.sleep(2)
      print("""\nBad choice. You died as a coward. You failed to kill the king and died with disgrace.""")
      break
    elif choice11 == "b":
      print("\nYou swing your sword. Your sword clashes with his sword.")
      time.sleep(2)
      print("\n*staring at each other intensly*")
      time.sleep(2)
      print("\n"+name+": You think you can get away with this, all these people are in a state of sorrowness because of you and and they aren't even supporting you.")
      time.sleep(4)
      print("\nKing Waes: I don't need a lecture from you. I am the king. My power is absolute!")
      time.sleep(2)
      print("\n"+name+": We'll see about that!")
      break
    elif choice11 == "c":
      print("""\nHe charges at you. You brace for impact but despite your strong stance, he knocks you to the ground.""")
      time.sleep(2)
      print("""\nKing Waes: Foolish of you to let the enemy make the first move. You should have made your move when you had the chance.""")
      time.sleep(2)
      print("""\n*King Waes kicks you in the side and breaks your ribs*""")
      time.sleep(2)
      print("\n"+name+""": Foolish you say? I think not.""")
      time.sleep(2)
      print("""\n*You stab King Waes in the foot with your sword.*""")
      break
    elif choice11 == "d":
      print("\nYou start winding up a ball of"""+mainAbility+" and blast it at him and he stands there. Unfazed!")
      time.sleep(2)
      print("""\nKing Waes: Did you really think such a puny attack will damage me!""")
      time.sleep(2)
      print("\n"+name+""": Damn. How is he so strong!""")
      break
    else:
      choice11 = input("Invaid repsonse. Please pick A, B, C, or D.").lower()
  while choice11 != "a":
    time.sleep(2)
    print("I need to plan a conunter attack.")
    time.sleep(2)
    print("My party is fighting the guards. Maybe they can lend a hand")
    time.sleep(2)
    choice12 = input("""What should our next move be?
A. Ask a party member for help
B. Fight the King to buy time for your party to arrive
C. Secretly tell one of your party members to disguise as a guard                      
D. Flip the script

  Your Choice: """).lower()
    break
  while choice11 != "a":
    if choice12 == "a":
      print("\n"+name+ ":Hey "+party[1]+"""Can you lend a hand?""")
      time.sleep(2)
      print("\n"+party[1]+"""Sure thing.""")
      time.sleep(2)
      print("\nWith "+party[1]+""" help, we was able to get a slash across his face.""")
      time.sleep(2)
      print("""\nKing Waes: You annoying little monkeys. Where are my guards.""")
      time.sleep(2)
      print("""\nYou are surrounded by guards. You removed """+party[1]+ """ from his posion and now you are out numbered.""")
      time.sleep(2)
      print("""You are asking for help form the other party members but they are busy and king Waes and the guards attack at once and he was able to slice bith of your heads at the same time.""")
      time.sleep(4)
      print("""Soon, King Waes was able to kill the rest of your army and you and your party are dead.""")
      time.sleep(2)
      print("""You lost because you were foolish. Every party member has a role and removing"""+ party[1]+ """from his post caused your entire team to crumble.""")
      break
    elif choice12 == "b":
      print("""\nKing waes: This is all futile. You will never be able to take down my army.""")
      time.sleep(2)
      print("""\nYou are all nothing but ants beneath my feet.""")
      time.sleep(2)
      print("\n"+name+""": I dont care what you say. People are supposed to be equal and free.""")
      time.sleep(2)
      print("""\nKing Waes: NONSENSE!""")
      time.sleep(2)
      print("""\n*You dash at him to attack with your sword*.""")
      time.sleep(2)
      print("""\nKing waes: That wont work.""")
      time.sleep(2)
      print("""*King Waes dodges your attack and kicks you to the ground*""")
      break
    elif choice12 == "c":
      print("\n"+name+ ":Hey "+party[1]+" take a dead guards armor and stay near the king.")
      time.sleep(2)
      print("""Incase anything goes wrong ambush him.""")
      break
    elif choice12 == "d":
      print("""*You charge at him and keep fighting with all your might*""")
      time.sleep(2)
      print("""*Swinging, dodging, slashing each other with your swords until a moment when you swords clash again*""")
      time.sleep(2)
      print("\n"+name+": I'll do anything to protect this kingdom! My parents left me as baby and I have to do this for my own legacy!""")
      time.sleep(3)
      print("""\n*You keep fighting until you swing you sword upward toward his neck area and you see a necklace fall out*""")
      time.sleep(2)
      print("""\n*You realize it is the same necklace that you're wearing*""")
      time.sleep(2)
      print("\n"+name+": Wait! Where did you get this?")
      time.sleep(2)
      print("""\nKing Waes: You were born in this kingdom and we grant necklaces to every new Kingdom family member. ...because I am your father. You were taken away to an orphanage.""")
      time.sleep(2)
      print("\n"+name+": And my mom?")
      time.sleep(2)
      print("""\nKing Waes: Your mother died giving birth to you.""")
      time.sleep(2)
      print("""\n*You pull out your necklace from under your cloak and just stand there in shock*""")
      time.sleep(2)
      print("\n"+name+""": Then why do do you have all of these Kingdom people do cheap labor?""")
      time.sleep(2)
      print("""\nKing Waes: I felt very depressed that you were taken away to an orphanage and I fell into a state of evil power because of this depression.""")
      time.sleep(2)
      print("\n"+name+":So what now?")
      time.sleep(2)
      print("""\nKing Waes: Come with me son.""")
      time.sleep(2)
      print("""\nWe can change this Kingdom to a better place again. Let's do this for your mother.""")
      time.sleep(2)
      print("""Yes, for mom.""")
      time.sleep(2)
      print("""*You guys hug it out and start the next chapter of this Kindom.""")   
      break
    else:
      choice12 = input("""Invaild response. Please choose A, B, C, D.""").lower()
  while choice12 == "b":
    time.sleep(3)
    print("""\nWe need to make one final push. This last attack needs to kill the king.""")
    choice13 = input("""What should our last attack be:
A. Attack all at once with physical attacks.
B. Concentrate all of your party's magical power into one big blast.

  Your Choice: """).lower()
    break
  while choice12 == "c":
    time.sleep(3)
    print("""\nWe need to make one final push. This last attack needs to kill the king.""")
    choice13 = input("""What should our last attack be:
A. Attack all at once.
B. Concentrate all of your party's magical powers into one big blast.
C. Tell """+party[1]+""" to ambush the king.

  Your Choice: """).lower()
    break
  while choice12 == "b" or choice12 == "c":
    if choice13 == "a":
      print("""\nYou all gather in front of the king to deliver a final blow""")
      time.sleep(2)
      print("""King Waes: What a foolish idea you all gathered in one spot.""")
      time.sleep(2)
      print("""King Waes charges a huge ball of magical energy in mere seconds and obliterates your entire team.""")
      time.sleep(2)
      print("""Your quest to free the kingdom failed.""")
      time.sleep(2)
      print("""King Waes evil family continues to rule the kingdom for years to come.""")
      break
    elif choice13 == "b":
      print("""*We start charging up and massive blast with all of our powers combined*""")
      time.sleep(2)
      print("*But you guys fail to control your powers into this blast and it ends up overcharging and blasting you all to your death*")
      time.sleep(3)
      print("In memory of "+party+".")
      time.sleep(2)
        
      break
    elif choice13 == "c":
      print("""King Waes: I have already won this fight. I will kill you with my explotion magic.""")
      time.sleep(2)
      print("""\nGuard: King Waes there is an enmergency.""")
      time.sleep(2)
      print("""\nKing Waes: I am busy. What is it!""")
      time.sleep(2)
      print("""Guard: look at this, *The guard stabs him*""")
      time.sleep(2)
      print("""\nKing Waes: what is the meaning of this.""")
      time.sleep(2)
      print("""\nThe guard takes off his mask and it was """+party[1]+""".""")
      time.sleep(2)
      print("\n"+party[1]+""": Go to hell!""")
      time.sleep(2)
      print("""\nKing Waes: That was a dirty trick. It seems that I am going to die because the knife is poisoned.""")
      print("""\n"""+name+""": Good bye King Waes. I will make sure that the kingdom is safe in m hands""")
      time.sleep(2)
      print("""\nThe king dies and ou and your party are seen as heros. You celebrate through the night with the towns people for the death of the king and for becoming the new ruler.""")
      time.sleep(2)
      print("""\nCongratulations! You were able to defeat the king.""")
      break
    else:
      choice13 = input("""Invalid respose. Please choose A, B, C, D.""")

  time.sleep(2)
  print("The End! Thanks for playing.")


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
stats()
story6()
story7()
stats()
story8()
stats()
story9()
