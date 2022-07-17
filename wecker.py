from colorama import Fore, Style, init
from pyfiglet import Figlet
import time
import os
from win10toast import ToastNotifier

c = Fore.LIGHTCYAN_EX
r = Fore.LIGHTRED_EX
re = Fore.RESET

d = Style.DIM
res = Style.NORMAL

on = True
bull_on = True

class Wecker():
    

    def __init__(self):
        self.start()

    def start(self):
        os.system("cls")
        print("START")
        print("")
        print("[1] Live")
        print("[2] Add")
        print("[3] Exit")
        print("")
        action = input("[+] ")

        if action == "1":
            self.live()
        elif action == "2":
            self.add()
        elif action == "3":
            quit()

    def live(self):

        global on, bull_on

        os.system("cls")
        print("LIVE")
        print("")

        if bull_on:
            bullet = "◉"
            bull_on = False
        else:
            bullet = " "
            bull_on = True

        print("[ " + r + bullet + re +  " ] | " + time.strftime("%H:%M:%S"))
        print("")

        read_file = open("times.txt", "r")

        for line in read_file.readlines():
            sp = line.strip("\n").split(" | ")

            if sp[0] == time.strftime("%H:%M"):

                if time.strftime("%S") == "00":
                    player = vlc.MediaPlayer("beep.mp3")
                    player.play()

                    toast = ToastNotifier()
                    toast.show_toast(
                        "Time Is Up [" + sp[0] +"]",
                        sp[1],
                        duration = 10,
                        threaded = True,
                    )

                if on:
                    on = False
                    print(c + sp[0] + " | " + sp[1] + re)
                else:
                    on = True
                    print(r + sp[0] + " | " + sp[1] + re)
            
            else:
                print(sp[0] + " | " + sp[1])

        print("")
        print(d+ "[<--] | Ctrl+C" + res)

        try:
            time.sleep(1)
            self.live()
        except KeyboardInterrupt:
            self.start()

    def add(self):
        os.system("cls")
        print("ADD")
        print("")

        hour = input("Hour:   ")
        minute = input("Minute: ")
        text = input("Title:  ")

        write_file = open("times.txt", "a")
        write_file.write(hour + ":" + minute + " | " + text + "\n")
        write_file.close()

        more = input("Would you like to add more times? [y|N]: ")

        if more == "Y" and more == "y":
            self.add()
        else:
            self.start()

app = Wecker()
app.__init__()