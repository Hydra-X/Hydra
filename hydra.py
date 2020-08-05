#!/usr/bin/env python

import os

os.system("clear")

print("""\x1b[37;1m
 _   _           _               
| | | |_   _  __| |_ __ __ _ 
| |_| | | | |/ _` | '__/ _` |
|  _  | |_| | (_| | | | (_| |
|_| |_|\__, |\__,_|_|  \__,_|
       |___/ \x1b[0m""")

print("""\x1b[33;92m
Welcome To Hydra Ultimate Software...
This Is Hydra Scanner Software
\x1b[0m""")


while(True):

    islem = raw_input("\x1b[37;1mHydra> \x1b[0m")

    if((islem=="hydra --help") or (islem=="--help") or (islem=="help") or (islem=="-h")):

        print("""\x1b[37;1m

    hydra --help = 'Show The Help Information'

    hydra --version = 'Show The Software Version'

    hydra --about = 'Show The About Software'

    hydra --show-modules = 'Show The Modules'

    use <Module Name> = 'Use The Modules'

        \x1b[0m""")

    elif((islem=="hydra --version") or (islem=="version") or (islem=="--version") or (islem=="-v")):
        print("""\x1b[31;1m
   Hydra Ultimate 1.0
      Profesional Hacker Tool
        
        \x1b[0m""")

    elif((islem=="hydra --about") or (islem=="about") or (islem=="--about") or (islem=="-a")):
        print("""\x1b[31;14m

    Hydra Is Hack And Cyber Securty Software.
    Hydra Programming By Hydra-X
   
        \x1b[0m""")

    elif((islem=="hydra --show-modules") or (islem=="--show-modules") or (islem=="show modules") or (islem=="-s")):

        print("""\x1b[37;1m
  
   Web Scanner:
  
       |> 1. Hydra Fierce
       |> 2. Hydra Dnsrecon
       |> 3. Hydra Dnswalk
       |> 4. Hydra Dnsmap
       |> 5. Hydra Dnsdict6
       |> 6. Hydra Dnsenum
       |> 7. Hydra Goofile
       |> 8. Hydra Dirb
       |> 9. Hydra Wafw00f
       |> 10. Hydra Dmitry
       |> 11. Hydra Email For Msfconsole
       |> 12. Hydra Web Scanner Pro 1.0
       
   Nmap Scanner:  
      
       |> 13. Hydra Normal Scanner
       |> 14. Hydra Port Scanner
       |> 15. Hydra Ping Scanner 
       |> 16. Hydra Service Scanner
       |> 17. Hydra Tcp Syn Scanner 
       |> 18. Hydra Ack Scanner 
       |> 19. Hydra Fin Scanner
       |> 20. Hydra Window Scanner
       |> 21. Hydra Tcp Connect Scanner
       |> 22. Hydra Udp Scanner
       |> 23. Hydra Version Scanner
       |> 24. Hydra Os Scanner
       |> 25. Hydra Anonymous Scanner
       |> 26. Hydra Fake Ip Scanner

        
        \x1b[0m""")

     
    elif(islem=="use 1"):
        print("")
        print("\x1b[31;1mFierce: \x1b[0m")
        site = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("fierce --dns " + site)
    elif(islem=="use 2"):
        print("")
        print("\x1b[31;1mDnsrecon: \x1b[0m")
        site2 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("dnsrecon -d " + site2 + " -t goo")
    elif(islem=="use 3"):
        print("")
        print("\x1b[31;1mDnswalk: \x1b[0m")
        site3 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("dnswalk " + site3 + ".")
    elif(islem=="use 4"):
        print("")
        print("\x1b[31;1mDnsmap: \x1b[0m")
        site4 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("dnsmap " + site4)
    elif(islem=="use 5"):
        print("")
        print("\x1b[31;1mDnsDict6: \x1b[0m")
        site5 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("dnsdict6 " + site5)
    elif(islem=="use 6"):
        print("")
        print("\x1b[31;1mDnsenum: \x1b[0m")
        site6 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("dnsenum -enum " + site6)
    elif(islem=="use 7"):
        print("")
        print("\x1b[31;1mGoofile: \x1b[0m")
        site7 = raw_input("Hydra> Please Write The Domain Names> ")
        name = raw_input("Hydra> Domain> Extension(Exp: com,asp,edu)> ")
        os.system("goofile -d " + site7 + " -f " + name)
    elif(islem=="use 8"):
        print("")
        print("\x1b[31;1mDirb: \x1b[0m")
        site8 = raw_input("Hydra> Please Write The Domain Names> ")
        wordlist = raw_input("Hydra> Please Write Wordlist For Dirb> ")
        os.system("dirb " + site8 + " " + wordlist)
    elif(islem=="use 9"):
        print("")
        print("\x1b[31;1mWafw00f: \x1b[0m")
        site9 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("wafw00f " + site)
    elif(islem=="use 10"):
        print("")
        print("\x1b[31;1mDmitry: \x1b[0m")
        site10 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("dmitry -winsepfb " + site10)
    elif(islem=="use 11"):
        print("")
        print("\x1b[31;1mMsfconsole Email Collector: \x1b[0m")
        site11 = raw_input("Hydra> Please Write The Domain Names> ")
        os.system("msfconsole -x " + '"' + "use auxiliary/gather/search_email_collector; set DOMAIN " + site11 + "; run" + '"')
    elif(islem=="use 12"):
        os.system("clear")        
        os.system("figlet Web Scanner Pro")
        print("")
        
        print("""\x1b[31;1m

Welcome To Web Scanner Pro Software...
This Is Web Scanner Software

        \x1b[0m""")

        print("""\x1b[36;1mStarting Hydra Server...
        \x1b[0m""")

        site99 = raw_input("Hydra> WebScanner> Please Write The Domain> ")

        print("")
        print("\x1b[31;1mDnsenum \x1b[0m")

        os.system("dnsenum -enum " + site99)
        print("")
        print("\x1b[31;1mDnsmap \x1b[0m")

        os.system("dnsmap " + site99)
        print("")
        print("\x1b[31;1mDnswalk \x1b[0m")

        os.system("dnswalk " + site99 + ".")
        print("")
        print("\x1b[31;1mDnsrecon \x1b[0m")

        os.system("dnsrecon -d " + site99 + " -t goo")
        print("")
        print("\x1b[31;1mDnsdict6 \x1b[0m")

        os.system("dnsdict6 " + site99)
        print("")
        print("\x1b[31;1mFierce \x1b[0m")

        os.system("fierce -dns " + site99)
        print("")
        print("\x1b[31;1mGoofile \x1b[0m")

        os.system("goofile -d " + site + " -f asp")
        os.system("goofile -d " + site + " -f edu")
        os.system("goofile -d " + site + " -f net")
        os.system("goofile -d " + site + " -f com")
        os.system("goofile -d " + site + " -f gov")
        print("")
        print("\x1b[31;1mDmitry \x1b[0m")

        os.system("dmitry -winsepfb " + site99)
        print("")
        print("\x1b[31;1mWafw00f \x1b[0m")

        os.system("wafw00f " + site99)
        print("")
        print("\x1b[31;1mBlindElephent.py \x1b[0m")

        os.system("BlindElephant.py " + site99 + " joomla")
        os.system("BlindElephant.py " + site99 + " wordpress")
        os.system("BlindElephant.py " + site99 + " guess")
        os.system("BlindElephant.py " + site99 + " drupal")
        print("")
        print("\x1b[31;1Msfconsole \x1b[0m")

        os.system("msfconsole")
        os.system("msfconsole -x " + '"' + "use auxiliary/gather/search_email_collector; set DOMAIN " + site99 + "; run" + '"')

    elif(islem=="use 13"):
        pin = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap " + pin)
    elif(islem=="use 14"):
        pin2 = raw_input("Hydra> Please Write The Ip> ")
        pon = raw_input("Hydra> Please Write The Port> ")
        os.system("nmap -p" + pon + " " + pin2)
    elif(islem=="use 15"):  
        pin3 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -sP -T4 " + pin3 + "/24")
    elif(islem=="use 16"):
        pin4 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -sV " + pin4)
    elif(islem=="use 17"):
        pin5 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -sS " + pin5)
    elif(islem=="use 18"):
        pin6 = raw_input("Hydra> Please Write The Ip> ")
        pon2 = raw_input("Hydra> Please Write The port> ")
        os.system("nmap -sA " + pin6 + " -p" + pon2)
    elif(islem=="use 19"):
        pin7 = raw_input("Hydra> Please Write The Ip> ")
        pon3 = raw_input("Hydra> Please Write The Port> ")
        os.system("nmap -sF " + pin7 + " -p" + pon3)
    elif(islem=="use 20"):
        pin8 =  raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -sW -v " + pon8)
    elif(islem=="use 21"):
        pin9 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -sT " + pin9)
    elif(islem=="use 22"):
        pin10 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -sU " + pin10)
    elif(islem=="use 23"):
        pin11 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -sV " + pin11)
    elif(islem=="use 24"):
        pin12 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -o --osscan-guess " + pin12)
        os.system("nmap -o --osscan-limit " + pin12 + "/24")
        os.system("nmap -o -max-retries 3 " + pin12 + "/24")
    elif(islem=="use 25"):
        pin13 = raw_input("Hydra> Please Write The Ip> ")
        pon3 = raw_input("Hydra> Please Write The Port> ")
        os.system("proxychains nmap -sT -sV -p" + pon3 + " " + pin13)
    elif(islem=="use 26"):
        pen = raw_input("Hydra> Please Write The Fake Ip> ")
        pin14 = raw_input("Hydra> Please Write The Ip> ")
        os.system("nmap -D " + pen + " " + pin14)
    else:
        print("\x1b[31;1m[!]\x1b[0m" + "\x1b[37;1m Unknown command: \x1b[0m" + islem)        
