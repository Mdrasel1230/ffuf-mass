import os
import sys, time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", required=True, help="Give the subdomain list")
parser.add_argument("-w", "--wordlist", help="Give the wordlist")
parser.add_argument("-o", "--output", help="Give the path where output will be saved")

class bcolors:
    OKCYAN = '\033[96m'

version = 'v0.1'+bcolors.OKCYAN
site = 'list urls should be contain urls like this format https://site.com'+bcolors.OKCYAN

print(bcolors.OKCYAN+'\n'
r'''                       

  ______ ______ _    _ ______   __  __           _____ _____     
 |  ____|  ____| |  | |  ____| |  \/  |   /\    / ____/ ____| --------------- 
 | |__  | |__  | |  | | |__    | \  / |  /  \  | (___| (___                -
 |  __| |  __| | |  | |  __|   | |\/| | / /\ \  \___ \\___ \    ^_^       -
 | |    | |    | |__| | |      | |  | |/ ____ \ ____) |___) |            -
 |_|    |_|     \____/|_|      |_|  |_/_/    \_\_____/_____/            -
                                                                       -                                                         
-----------------------------------------------------------------------

  ____          _____                _        __   ___  
 |  _ \        |  __ \              | |      /_ | / _ \ 
 | |_) |_   _  | |__) |__ _ ___  ___| | __   _| || | | |
 |  _ <| | | | |  _  // _` / __|/ _ \ | \ \ / / || | | |
 | |_) | |_| | | | \ \ (_| \__ \  __/ |  \ V /| || |_| |
 |____/ \__, | |_|  \_\__,_|___/\___|_|   \_/ |_(_)___/ 
         __/ |                                          
        |___/                                           

            ++++++++++++++ Thanks for using this script ++++++++++++++
                 ---------------- ./Md Rasel ------------------
                     ######## We Are ~ErrOr SquaD~ #########

        ''')
print(version)
print(site)

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args=parser.parse_args()

a = args.list
b = open(a, "r")
read = b.readlines()
out = 0


try:
    for line in read:
        out += 1
        if 'http://' not in line and 'https://' not in line:
            line = 'http://'+line
            line = line+'/FUZZ'
            test = line
            j = "".join(test.splitlines())
        else:
            line = line+'/FUZZ'
            test = line
            j = "".join(test.splitlines())
            if args.wordlist !=None:
                if args.output !=None:
                    cmd = "ffuf -u %s -w %s -c -of html -o %s/%s.html -or"%(j,args.wordlist,args.output,out)
                else:
                    cd = os.getcwd()
                    cmd = "ffuf -u %s -w %s -c -of html -o %s/%s.html -or"%(j,args.wordlist,cd,out)

                go = "".join(cmd.splitlines())
                time.sleep(0.10)
                os.system(go)
            else:
                print("Your command is invalid, Please check usage again")

except KeyboardInterrupt:
    print("Process terminated")
    sys.exit(0)
