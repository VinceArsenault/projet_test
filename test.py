# programme bidon

print('\n \n Welcome to the dumest app you\'ll ever see\n Enter: quit() , to exit the programme \n \n Guest the movie about the man with a fury colar jacket, with ducks...\n')

def main():

    num_try = 0
    continu = True

    while continu:
        
        film = input('Enter movie\'s name: ')

        if (film) == 'tape gun':
            print('Got it ! Unline\'s the best')
            continu = False

      
            

        if film != 'tape gun' and film != 'quit()':
            num_try += 1 

            if num_try == 1:
                print('\n nah...please try again \n ')
            if num_try == 2:
                print('\nnope, it might be sticky on one side...')
            elif num_try == 3:
                print('\noh well...but might even carry weapon...')
            elif num_try == 4:
                print('\nso we said it got glu and weapon...')
            if num_try >= 5:
                print('\ndoes uline even make movie ?')        
        if film == 'quit()':
            continu = False

main()