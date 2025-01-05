import http.client
from ui import TerminalInterface
from user import User

# from simple_term_menu import TerminalMenu 

class MortalKombat:
    """ """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.ui = TerminalInterface()
        self.connection  = http.client.HTTPConnection(f"{self.ip}:{self.port}")
        self.user = User(connection = self.connection)
        
       

    def run_game(self):
        
        # options = ["Register","Login","start combat","my heroes","my history"]
        options = {"Register":"combat_manager/register",
                   "Login": "combat_manager/login",
                   "start_combat": "combat_manager/start_combat",
                   "history": "combat_results/results",
                   "My Heroes": "combat_manager/my_heroes",
                   }
       

        # print(a)
        # print(options[a])
       
        while True:
            a = self.ui.initial_prompt(list(options.keys()))
            match a:
                case "Register":
                    pass
                case "Login":
                    self.user.login()
                case "start_combat":
                    pass
                case "history":
                    pass
                case "heroes":
                    pass
                    
            
        #  self.connection = http.client.HTTPConnection(self.ip, self.port, timeout=10)

   
 

    def check_service(self):
        pass