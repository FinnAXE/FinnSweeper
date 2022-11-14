# IP Sweeper
# Created by Claudio Lo Preiato
# Finmeccanic Calabria S.R.L
# Finn
import os

print('''
          _____   ____   ____   ____
        /  ___/  /   /  /    |/    /
       /  /__   /   /  /          /  __    __
      /  ___/  /   /  /   /|     /  /  | /  /
     /  /     /   /  /   / |    /  /  /|   /
    /__/     /___/  /___/  |___/  /__/ |__/                                             
-Finn, a product created by Claudio Lo Preiato 
-Finmeccanic Calabria S.R.L 

 ''')


def main():
    ip = input("[+] Enter the Host IP Address:\t")
    print("[+] Starting Ping Sweeping on " + ip)
    dot = ip.rfind(".")
    ip = ip[0:dot + 1]
    for i in range(1, 256):
        host = ip + str(i)
        response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")

        if response == 0:
            print(host + " is up")
        else:
            print(host + " is down")
    main()


main()
