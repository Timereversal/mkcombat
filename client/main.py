from mortal_kombat import MortalKombat

if __name__ == '__main__':
    mk = MortalKombat(ip="127.0.0.1",port=8000)
    mk.run_game()
    print("checking")