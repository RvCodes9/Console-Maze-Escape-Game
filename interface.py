from colorama import Fore, Style

class Interface:

    def interface(self, state):
        
        if state == 1:
            print(f'''{Fore.YELLOW}
            ###############    #
            # {self.char} #        #    #
            #        #         #
            ####################{Style.RESET_ALL}''')

        elif state == 2:
            print(f'''{Fore.YELLOW}
            ###############    #
            #    #        #    #
            # {self.char}     #         #
            ####################{Style.RESET_ALL}''')

        elif state == 3:
            print(f'''{Fore.YELLOW}
            ###############    #
            #    #        #    #
            #     {self.char} #         #
            ####################{Style.RESET_ALL}''')

        elif state == 4:
            print(f'''{Fore.YELLOW}
            ###############    #
            #    # {self.char}     #    #
            #        #         #
            ####################{Style.RESET_ALL}''')

        elif state == 5:
            print(f'''{Fore.YELLOW}
            ###############    #
            #    #     {self.char} #    #
            #        #         #
            ####################{Style.RESET_ALL}''')

        elif state == 6:
            print(f'''{Fore.YELLOW}
            ###############    #
            #    #        #    #
            #        # {self.char}      #
            ####################{Style.RESET_ALL}''')

        elif state == 7:
            print(f'''{Fore.YELLOW}
            ###############    #
            #    #        #    #
            #        #      {self.char} #
            ####################{Style.RESET_ALL}''')

        elif state == 8:
            print(f'''{Fore.YELLOW}
            ###############    #
            #    #        # {self.char} #
            #        #         #
            ####################{Style.RESET_ALL}''')

        elif state == 9:
            print(f'''{Fore.YELLOW}
            ############### {self.char} #
            #    #        #    #
            #        #         #
            ####################{Style.RESET_ALL}''')