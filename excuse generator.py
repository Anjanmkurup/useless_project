import random
msg = ["I'm running late because I was trying to catch my cat, but it's faster than me.","Sorry, I overslept. My bed was too comfy.","I'm not late, I'm fashionably delayed.","Traffic was bad, but my podcast was really good.","My dog ate my schedule.","I lost track of time because I was having too much fun.","My car broke down... again.","I was stuck in a loop of YouTube videos.","Aliens abducted me, but they dropped me back off.", "I was reorganizing my sock drawer."]
ans = input("do you want an excuse?(y/n): ")
while ans == 'y':
    print(random.choice(msg))
    ans = input("do you want an excuse?(y/n): ")
    if ans == 'n':
        break