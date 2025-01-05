from abc import ABC, abstractmethod
import http.client
import getpass 
import urllib.parse
import json

class User():
    login_status = False
    auth_token: str = ""

    def __init__(self, connection):
        self.conn = connection
    # @staticmethod
    def login(self):
        username = input("Username: ")
        password = getpass.getpass()
        data = {"grant_type":"password","username": username, "password": password}
        payload = urllib.parse.urlencode(data)
        headers = {'Accept': 'application/json','Content-type': 'application/x-www-form-urlencoded'}
        self.conn.request("POST", "/users/login", payload, headers)
        response = self.conn.getresponse()
        body_json= json.loads(response.read().decode())
        if response.reason != "OK":
            print(body_json["detail"])
            return

        self.auth_token = body_json["access_token"] 
        self.login_status = True   
        print(self.auth_token)
        print("User logged")
        
          
        

        
        
    def register(self):
        pass
    def start_combat(self):
        pass
    def my_history(self):
        pass
    def my_heroes(self):
        pass
    

class AAA(ABC):
    """
    AAA authentication authorization accountability,
    Auth methods : Pass Hashing , JWT
    """
    def __init__(self, protocol_type, username, password):
        self.protocol_type = protocol_type
        self.username = username
        self.password = password
    @abstractmethod
    def register():
        pass
    def login():
        pass

class HTTPAAA(AAA):
    def __init__(self, http_ip, http_port):
        super.__init__("http")
        self.ip = http_ip
        self.port = http_port

    def register():
        pass
    def login():
        pass
# class CombatManage:
#     def register():
#         pass
#     def login():
#         pass
#     def start_combat():
#         pass
#     def my_heroes():
#         pass
#     def my_history():
#         pass