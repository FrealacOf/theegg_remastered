# ACTIONS
# > 1. SNACKS (+5 [HUN])
# > 2. MEALS (+5 [HAP])
# > 3. PLAY (randomint left or right [si vous on choissis le meme sens on perd])
# > 4. PUNISH (+5 [DIS])

# DONNES
# > HUN (300)
# > HAP (300)
# > DIS (300)

# EXPERIENCE
# > Niv1 : 1000 (Next Level + 1000)

# TIMERS
# > if timer = 100(100S) - 50[HUN, HAP, DIS]

# DEATH
# if HUN,HAP,DIS = 0 [GAME OVER]
import random
import time
hun = 0 #max 300
hap = 0 #max 300
dis = 0 #max 300

level = 0 #+1000 a chaque level update

remove_timer = 0 #100s =- 50[HUN, HAP, DIS]

snacks = 5
meals = 5
punish = 5 

# START
def start():
    print(""" 
                    ___           ___                ___           ___           ___     
      ___          /  /\         /  /\                  /  /\         /  /\         /  /\    
     /__/\        /  /:/        /  /::\                /  /::\       /  /::\       /  /::\   
     \  \:\      /  /:/        /  /:/\:\              /  /:/\:\     /  /:/\:\     /  /:/\:\  
      \__\:\    /  /::\ ___   /  /::\ \:\            /  /::\ \:\   /  /:/  \:\   /  /:/  \:\ 
      /  /::\  /__/:/\:\  /\ /__/:/\:\ \:\          /__/:/\:\ \:\ /__/:/_\_ \:\ /__/:/_\_ \:\
     /  /:/\:\ \__\/  \:\/:/ \  \:\ \:\_\/          \  \:\ \:\_\/ \  \:\__/\_\/ \  \:\__/\_\/
    /  /:/__\/      \__\::/   \  \:\ \:\             \  \:\ \:\    \  \:\ \:\    \  \:\ \:\  
   /__/:/           /  /:/     \  \:\_\/              \  \:\_\/     \  \:\/:/     \  \:\/:/  
   \__\/           /__/:/       \  \:\                 \  \:\        \  \::/       \  \::/   
                   \__\/         \__\/                  \__\/         \__\/         \__\/    
                                    ____________________
                                    
                                  [ PRESS ENTER TO START ] 
                                    ____________________
    """)
    time.sleep(2)
    ask_names = input("Veilliez entrez un pseudo\n> ")
start()