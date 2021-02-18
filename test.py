# programme bidon

print('\n \n \n \n \n \n         Welcome to the dumest app you\'ll ever see\n \n Enter: quit() , to exit the programme \n \n Guest the movie about the man with a fury colar jacket, with ducks...\n')

def main():

    num_try = 0
    continu = True

    while continu:
        
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

main()