from abc import ABC, abstractmethod
import http.client
from simple_term_menu import TerminalMenu


class VisualInterface(ABC):
    
    @abstractmethod
    def register(self):
        pass
    @abstractmethod
    def login(self):
        pass
    def initial_prompt(self):
        pass

class TerminalInterface(VisualInterface):

    def initial_prompt(self,menu_options):
        print("#########################")
        print("#### Mortal Kombat ######")
        print("#########################")
       
        terminal_menu = TerminalMenu(menu_options)
        menu_entry_index = terminal_menu.show()
        print(f"Selected {menu_options[menu_entry_index]}!")
        return menu_options[menu_entry_index]
             

    def login(self):
        pass
    def register(self):
        pass