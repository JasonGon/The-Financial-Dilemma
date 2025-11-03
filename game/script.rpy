# The script of the game goes in this file.

# CHARACTERS
define Ben = Character('Ben', color="#8B0000")
define Boss = Character('Boss', color="#8B8000")
define Jessica = Character('Jessica', color="#8B0000")
define Mom = Character("Jessica's Mom", color="#FFA500")
define MrB = Character('Mr. B', color="#FFFF00")
define Ruby = Character("Ruby", color="#00008B")

# The game starts here.

label start:
    #VARIABLES
    $ money_amount = 0
    $ social_bar = 2
    $ savings = False
    $ deal1 = False
    $ deal2 = False
    stop music fadeout 1.0
    pause(2.0)
    play music bgm_carpe_diem
    scene bg ben
    with fade
    "On a random day in the middle of October, I was invited over to a friend’s house for a game night..."
    scene bg benhouse
    with fade
    show ruby smile at left
    with dissolve
    Ruby "All of this tension is kind of making me hungry. Want to get pizza?"
    show ben happy at center
    with dissolve
    Ben "Sure! I’ll go order it. I think it’s $27 for two larges. In that case, can you all chip in $9?"
    show jessica nervous at right
    with dissolve
    Jessica "Yeah… About that… I don’t really have a… job yet..."
    show ben scared at center
    with dissolve
    Ben "Seriously Jess? It’s SENIOR YEAR!!! You have no money?"
    show jessica laugh2 at right
    with dissolve
    Jessica "I mean I get an allowance, but I spend it fast..."
    scene bg black
    with fade
    "After an awkward 5 minutes (that definitely felt like 10), I eventually got Ruby to pay my share in return for an alliance in the board game."
    "Once it was midnight, my friends and I parted ways. Ruby accompanied me on my walk home."
    pause(1.0)
    scene bg town2
    with fade
    show ruby angry at left
    with dissolve
    Ruby "Jess! I’m not going to keep covering for you by paying your share... You should really get in the game and apply somewhere!"
    show jessica sad at right
    with dissolve
    Jessica "Fine, but I honestly have no idea where to apply! Any suggestions?"
    show ruby normal at left
    with dissolve
    Ruby "Have you not seen all of those help wanted signs?"
    show jessica nervous at right
    with dissolve
    Jessica "I don’t have a car either..."
    show ruby laugh2 at left
    with dissolve
    Ruby "Yeah this is going to be a work in progress. I suggest you start with applying for a job. I heard from Ben that Ralph’s Pizzeria is hiring people. You could start there!"
    show jessica happy at right
    with dissolve
    Jessica "I’ve always loved pizza! It might be a fun job..."
    show ruby smile at left
    with dissolve
    Ruby "Cool! Let me know how it goes!"
    scene bg black
    with fade
    "I returned home and after a long sleep, began to write my application. By the next week, I was hired."
    "For my first day, they wanted me to bring some basic information to set up how I get paid."
    pause(1.0)
    scene bg house
    with fade
    show jessica smile at center
    with dissolve
    Jessica "Ok! I’m off to work!"
    Mom "Are you sure you got this?"
    show jessica laugh at center
    with dissolve
    Jessica "When have I ever NOT had something?"
    Mom "You almost burnt down the house last week making an omelet…"
    show jessica nervous at center
    with dissolve
    Jessica "Hehe…"
    Mom "Are you sure you've got everything?"
    show jessica happy at center
    with dissolve
    Jessica "Yep! I have my ID and my social security number."
    Mom "What about your bank account?"
    show jessica smile at center
    with dissolve
    Jessica "Do I need one for a job?"
    Mom "How else can they deposit your paycheck?"
    Mom "I’m kind of busy right now, can you go to the bank and figure it out?"
    show jessica sad at center
    with dissolve
    Jessica "Fine…"
    scene bg black
    with fade
    "After a short bike ride, I arrived at the bank."
    pause(1.0)
    scene bg office
    with fade
    show jessica nervous at left
    with dissolve
    Jessica "Hi, so I need to make an account for my job, but I have no idea how."
    show mrb normal2 at right
    with dissolve
    MrB "Ok! I can help you! Though first, you should probably understand the difference between the different accounts we offer."
    show mrb smile at right
    with dissolve
    MrB "There are 4 main types of accounts: checking, savings, money market, and certificate of deposit."
    MrB "A checking account is a short-term account used commonly for bills. A savings account is, well, an account for saving money. The money in this account will slowly grow over time."
    MrB "A money market account functions like a savings account, but can act as a checking account as well and allow for debit card purchases. The one drawback is that you are limited to 6 withdrawals or deposits a month."
    MrB "Lastly, the certificate of deposit is a savings account where you put aside money for a specific amount of time without being able to withdraw from it."
    show jessica sad at left
    with dissolve
    Jessica "Ok. That’s a lot of information… For a job, which type should I get?"
    show mrb normal2 at right
    with dissolve
    MrB "Typically, people get either a savings account or checking account. Which would you like?"

    menu:
     "What should I say?"

     "Savings account!":
         show jessica happy at left
         with dissolve
         Jessica "Savings please!"
         MrB "Great choice! Since you just want to save and have no bills to pay, you would want to go with a savings account."
         MrB "You will also recieve a bonus amount of money over time!"
         MrB "Not to break the fourth wall, but some people would say that is equal to 1 additional dollar per choice!"
         show jessica nervous at left
         with dissolve
         Jessica "Huh?"
         show mrb normal2 at right
         with dissolve
         MrB "D-Don't worry about it!"
         $ savings = True
         $ money_amount = money_amount + 1
         #Plus 1 after every choice

     "Checkings account!":
         show jessica smile at left
         with dissolve
         Jessica "Checkings please!"
         MrB "Good choice! If you ever have to pay bills in the future, you won't have to switch to a savings account!"
         $ savings = False


    "With that, I was ready to begin my job."
    scene bg black
    with fade
    stop music fadeout 1.0
    pause(2.0)

    #Event 1:
    $ money_amount = money_amount + 150
    play music bgm_montauk_point
    pause(1.0)
    scene bg town1
    with fade
    show ruby smile at left
    with dissolve
    Ruby "So you finally got a job?"
    show jessica laugh at right
    with dissolve
    Jessica "Yep! I’m earning around $150 a week!"
    show ruby laugh at left
    with dissolve
    Ruby "Want to put that money to good use?"
    show jessica laugh2 at right
    with dissolve
    Jessica "By that, I’m sure you mean something stupid."
    show ruby smile at left
    with dissolve
    Ruby "Yep! We should go shopping!"
    show jessica smile at right
    with dissolve
    Jessica "Isn’t that a little 2000s for us?"
    Ruby "Kind of, but I want to buy some new funko pops for my collection! Want to come?"
    "Hi there! It’s me, your brain! This is your first big decision in the game, isn’t it? Currently you are at $[money_amount] and have a 2/4 social bar."
    "Your social bar represents how active you are with your friends. Keeping this up might require some money spending, but don’t spend it all! Also, don’t let it drop below 0 or it's game over!"
    "Your money bar represents how much money you have. Make sure to pay attention to this! If it drops below 0, you will get a game over!"
    "Anyway, I wish you luck!"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I say?"

     "Let's do it!":
         Jessica "Let’s do it!"
         scene bg black
         with fade
         "Me and Ruby had a great time shopping. I ended up going a little overboard though and spent $40. It’s not my fault, ok? Those were really cool funko pops!"
         $money_amount = money_amount - 40
         if social_bar != 4:
             $ social_bar = social_bar + 1

     "Can't...":
         show jessica sad at right
         with dissolve
         Jessica "Sorry, but I want to start saving! Once I get more we can, ok?"
         show ruby normal at left
         with dissolve
         Ruby "Oh, alright! Cya!"
         scene bg black
         with fade
         "She didn’t seem offended, but I definitely disappointed her. I should definitely go with her next time!"
         $ social_bar = social_bar - 1

    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event 2:
    pause(1.0)
    if savings == True:
        $ money_amount = money_amount + 1
    scene bg pizza
    with fade
    show ben smile at left
    with dissolve
    Ben "Another long day… I swear these orders get more ridiculous every day!"
    show jessica nervous at right
    with dissolve
    Jessica "I agree, but where’s your employee uniform?"
    show ben happy at left
    with dissolve
    Ben "I could say the same to you. Did the art department for the game run out of budget?"
    show jessica sad at right
    with dissolve
    Jessica "Shut it! I’m sure they tried their hardest!"
    Ben "Anyway, I was thinking we could do something fun like mini golfing. I think it would cost us $25? I haven’t been in a while, so the price might have changed."
    "That does sound like fun, but I don’t know. If I save the money then I’ll have more, but if I say no, I might annoy Ben..."
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I say?"

     "Count me in!":
         show jessica happy at right
         with dissolve
         Jessica "Heck yeah! Count me in!"
         Ben "Great. Let’s go!"
         scene bg black
         with fade
         "Me and Ben had a great time, but I couldn’t say the same for my wallet. I ended up having to pay $35 to get in. I guess the price has risen since Ben last went..."
         $money_amount = money_amount - 35
         if social_bar != 4:
             $ social_bar = social_bar + 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "Sorry...":
         Jessica "Sorry, but I want to try and save up my money before spending it."
         show ben neutral at left
         with dissolve
         Ben "Oh, ok. I guess I'll see you later then."
         scene bg black
         with fade
         "It looked like he took that ok, but I looked kind of cheap. I shouldn't try to build that as my reputation."
         $ social_bar = social_bar - 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs



    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event 3:
    pause(1.0)
    if savings == True:
        $ money_amount = money_amount + 1
    scene bg pizza2
    with fade
    show jessica smile at left
    with dissolve
    Jessica "I'm done cleaning! I’m clocking out!"
    "As I went to clock out, I came to a startling realization..."
    show jessica scared at left
    with dissolve
    Jessica "Um… Where’s my wallet?"
    "In a panic, I retraced my steps. No wallet. I spent the entire morning behind the counter, so I couldn’t have dropped it in a place where a customer could steal it."
    "My entire shift was with Ben! Did he-"
    show ben smile at right
    with dissolve
    Ben "Are you ready to go?"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I say?"

     "Did you take my wallet?":
         show jessica angry at left
         with dissolve
         Jessica "Did you prank me?"
         show ben neutral at right
         with dissolve
         Ben "What are you talking about?"
         Jessica "I had my wallet and now it’s gone. Did you take it?"
         show ben angry at right
         with dissolve
         Ben "Of course not! I wouldn’t do something like that!"
         Boss "Jessica! Is this your wallet? I found it in the back."
         show jessica nervous at left
         with dissolve
         Jessica "Oh.......Thanks. Sorry about accusing you Ben."
         Ben "…"
         scene bg black
         with fade
         "I think I offended him! I should apologize again later…"
         $ social_bar = social_bar - 2
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "I lost my wallet!":
         Jessica "I can’t find my wallet. Can you help me look?"
         show ben scared at right
         with dissolve
         Ben "Sure. Where did you last have it-"
         Boss "Jessica! Is this yours? I found it in the back!"
         show jessica smile at left
         with dissolve
         Jessica "Oh! Thanks! I won’t lose it again!"
         show ben smile at right
         with dissolve
         Ben "Cool! Let’s go!"
         scene bg black
         with fade
         "I’m glad I didn’t accuse Ben. That would have made things very awkward…"
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event 4
    pause(1.0)
    if savings == True:
        $ money_amount = money_amount + 1
    scene bg school2
    with fade
    Jessica "Oh no! I’m going to be late for third period!"
    "I had spent way too much time packing up after the bell and was running as fast as I could. I didn’t even have time to fix my untied shoes."
    "I can either go left into a hallway and take the stairs after or I could go right to a staircase and then go down the hall…"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I do?"

     "Take the stairs!":
         scene bg school1
         with fade
         "I ran as fast as I could down the stairs."
         "As I approached the stairs, I tripped on my untied shoelace."
         show jessica scared
         with dissolve
         Jessica "AH!"
         scene bg black
         with fade
         "I ended up breaking my leg from that incident. My mom said I shouldn’t have tried to run down stairs and I had to pay $80 for crutches."
         "What bad luck…"
         $ money_amount = money_amount - 80
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "Go down the hallway!":
         "I ran as fast I could down the hallway."
         show jessica scared
         with dissolve
         Jessica "AH!"
         scene bg black
         with fade
         "I tripped on my untied shoelace and fell on the floor."
         "Thank goodness! That would have been bad if I took the stairs first…"

    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event 5
    stop music fadeout 1.0
    pause(2.0)
    play music bgm_wallpaper
    if savings == True:
        $ money_amount = money_amount + 1
    scene bg house2
    with fade
    show jessica laugh2
    with dissolve
    Jessica "Man… walking to work really stinks…"
    Mom "So do you! You really should shower!"
    show jessica smile
    with dissolve
    Jessica "I’m going to need a car if I want to not have to walk a mile every day…"
    show jessica happy
    with dissolve
    Jessica "Oh wait! I have money now! I could probably go buy a car!"
    scene bg black
    with fade
    "I realized then that I knew nothing about buying cars and went to see Mr. B."
    pause(0.5)
    scene bg office
    with fade
    show mrb smile at left
    with dissolve
    MrB "Welcome back, Jessica! What’s up?"
    show jessica smile at right
    with dissolve
    Jessica "I need to buy a car and I have no idea how."
    MrB "Well, obviously you wouldn’t pay the full price up front. Instead, you would take out an auto loan."
    MrB "The important thing about auto loans is that they work differently from regular loans. As the name suggests, an auto loan is related only to cars.
    In addition, the lender of the car is technically the owner until the loan is paid off."
    MrB "So for example, if you crash the car, you technically crash their car."
    show jessica laugh2 at right
    with dissolve
    Jessica "Do you think I’ll crash a car?"
    show mrb normal2 at left
    with dissolve
    MrB "Probably."
    show jessica sad at right
    with dissolve
    Jessica "Wait-"
    show mrb smile at left
    with dissolve
    MrB "Anyway, the loan is really dependent on the car you buy and the deal you make. Whatever deal you come to, it's important that you pay. If you don’t, the bank can seize it."
    scene bg black
    with fade
    "After leaving Mr. B’s office, I searched the internet for good deals and was stuck between 2 deals."
    pause(0.5)
    scene bg house
    with fade
    "Thankfully, my mom agreed to help pay most of the loan eitherway; however, I still had to pay something."
    "With one deal, I would be paying $20 per week for fewer weeks and the other, I would be paying $10 for a while."
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I do?"

     "$10 Deal":
         "While paying off the debt quicker is tempting, I don't want to lose all of my money."
         "For the rest of the game, $10 will be subtracted after every choice."
         scene bg black
         with fade
         $ money_amount = money_amount - 10
         $ deal1 = True
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "$20 Deal":
         "I ended up going with the $20 deal. It's easier to pay a lot to pay off a debt quicker, right?"
         "For the next three choices, $20 will be subtracted from the bank."
         scene bg black
         with fade
         $ deal2 = True
         $ money_amount = money_amount - 20
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event 6
    pause(1.0)
    if savings == True:
        $ money_amount = money_amount + 1
    $ money_amount = money_amount + 150
    if deal2 == True:
        $ money_amount = money_amount - 20
    if deal1 == True:
        $ money_amount = money_amount - 10
    "Luckily for me, the next week was pay week. I earned an additional $150. I was relieved to get more money with Ben's birthday around the corner."
    scene bg store
    with fade
    show jessica smile at left
    with dissolve
    Jessica "So what are you getting him?"
    show ruby normal at right
    with dissolve
    Ruby "I don’t know yet… He’s kind of a difficult person to shop for. What about you?"
    Jessica "I can’t tell what I should get him. I know he wanted a board game that costs around $20. I could get him that, but I know he also wanted a video game that costs around $60."
    show ruby angry at right
    with dissolve
    Ruby "Stupid inflation!"
    show jessica smile at left
    with dissolve
    Jessica "How about this, if I get him one thing, you can get the other."
    show ruby smile at right
    with dissolve
    Ruby "Alright! Which thing do you want to buy?"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I pick?"

     "The Video Game ($60)":
         show jessica happy at left
         with dissolve
         Jessica "I’ll get the video game!"
         Ruby "Cool! I’ll get the board game!"
         scene bg black
         with fade
         "Ruby and I were able to buy the presents on time. While I was happy to see Ben enjoyed his gift, my wallet definitely wasn’t happy that I chose the expensive option."
         $ money_amount = money_amount - 60
         if social_bar != 4:
             $ social_bar = social_bar + 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "The Board Game ($20)":
         show jessica happy at left
         with dissolve
         Jessica "I’ll get the board game!"
         show ruby angry at right
         with dissolve
         Ruby "Dang it! You took the cheap one…"
         scene bg black
         with fade
         "Me and Ruby were able to buy the presents on time. While I was happy to see Ben happy, Ruby seemed slightly annoyed that I picked the cheaper option and left the expensive one to her."
         $ money_amount = money_amount - 20
         $ social_bar = social_bar - 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event7
    pause(1.0)
    if savings == True:
        $ money_amount = money_amount + 1
    if deal2 == True:
        $ money_amount = money_amount - 20
    if deal1 == True:
        $ money_amount = money_amount - 10
    scene bg house2
    with fade
    "While I had a car, I still couldn’t take it out without a license. I was finally doing my driving lessons…"
    Mom "Jessica! Did you schedule your appointments?"
    show jessica happy
    with dissolve
    Jessica "Yep! All 8 of them are scheduled."
    Mom "Do you even have the money for that?"
    show jessica nervous
    with dissolve
    Jessica "W-wait, they aren’t free?"
    Mom "Why do you always do these things? They are very pricey. I’d imagine you’d at least go through $70 until you get your next paycheck."
    show jessica scared
    with dissolve
    Jessica "Dang it…"
    Mom "How about this? If you want, I’ll help pay for them so you can focus on saving for college."
    show jessica smile
    with dissolve
    "That does sound like a good offer, but I really wanted to impress my mom by showing her I could be responsible with money…"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I do?"

     "Yes, please!":
         show jessica laugh2
         with dissolve
         Jessica "T-thanks… I owe you for this."
         scene bg black
         with fade
         "In the end, I paid only $20 for the lessons that cycle. While I didn’t impress my mom like I wanted, I at least saved money…"
         $ money_amount = money_amount - 20
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "I'll pay for it!":
         Jessica "You don’t have to pay for it! I was just saying how shocked I was because of the amount."
         Mom "Jessica, that’s amazing. I’m really proud of you for being so responsible with your money."
         show jessica happy
         with dissolve
         Jessica "T-thanks…"
         scene bg black
         with fade
         "While lessons ended up being a very big expense, I was able to impress my mom. I’d consider that a win."
         $ money_amount = money_amount - 70
         if social_bar != 4:
             $ social_bar = social_bar + 1
         if social_bar != 4:
            $ social_bar = social_bar + 1
         if social_bar != 4:
            $ social_bar = social_bar + 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event8
    stop music fadeout 1.0
    pause(2.0)
    play music bgm_two_finger_johnny
    if savings == True:
        $ money_amount = money_amount + 1
    if deal2 == True:
        $ money_amount = money_amount - 20
    if deal1 == True:
        $ money_amount = money_amount - 10
    scene bg house
    with fade
    show jessica confident at left
    with dissolve
    show ruby laugh at right
    with dissolve
    "I invited Ruby over to play some video games at my house."
    show jessica scared at left
    with dissolve
    "We were both really getting into a competitive mood, so I foolishly bet $10 and lost…"
    Jessica "I can’t believe it! I was so close to beating you there!"
    show ruby smile at right
    with dissolve
    Ruby "Hahaha! You’re still no match for me. Now, where is that $10?"
    "I could try seeing if we can go double or nothing. I might be able to avoid giving her money, but she is really good at this game…"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I say?"

     "Double or nothing!":
         show jessica confident at left
         with dissolve
         Jessica "How about we play for double or nothing. If you win, I owe you $20, but if I win, I owe you nothing!"
         Ruby "Alright! I like that competitive spirit! Let’s do it!"
         scene bg house
         with fade
         show jessica scared at left
         with dissolve
         Jessica "I LOST AGAIN?"
         show ruby laugh at right
         with dissolve
         Ruby "Hahaha! Now, my $20 please!"
         scene bg black
         with fade
         "I ended up having to pay $20. I guess the real lesson here is to not bet on stupid things. At least Ruby had a fun time."
         $ money_amount = money_amount - 20
         if social_bar != 4:
             $ social_bar = social_bar + 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "Fine...":
         show jessica sad at left
         with dissolve
         Jessica "Fine..."
         scene bg black
         with fade
         "I ended up paying $10. While I didn’t want to pay anything, it was better to play it safe. I guess the real lesson here is to not bet on stupid things…."
         $ money_amount = money_amount - 10
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #Event9
    pause(1.0)
    if savings == True:
        $ money_amount = money_amount + 1
    if deal1 == True:
        $ money_amount = money_amount - 10
    scene bg pizza
    with fade
    Boss "Jessica! I need to talk to you when you have a minute."
    show ben smile at left
    with dissolve
    Ben "Ooo! Someone’s in trouble!"
    show jessica scared at right
    with dissolve
    Jessica "Y-you wanted to see me?"
    Boss "Don’t worry! I’m not firing you or anything. I just wanted to ask if you could pick up some more hours. You’ve been doing a great job so far, so if you could,
    that would be helpful, but if not, that's fine too."
    show jessica smile at right
    with dissolve
    "That sounds great! More money is a good thing, but that definitely will mean less time to hang out with my friends…"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I say?"

     "Yes!!":
         Jessica "Sign me up!"
         Boss "Excellent."
         scene bg black
         with fade
         "I ended up earning an additional $40 from those hours, but it took a lot of my time. I didn’t get any time to spend with my friends…"
         $ money_amount = money_amount + 40
         $ social_bar = social_bar - 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "I can't...":
         Jessica "I would like to, but I can’t. I’m sorry…"
         Boss "Don’t worry about it! Let me know if that changes."
         scene bg black
         with fade
         "While I didn’t earn any additional money, I didn’t lose time with friends either. This definitely would have been the wrong choice if I was older,
         but I feel a bit happier to have some time as a teenager."
         if social_bar != 4:
             $ social_bar = social_bar + 1
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"

    #FINAL EVENT (YES OH MY GOD IT FEELS GOOD TO FINISH A GAME FOR THE FIRST TIME!!)
    pause(1.0)
    if savings == True:
        $ money_amount = money_amount + 1
    if deal1 == True:
        $ money_amount = money_amount - 10
    scene bg school2
    with fade
    "A big science fair for my school was coming up. For my project, I decided to make a poster board."
    "The problem… I kind of don’t have any supplies."
    "I mean, I could go out and buy them, but they are almost $70. I could also ask Ruby if she could help chip in, but she really doesn’t have any reason to…"
    "Your current money amount: $[money_amount]"
    "Your social bar: [social_bar]/4"
    menu:
     "What should I do?"

     "Buy the supplies!":
         scene bg black
         with fade
         "I ended up just buying the supplies. While it did cost a lot, I was proud. The entire point of this was for me to pay my own share, right?"
         $ money_amount = money_amount - 70
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

     "Ask Ruby!":
         show ruby angry at left
         with dissolve
         Ruby "You need to borrow money… again?"
         show jessica laugh2 at right
         with dissolve
         Jessica "Y-yes, though I promise this time I can actually pay it back!"
         Ruby "I thought the entire point of you getting a job was to not have this happen?"
         Ruby "...Fine, but please pay me back."
         scene bg black
         with fade
         "I was able to save money for a little while, but I think I upset Ruby…"
         $ social_bar = social_bar - 2
         if money_amount <= 0:
             jump game_overm
         if social_bar == 0:
             jump game_overs

    #ENDING
    stop music fadeout 1.0
    pause(2.0)
    play music bgm_carpe_diem
    scene bg beach
    with fade
    show ruby smile at left
    with dissolve
    Ruby "It’s been a while since you started your job! How are you feeling about everything?"
    show jessica smile at center
    with dissolve
    Jessica "It feels good, but stressful. I was able to manage my time and money, but I had to make some tough choices. Is it always like this?"
    show ben smile at right
    with dissolve
    Ben "Sometimes, but that’s just the way it is with money. Sometimes things come up and you have no choice but to deal with them. Other times, you have plenty of spending money.
    I’m sure you’ll figure it out!"
    show jessica laugh2 at center
    with dissolve
    Jessica "Though… What now? What random life event is going to cause me to make a financial choice?"
    show ben happy at right
    with dissolve
    Ben "You see, this is the end of the game. You're done. You win."
    show jessica scared at center
    with dissolve
    Jessica "Wait what?"
    show ruby laugh at left
    with dissolve
    Ruby "This entire time it was just a simulation to teach financial literacy. We don’t exist…"
    show jessica laugh at center
    with dissolve
    Jessica "Ok. I guess that makes sense."
    pause(0.5)
    show jessica scared at center
    with dissolve
    Jessica "Waaiiit…"
    scene bg ocean
    with fade
    "THE END! Thank you for playing the Financial Dilemma! I've had a lot of fun making this game and it is so great to finally see it finished!"
    "Your final money amount: $[money_amount]"
    "Your final social bar: [social_bar]/4"
    return

label game_overm:
    stop music fadeout 1.0
    pause(2.0)
    play music bgm_mischief_maker
    scene bg house2
    with fade
    Mom "JESSICA!!!!"
    show jessica smile
    with dissolve
    Jessica "Yeah?"
    Mom "This is the bank calling. Apparently your account balance is below 0…"
    show jessica nervous
    with dissolve
    Jessica "Oh… What does that mean? Can’t I just pay it back?"
    Mom "It’s not that simple! Banks can take legal action against you! This might be a big deal…"
    scene bg black
    with fade
    "Me and my mom were eventually able to pay off the debt, which luckily did not end with legal action, but I did get grounded. I shouldn’t have spent so much…"
    "Game Over"
    return

label game_overs:
    stop music fadeout 1.0
    pause(2.0)
    play music bgm_mischief_maker
    scene bg biketrail
    with fade
    show jessica smile at left
    with dissolve
    Jessica "Hey, Ben! Hey, Ruby! Ready to have some fun?"
    show ben angry at center
    with dissolve
    Ben "To be honest, no. Look, you’ve been being responsible with money lately
    and that’s cool, but you keep blowing us off. I would understand if you were busy or something, but every time it's just because you want to save money."
    show ruby angry at right
    with dissolve
    Ruby "Yeah. Every time we’ve asked you to do something you just say no. I get you want to save for the future, but I thought the entire point of this
    was to have just SOME money for when we do fun stuff…"
    Ruby "We’re off to go to the mall. Let us know when you decide you want to do something…"
    show jessica sad at left
    with dissolve
    Jessica "Wait-"
    scene bg black
    with fade
    "But they already headed off. While I did manage to save my money, I made my friends feel like I didn’t want to spend time with them. I should have managed things better…"
    "Game Over"
    return
