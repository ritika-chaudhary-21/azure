import random
import pyttsx3
from playsound import playsound

engine = pyttsx3.init()

def gameWin(comp, you):
# If two values are equal, declare a tie 
    if comp == you:
        playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\gameover.mp3')
        return None
    
#Check for all possiblities when computer chose s
    elif comp == 's':
        if you == 'w':
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\snake-hissing.mp3')
            return False
        elif you == 'g':
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\load-gun-sound-effect.mp3')
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\shoot.mp3')
            return True
        
#Check for all possiblities when computer chose w
    elif comp == 'w':
        if you == 'g':
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\water.wav')
            return False
        elif you == 's':
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\snake-hissing.mp3')
            return True
        
#Check for all possiblities when computer chose g
    elif comp == 'g':
        if you == 's':
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\load-gun-sound-effect.mp3')
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\shoot.mp3')
            return False
        elif you == 'w':
            playsound('C:\\Users\\ADMIN\\Desktop\\Snake Water Gun Game\\Snake_Water_Gun_Game\\Sound\\water.wav')
            return True

text="Welcome To Snake-Water-Gun Game!"  
print(text)
engine.say(text)
engine.runAndWait()

choice=None
while(choice!=2):
    choice=int(input("Press 1: PLAY\nPress 2: EXIT\n"))

    if(choice==1):
        print("Thanks for choosing to play!")
        print("Computer Turn: Snake(s), Water(w) or Gun(g)?")
        randNo = random.randint(1, 3)
        if randNo == 1:
            comp = 's'
        elif randNo == 2:
            comp = 'w'
        elif randNo == 3:
            comp = 'g'

        you= input("Your Turn: Snake(s), Water(w) or Gun(g)?\n")

        print(f"Computer chose {comp}")

        a = gameWin(comp, you)
        if a == None:
            print("The game is a tie!")
        elif a:
            print("You Won!")
        else:
            print("You Lost!")
    
    else:
        print('Exiting! Thanks for playing!')
