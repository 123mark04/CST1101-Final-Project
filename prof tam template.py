#Imports
import time

#Initialization of all the variables in the game
creativity = 50
leadership = 50
sociability = 50
tact = 50
page = 0

#The stats() is called at the beginning of each new part of the story where the user's choice will effect them.
def stats():
    global creativity
    global leadership
    global sociability
    global tact
    choice = input("Do you want to view your stats? Y/N")
    while (choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n'):
        if (choice == 'Y' or choice == 'y'):
            print ("+=========Stats==========+")
            print ("|       Creativity: " , creativity, " |")
            print ("|       Leadership: " , leadership, " |")
            print ("|       Sociability: " , sociability, " |")
            print ("|       Tact: " , tact, " |")
            print ("+==========================+")
            break
        elif (choice == 'N' or choice == 'n'):
            print ("Okay. Continuing with the program.")
            break
            
#The endStats() is only called when the user reaches one of the 4 endings.
def endStats():
    global creativity
    global leadership
    global sociability
    global tact
    print ("+=========Stats==========+")
    print ("|       Creativity: " , creativity, " |")
    print ("|       Leadership: " , leadership, " |")
    print ("|       Sociability: " , sociability, " |")
    print ("|       Tact: " , tact, " |")
    print ("+==========================+")

#Displays the name of the game and the creator at the beginning
def credit():
    print ("Title: Running Late")
    print ("Author: Tamrah Cunningham")

#After each section(paragraph) of text, it will be followed by a pageNumber in order to simulate a new page of the story
def pageBreak(pageNum):
    print ("======= Page %d ======" % pageNum)
    pageNum += 1

#The generic ending of the game. This runs at the end of all endings. This allows users to see their final stats
# And let them know that they reached the end of the program and it will automatically terminate at the end.
def theEnd():
    global creativity
    global leadership
    global sociability
    global tact
    print("+==========================+")
    print("|        The End!          |")
    print("|    Thanks for playing!   |")
    print("+===========================+")
    choice = input("Do you want to view your final stats? Y/N")
    while (choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n'):
        if (choice == 'Y' or choice == 'y'):
            endStats()
            print("You can close the program now.")
            break
        elif (choice == 'N' or choice == 'n'):
            print("Ok. Feel free to close the program now.")
            break
        else:
            choice = input("Do you want to view your final stats? Y/N")
    time.sleep(2)
    quit()    

#This ending comes into play when the user fails to accomplish their end goal
def badEnd():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    page += 1
    pageBreak(page)
    print("""This whole day was a waste. Maybe you should've stayed home and slept the day away. At least in your dreams, as the lord of a country, you could've commanded the people to forfeit what they bought as tithes. Then none of this would ever be a problem.\n\n""")
    page += 1
    time.sleep(1)
    pageBreak(page)
    print ("Next time, you decide to yourself, you should just shop online.\n\n")
    theEnd()

#This ending comes into play when the user reaches their end goal in a unique way
def strangeEnd():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    page += 1
    time.sleep(1)
    pageBreak(page)
    print ("""As you exit the store, you see a few cop cars and an ambulance parked in front of the store. As you watch a few people get carted off due to injuries or for resisting arrest, you realize that maybe, you should have suggested something tamer to scare off the crowd. Maybe a rodent infestation?\n\n""")
    page += 1
    time.sleep(1)
    pageBreak(page)
    print ("""As you ponder this, someone points you out and a cop walks up to you, wanting to question you. You sigh to yourself as you prepare to think of another way to get out of this mess.\n\n""")
    print ("""...Maybe you should suggest parley?\n\n""")
    theEnd()

#This ending come into play when the user accomplishes their end goal
def goodEnd():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    page +=1
    time.sleep(1)
    pageBreak(page)
    print ("""You are the first to touch the brand new pair of Louis Vuitton and the price made you buy 3 pairs and then some. Also some matching shirts and shoes. The prices are ridiculous and you can't help but splurge. You leave the boutique in good spirits!\n\n""")
    page +=1
    time.sleep(1)
    pageBreak(page)
    print ("""As you enter your room with your arms loaded with bags of goodies, you smile to yourself and give yourself a mental pat on the back. You almost missed out on it, but you finally did get what you wanted and that made today such a perfect day.\n\n""")
    print ("""Now maybe, when you go to sleep, you can dream again of being a lord of a country. You think you have a knack for it.\n\n""")
    theEnd()

#Starting from here, this is where the story takes shape. Starting from dreamSequence(), each function is a new part of the story
#For the most part, the story progression is linear. 
def store():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    stats()
    page +=1
    time.sleep(1)
    pageBreak(page)
    print ("""The store is a small boutique that is in the corner of the mall and is hard to see from the entrance. You notice a lot of people gathering outside the small shop, which is not what you want to see at all. \n\n""")
    page +=1
    time.sleep(6)
    pageBreak(page)
    print ("""Voices are shouting from all over as people are anxious for the shopping bonanza to start. It is absolute mayhem. Do you have a course of action?\n\n""")
    print ("A.)Use your leadership to appeal to the masses")
    print ("B.)Use your active imagination to cause a diversion")
    print ("C.)You can't handle the population!")
    print ("D.)Your mother raised you to be patient")
    choice = input("So, what is your course of action?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice != 'D' or choice != 'd'):
        if (choice == 'A' or choice == 'a'):
            if (leadership >= 70):
                print ("""With a strong voice (and an imaginary soap box) you command everyone's attention. 'My fellow shoppers! We all came here to get one thing and one thing only! And that is the best prices of the season!' The crowd quiets down as they listen to you. And you feel that you are on the right path.\n\n""")
                print ("""'So, if we want this to be a glorious day, line up in an orderly fashion so that we can all get in and get out!' Hmm...sounds illogical and highly idealistic that you believe that people would listen to you.\n\n""")
                page +=1
                time.sleep(6)
                pageBreak(page) 
                print("""But shockingly enough, the crowd thinks that you are probably an undercover cop. Which works for you. So playing it up, you shimmy your way to the front of the line in order to pretend to be maintaining the peace. And when the clock strikes 11, the doors open and you are the first one in. Fantastique!\n\n""")
                goodEnd()
            else:
                print ("You are not the type of person these people would listen to.\n\n")
                store()
        elif (choice == 'B' or choice == 'b'):
            if (creativity >= 70):
                print ("""'Hey guys! The store next door is doing an event where if you catch the workers, you can get a $1000 gift card!\n\n'""")
                print ("""'Seriously!?' Someone in the crowd shouts. You shout out an affirmative and pretend to prepare to run over to the store. The crowd takes that as their cue to make a run for it and they all chase each other into the store next door...Leaving you all alone.\n\n""")
                page +=1
                time.sleep(6)
                pageBreak(page) 
                print ("""When the clock strikes 11, you walk into the store and calmly browse around. As you are picking up the latest name brand jeans, you hear the sounds of sirens and absolute mayhem in the store next door. Lucky for you I suppose.\n\n""")
                strangeEnd()
            else:
                print ("You thought and you thought, but nothing came to mind.\n\n")
                store()
        elif (choice == 'C' or choice == 'c'):
            if (sociability < 50):
                print ("""You can't deal with so much people. It's too much. The noise. The touching. The possible interaction? Nope! Nuh uh! You turn right back around and hop on the bus. It's not too much of a hassle to shop online. You actually prefer it. Dealing with people in the end, is just too much of a hassle.\n\n""") 
                time.sleep(2)
                badEnd()
            else:
                print ("You will not cower to such forces.\n\n")
                store()
        elif (choice == 'D' or choice == 'd'):
            print("""You decide to wait patiently admist the chaos and hope that the store opens soon so you can shop to your hearts content. As if some time deity was listening to you, the clock strikes 11 and the store opens. You wait until the crowd diminshes and then walk in. Only to see that, like a hoard of ravenous locusts, the crowd has picked up everything! How cruel!\n\n""") 
            time.sleep(2)
            badEnd()
        else:
            choice = input("You came out all this way. You got to do something.")     

def mall():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    page +=1
    time.sleep(2)
    pageBreak(page)
    stats()
    print ("""Your bus pulls up at the curb across the street from the Atlantic Terminal. As usual, traffic is heavy as multiple buses are pulling up to the same stop and dozens of people are shoving their way to the  nearest entrance. To your left, you hear a conversation between a couple talking about the latest debate. To your right, a group of girls talking about a sale.\n\n """)
    time.sleep(2)
    print ("'The sale starts at 11. And all the designer clothes will be 70% off. Do you know how cheap that is!?'\n\n")
    time.sleep(2)
    print ("'I know! I'm totally buying the brand new season of Louis Vuitton. You know the one.'\n\n")
    time.sleep(2)
    print ("""Your mind blanks as you hear these girls. They seem to be talking about the very same sale that you are going to. Even the very same Louis Vuitton! You tap your foot incessantly, hoping that the crosswalk finally changes and when it does, you take off across the street, weaving through the crowd and shoving your way inside the mall.\n\n""")
    page +=1
    time.sleep(6)
    pageBreak(page)
    print ("""Once in, you run straight towards the escalator and now, it is the long wait for the second floor. What do you do to occupy your time?\n\n""")
    print ("A.)Bounce on your heels")
    print ("B.) Sing a song")
    print ("C.)Complain loudly")
    choice = input("So, what do you do?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c'):
        if (choice == 'A' or choice == 'a'):
            print ("""You bounce on your heels as you wait for your floor. You know the man behind you is looking at you like you are crazy, but you don't care. With a city this big, there is no way that you will run into this guy again.\n\n""")
            print ("Finally! You're here!\n\n")
            time.sleep(3)
            break
        elif (choice == 'B' or choice == 'b'):
            print ("""You whistle a tune from a song that was recently was stuck in your head. Once you whistle the intro, you start singing the lyrics. You know the man behind you is looking at you like you are crazy because the song that you are singing is in Japanese with heavily accented English words in between, but you don't care. With a city this big, there is no way that you will run into this guy again.\n\n""")
            print ("Finally! You're here!\n\n")
            creativity += 10
            time.sleep(3)
            break
        elif (choice == 'C' or choice == 'c'):
            print ("""You start to loudly complain about the fact that there is space on a few steps and that people should start walking up the escalator. People in front of you shoot you a dirty glare, while people behind you loudly start agreeing with you. You let the newcomers add in their two cents and by the time you get off the escalator, everyone is disgruntled.\n\n""")
            print ("But thankfully, you finally arrived.\n\n")
            tact -= 10
            time.sleep(3)
            break
        else:
            choice = input("You will be on this escalator for awhile. You have to do something.")
    store()

def bus():
    global creativity
    global leadership
    global sociability
    global tact
    global page
    stats()
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("""The person who is sitting next to you seems to be staring really hard at you for unknown reason. The man, who looks to be in his late 30's continues his staring for the next minute or so. It honestly kind of creeps you out a little.""")
    print ("A.) Ask him a question")
    print ("B.) Cringe at the look and huddle in on yourself")
    print ("C.) Glare right back at them")
    print ("D.) Think up a story")
    choice = input("What will you do?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice != 'D' or choice != 'd'):
        if (choice == 'A' or choice == 'a'):
            print ("""'Can I help you?' You ask when you finally get tired of the man. Instead he just stares at you again. Well so much for that. You try to ignore him again, but after 5 minutes, you break once more.\n\n""")
            page +=1
            time.sleep(2)
            pageBreak(page)
            print ("""You politely ask him why he is staring at you. The man, at first, doesn't respond. You repeat the question and he startles slightly before standing up and moving to another seat.\n\n""")
            print ("...You're not really sure how to take that.\n\n")
            time.sleep(2)
            break
        elif (choice == 'B' or choice == 'b'):
            if (sociability < 50):
                print ("""You invoke the move you dubbed the 'Hidden Turtle' and huddle in on yourself. If you collapsed even more upon yourself, you would implode. The man seems shocked at this defensive move, offers you an awkward grimace and looks the other way./n/n""")
                time.sleep(2)
                print ("""Great! You made yourself look so awkward that you scared off someone who seems to be as awkward, if not more so than you. Good job. \n\n""")
                sociability -= 20
                time.sleep(2)
                break
            else:
                print ("You are a little more sociable than that.")
                bus()
        elif (choice == 'C' or choice == 'c'):
            if (tact < 50):
                print ("""Well two can play at this game. You straighten your back, take a deep breath and unleash your most potent glare ever. People quake under the intense stare that seems to reprimand them for even existing and it seems to be working for this man. As soon as he looks into your eyes, he jumps up in fright and scurry off to the front of the bus.\n\n""")
                time.sleep(2)
                print ("""You feel inordinately pleased with yourself until you look around and see that a few people who witnessed what you did is looking at you as if you just kicked a puppy.\n\n""")
                tact -= 20
                time.sleep(2)
                break
            else:
                print ("You are more tactful than that.")
                bus()            
        elif (choice == 'D' or choice == 'd'):
            if (creativity >= 70):
                print ("""You look at the man and decide that it is best if you try to get his attention away from you. So you decide to tell him a story...\n\n""")
                time.sleep(2)
                print ("""'Man, can you believe how hard it is to catch up to a moving bus?' You start off with.\n\n""")
                time.sleep(1)
                print ("'...What?'\n\n")
                time.sleep(1)
                print ("'Yea, especially when I have to deal with a bad limp from yesterday's activity.'\n\n")
                time.sleep(1)
                print ("You smile at the man as he listens to you in confusion.\n\n")
                time.sleep(1)
                print ("""'And man that limp is something cra-zay! My friend wrecked me! Like really, really bad. Like, can you imagine a friend you trusted with your life just plowing into you with no remorse?!'\n\n""")
                time.sleep(2)
                print ("""It was at this point that the man's eyes widen and his face stares at you in abject horror. Immediately he turns to his side and pulls the cable signalling that it is his stop.\n\n""")
                time.sleep(2)
                print ("'I told him I trusted him and he did THAT to me? And now I'll be limping for who knows how long!'\n\n")
                time.sleep(1)
                print ("'I-I'm going to go now...uh, you should...get help?'\n\n")
                time.sleep(1)
                print ("""And with that, the man gets up and walks to the front of the bus, where he promptly exits. You laugh in delight, before sliding into his seat and waving at him from the window. He grimaces as he looks around and realizes that this isn't his stop and he now has to wait for another bus.\n\n""")
                creativity += 20
                time.sleep(2)
                break
            else:
                print ("You aren't creative enough to pull a story out of nowhere.")
                bus()
        else:
            choice = input("So, you're just going to ignore my question?")    
    mall()


def friend():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    stats()
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("""Once you reach your friend, Talia, she smiles jovially and shoves a flyer in front of your face. You take a step back in order to read more clearly. And you can see why she is so excited.\n\n""")
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("""There seems to be a music event being held at the nearby park that starts at 11. Now normally wouldn't care, but then you see that it is your favorite band that is playing. Wow. This changes everything. What should you do?\n\n""")
    print("A.) 'Screw Shopping!'")
    print("B.) 'But I've been waiting for this sale forever!' ")
    print("C.)'Talia, go buy what I want while I hold our spot' ")
    choice = input("What do you tell your friend?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c'):
        if (choice == 'A' or choice == 'a'):
             print ("""Between the choice of buying something on sale versus seeing your favorite band up close and personal? It's not even a choice. Forget shopping, your status as a fan is more important.\n\n""")
             time.sleep(2)
             print ("'Talia, we need to go. Like, now. We need the best spot so I can attempt to touch my living dream.'\n\n")
             time.sleep(2)
             print ("'So no shopping?'\n\n")
             time.sleep(2)
             print ("'Nope. Don't care. Let's go. Stop talking. Let's go!\n\n")
             page +=1
             time.sleep(2)
             pageBreak(page)
             print ("""With your enthusiasm launching over the recommended limit of human normalcy, you and Talia run off to meet your music idols. Maybe next time, you will get a chance to shop. But today will not be that day.\n\n""")
             time.sleep(2)
             stats()
             theEnd()
        elif (choice == 'B' or choice == 'b'):
            time.sleep(2)
            print ("""You do know that you waited for this sale for almost a year, right? You don't want to miss out on all the delectable purchases do you? Nope. This sale is too important. And besides, as a true fan, you know that you need the proper equipment to show your undying support. And you are not prepared. So with a heavy heart, you decline and decide to go shopping.\n\n""")
            time.sleep(2)
            mall()
        elif (choice == 'C' or choice == 'c'):
            if (leadership >= 70):
                print("You imperiously hold your head up high and look Talia in her eyes and demand:\n\n")
                time.sleep(2)
                print("'Talia, as your friend and pseudo leader of your life, go forth and shop for me.'\n\n")
                time.sleep(2)
                print("'What!?'\n\n")
                time.sleep(2)
                print("'You heard me. Here is my shopping list, there is your bus. I will meet you at the park. I promise to save you a spot!'\n\n")
                time.sleep(2)
                print("You push her towards the bus stop and walk the opposite direction.\n\n")
                page +=1
                time.sleep(2)
                pageBreak(page)
                print("In the end, you get to be up front and personal to your idols, completely forgetting about Talia and the things you made her buy for you.\n\n")
                stats()
                theEnd()
            else:
                print ("Your leadership is not high enough.")
                friend()

def sale():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    stats()
    print ("Time to prepare for that sale!\n\n")
    time.sleep(2)
    print ("""After locking your door, you make your way outside of your apartment and into the hazy air of the city life. The air shimmers in the heat and as you look around, you are mildly perturbed that so many people are already outside this early.\n\n""")
    time.sleep(2)
    print ("""You had hoped that being a Saturday, a lot of people would still be knocked out from partying last night. But apparently, these people had access to some coffee that woke them up. Or maybe, they heard about the sale. Well that's a no go. Those Louis Vuitton jeans belong to you!\n\n""")
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("""The morning bustle of the street is offering you no reassurance. You feel that you will not get to the sale on time, so you want to hurry, but you can't help but notice a few things...""")
    print ("A.) The commuter bus up the block")
    print ("B.) A sign advertising the sale")
    print ("C.) A woman waving frantically at you")
    choice = input("So, what caught your eye?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c'):
        if (choice == 'A' or choice == 'a'):
            print ("""The bus is quickly approaching the stop and you run to catch up as it pulls up. Luckily for you, you made it! But boy, that run took a lot out of you. It takes a while for you to catch your breath and as you desperately try to gulp in some of those lifesaving molecules that make up air, you look around.\n\n""")
            page +=1
            time.sleep(2)
            pageBreak(page)
            print("""The bus is, of course, as crowded as usual. There are many conversations going on, creating a constant murmur around you. You try politely shoving your way to the back where there is an empty seat. You are elated that there is a seat and you gratefully plop down. That's when you notice someone is looking at you...\n\n""")
            bus()
        elif (choice == 'B' or choice == 'b'):
            print ("""You are notably excited for this shopping trip. These types of sales only happen once in a while.\n\n""")
            print ("""The type of designer clothes that will be on sale is amazing and you can only drool at the variety of clothes you will be getting. Oh, you can't wait!\n\n""")
            page +=1
            time.sleep(2)
            pageBreak(page)
            print("""Oh, you almost missed the bus! So you leave your imagination behind and run to catch the bus. As the bus is about to pull away, you knock on the door in order to get the driver's attention. She looks at you, nods and then opens the door for you. Thanking her profusely, you push in your MetroCard, and start looking for a seat. You finally see one at the back and plop down.\n\n""")
            bus()
        elif (choice == 'C' or choice == 'c'):
            if (sociability >= 70):
                print ("""You turn your head and see that one of your friends who lives in your neighborhood is waving frantically at you. She seems extremely excited. Which you can't help but liken to a sugar crazed squirrel. But seeing as you are a busy-body, you can't help but wander over to her to see what is up.\n\n\n""")
                time.sleep(2)
                friend()
            else:
                print ("You aren't that sociable to talk to the person waving at you.")
                sale()
        else:
            choice = input("No, I'm sure one of these things caught your attention.")

def realization():
    global page
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("""Either way, you are up and the dream you had is slowly fading away. You reach on the floor to pick up your phone and turn off the alarm. Then you ponder what to do next, when the time actually catches your attention.\n\n""")
    time.sleep(2)
    print ("Oooh...it's almost 10'o'clock...Wasn't there something you were supposed to do?\n\n")
    print ("A.) Nothing")
    print ("B.) Wasn't there a sale?")
    print ("C.) Were you supposed to call someone?")
    print ("D.) Are you going to eat?")
    choice = input("So, what did you forget?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice != 'D' or choice != 'd'):
        if (choice == 'A' or choice == 'a'):
            print ("""Hmm...nothing comes to mind. So you just shove your phone under your pillow and go back to sleep. The only schedule you run on is "I'll get to it later." So, you will get to it later.\n\n""")
            page +=1
            time.sleep(5)
            pageBreak(page)
            print ("Later being 5 minutes from now.")
            realization()
        elif (choice == 'B' or choice == 'b'):
            print ("""If you recall, there was a sale at the nearby mall a couple of miles away from you. It feels like Black Friday has come early for the fashionistas of the world and you have to be a part of the once in a lifetime opportunity. You recall that the sale was going to start at 11'o'clock and you wanted to be there at the start of the sale in order to get the best. Let's mosey!\n\n""")
            time.sleep(2)
            break
        elif (choice == 'C' or choice == 'c'):
            print ("""You don't think so. After all, most of the friends you have (imaginary or otherwise) would never be awake before 10 am.""")
            time.sleep(2)
            realization()
        elif (choice == 'D' or choice == 'd'):
            print ("""You feel mild hunger pains, but it's something that you easily ignore. Though you know that eating breakfast is essential, you've trained your body to work well with a few quick bites every few hours. It isn't healthy but it's something.""")
            time.sleep(2)
            realization()
        else:
            choice = input("Hmm, no...I think you forgot one of these choices.")
    sale() 
  
def wakeUp():
    global creativity
    global leadership
    global sociability
    global tact
    global page
    stats()
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("""My Liege! Is that the best----BEEP! BEEP! BEEP!\n\n""")
    time.sleep(4)
    print ("...What?\n\n")
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("""Your body jerks up and you fling your hand to the left. You hear a dull sound as your phone hits the floor. It takes a moment to realize that, Lo and Behold, you are not the leader of a country warring with the rebels. Instead, you are...\n\n""")
    print ("A.) A lazy recluse who cringes at the outside world\n")
    print ("B.) A social busy-body who should be the leader of a country\n")
    print ("C.) A so-so type of person who can blend in the crowd\n")
    choice = input("What kind of person are you?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c'):
        if (choice == 'A' or choice == 'a'):
            sociability -= 20
            print ("""You are someone who would rather stay inside your room and let life pass you by. However, in the rare moment of activeness, you decided that you will venture outside to experience life as a human.\n\n""")
            time.sleep(2)
            break
        elif (choice == 'B' or choice == 'b'):
            sociability += 20
            leadership += 20
            tact -= 20
            print ("""You are someone who is in the know about everything. To the point that your friends make a legitimate effort to not tell you anything. Which you find rude, but that's ok. You know that they will rue the day that they didn't tell you everything.\n\n""")
            time.sleep(2)
            break
        elif (choice == 'C' or choice == 'c'):
            print ("You are nothing special, but you could be worse.")
            time.sleep(2)
            break
        else:
            choice = input("For this purpose, it'll be wise to answer with one of these choices.")
    realization()

def dreamSequence():
    global page
    global creativity
    global leadership
    global sociability
    global tact
    stats()
    page +=1
    time.sleep(2)
    pageBreak(page)
    print ("'My Liege, it is high time that you decide on the course of action that our country should take.'\n")
    time.sleep(2)
    print ('''Liege? You? You look around and see the hopeful faces of your advisors. You see that you are in the middle of a meeting, but you don't recall ever calling such a thing. Matter of fact, you don't recall much of anything at the moment.\n''')
    time.sleep(2)
    print ("'My Liege? Your response! Should we attack the rebel army in a head-on battle? Or should we attempt to parley?'\n")
    print ("A.) Attack the scums! How dare they think to rebel against me!?\n")
    print ("B.) As a benevolent ruler, I think it is best to parley.\n")
    print ("C.) Something doesn't seem right...\n")
    choice = input("What do you choose?")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c'):
        if (choice == 'A' or choice == 'a'):
            leadership += 20
            creativity += 20
            tact -= 20
            print ("""You feel a sinister smirk cross your face as you declare that your soldiers gear up and prepare for a bloodbath the likes in which they never have seen before. Your advisors look up in shocked awe as you explain the plan to them.\n\n""")
            page +=1
            time.sleep(2)
            pageBreak(page)
            print ("""You feel that as a leader, your words are absolute! All will follow your laws or suffer a bloody defeat at the hands of your soldiers. Your advisors are hesitant to listen, but they know that any objection will be answered with their blood.\n\n""")
            time.sleep(2)
            break
        elif (choice == 'B' or choice == 'b'):
            tact += 20
            sociability += 20
            leadership += 20
            print ("""You think about your options and with a kind smile, you suggest that the best course of action is to parley. After all, there must be some reason as to why the rebels are even up in arms.\n\n""")
            page +=1
            time.sleep(2)
            pageBreak(page)
            print ("""You feel that as a leader, it is your responsibility to find the best course of action in order to resolve any conflict as peacefully as possible. You abhor violence and agree that negotiation is the key. Of course, some of your more bloodthirsty advisors feel that you are too naive, you tell them that it is what a good ruler should do.\n\n""")
            time.sleep(2)
            break
        elif (choice == 'C' or choice == 'c'):
            print ("""You are baffled that this is even a problem in your life. Liege? Rebel Army? When did this ever happen? Last time you checked, there was no way that you could ever be considered royalty!\n\n""")
            page +=1
            time.sleep(2)
            pageBreak(page)
            print ("""You look around the opulent throne room filled with sensual reds and gold and then to your advisors, who for some reason, you can't see their faces...even though you know for sure that you feel their eyes on you.\n\n""")
            time.sleep(2)
            break
        else:
            choice = input("You have to choose one of these answers My Liege.")
    wakeUp()

    
#This is the start of the game.
def main():
    credit()
    dreamSequence()
main()

