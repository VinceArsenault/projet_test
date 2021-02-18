# programme bidon

def main():
    num_try = 0
    continu = True
    while continu:
        film = input('Entrez un film: ')

        if film == 'Tape Gun':
            print('Got it ! Unline\'s the best')
            continu = False
        else:
            num_try += 1 
            print('please try again')
        if num_try == 2:
            print('might be sticky on one side...')
        elif num_try == 3:
            print('might even carry weapon...')
        elif num_try == 4:
            print('so we said it got glu and weapon...')
        elif num_try >= 5:
            print('does uline even make movie ?')
        if num_try == "quit":
            continnu = False

main()