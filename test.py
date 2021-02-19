from random import randrange
import webbrowser

print('\n \n \n \n         Welcome to the dumbest app you\'ll ever see\nEnter: quit() , to exit the programme\n')

def main():
    print('Enter the name of the game you wanna play \n movie: to play guest the movie\n number: to play guest the number\n google: to ask google a question')
    game_name = input('Enter the game name here:  ')
    if game_name == 'movie':
        guest_movie()
    if game_name =='number':
        guest_num()
    if game_name == 'google':
        ask_google()

def guest_num():
    num_try = 0
    continu = True
    num_to_guest = randrange(0,51)
    while continu:
        print('guest a number in between 0 and 50 ')
        num_guested = int(input('What is your guest?: '))
        if num_guested == num_to_guest:
            print('You got it bud !')
            continu = False
        if num_guested >= num_to_guest + 10:
            print('You can go a bit lower you crazy fool')
        if num_guested >= num_to_guest + 5:
            print('you can go a tiny bit lower but you are getting there')
        if num_guested <= num_to_guest - 10: 
            print(' you can fo a bit higher you extremist turtle')
        if num_guested <= num_to_guest - 5: 
            print('you can go a tiny bit higher but you are getting there')


def guest_movie():
    num_try = 0
    continu = True

    while continu:
        print('Name a movie about a guy with a leather jacket flighing with ducks\n')
        film = input('Enter movie\'s name: ')

        # if answer if right
        if (film) == 'tape gun':
            print('\nYou got it ! Unline\'s the best!!! \n')
            continu = False

        # if answer if wrong
        if film != 'tape gun' and film != 'quit()':
            
            num_try += 1 

            if num_try == 1:
                print('\n nah...please try again \n ')
            if num_try == 2:
                print('\nnope, it might be sticky on one side...\n')
            elif num_try == 3:
                print('\noh well...but you know, it might even carry weapon...\n')
            elif num_try == 4:
                print('\nso we said it got glu and weapon...\n')
            if num_try >= 5:
                print('\ndoes uline even make movie ?\n')        
        if film == 'quit()':
            continu = False

def ask_google():
    ask = input('ask something to your friend google:  ')
    chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome).open_new('http://google.com/search?q=' + ask)

main()