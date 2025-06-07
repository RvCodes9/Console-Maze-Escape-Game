# Python modules
from colorama import Fore, Style
from os import name,system
from time import sleep

# My module
from interface import Interface

class Game(Interface):

    def __init__(self):

        self.char = '🧑'
        self.state = 1
        self.game_loop = True
        
        self.clear_console()
        self.interface(self.state)
        
        while self.game_loop:

            self.player()
            self.interface(self.state)

        sleep(1)
        self.clear_console()

        print(f'''{Fore.YELLOW}
            ####################
            #      {Fore.GREEN}Winner{Style.RESET_ALL}{Fore.YELLOW}      #
            #        {self.char}        #
            ####################{Style.RESET_ALL}''')



    def player(self):

        if self.state == 1:

            self.player_move = input(f"{Fore.GREEN}\n(down) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'down':
                self.state = 2



        elif self.state == 2:

            self.player_move = input(f"{Fore.GREEN}\n(up,right) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'up':
                self.state = 1

            elif self.player_move == 'right':
                self.state = 3



        elif self.state == 3:

            self.player_move = input(f"{Fore.GREEN}\n(left,up) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'up':
                self.state = 4

            elif self.player_move == 'left':
                self.state = 2



        elif self.state == 4:

            self.player_move = input(f"{Fore.GREEN}\n(down,right) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'down':
                self.state = 3

            elif self.player_move == 'right':
                self.state = 5


        elif self.state == 5:

            self.player_move = input(f"{Fore.GREEN}\n(left,down) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'down':
                self.state = 6

            elif self.player_move == 'left':
                self.state = 4


        elif self.state == 6:

            self.player_move = input(f"{Fore.GREEN}\n(up,right) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'up':
                self.state = 5

            elif self.player_move == 'right':
                self.state = 7


        elif self.state == 7:

            self.player_move = input(f"{Fore.GREEN}\n(left,up) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'left':
                self.state = 6

            elif self.player_move == 'up':
                self.state = 8


        elif self.state == 8:

            self.player_move = input(f"{Fore.GREEN}\n(down,up) Move ::: {Style.RESET_ALL}")
            
            self.clear_console()

            if self.player_move == 'down':
                self.state = 7

            elif self.player_move == 'up':
                self.state = 9


        elif self.state == 9:
            self.state = 'end'
            self.game_loop = False


    def clear_console(self):

        if name == 'nt':
            system('cls')
        
        else:
            system('clear')

game = Game()