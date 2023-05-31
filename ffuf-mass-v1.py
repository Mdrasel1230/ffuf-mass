import os
import sys, time

version = 'v1.0'
site = 'list urls should be contain urls like this format https://site.com/'

print('\n'
r'''                       

  ______ ______ _    _ ______   __  __           _____ _____     
 |  ____|  ____| |  | |  ____| |  \/  |   /\    / ____/ ____| --------------- 
 | |__  | |__  | |  | | |__    | \  / |  /  \  | (___| (___                -
 |  __| |  __| | |  | |  __|   | |\/| | / /\ \  \___ \\___ \    ^_^       -
 | |    | |    | |__| | |      | |  | |/ ____ \ ____) |___) |            -
 |_|    |_|     \____/|_|      |_|  |_/_/    \_\_____/_____/            -
                                                                V1.0   -                                                         
-----------------------------------------------------------------------

  ____          _____                _        __   ___  
 |  _ \        |  __ \              | |      /_ | / _ \ 
 | |_) |_   _  | |__) |__ _ ___  ___| | __   _| || | | |
 |  _ <| | | | |  _  // _` / __|/ _ \ | \ \ / / || | | |
 | |_) | |_| | | | \ \ (_| \__ \  __/ |  \ V /| || |_| |
 |____/ \__, | |_|  \_\__,_|___/\___|_|   \_/ |_(_)___/ 
         __/ |                                          
        |___/                                          
                     ######## We Are ~ErrOr SquaD~ #########

        ''')
print(version)
print(site)

if os.path.isfile('command.txt') == True:
  a = input("Please enter the url list> ")
  b = open(a, "r")
  read = b.readlines()
  out = 0
  auto = open('command.txt').readline()
  for line in read:
    out += 1
    if 'http://' not in line and 'https://' not in line:
        line = 'http://'+line
    line = line+'FUZZ'    
    test = line
    j = "".join(test.splitlines())
    mix = auto%(j,out)
    fire = "".join(mix.splitlines())
    print(fire)
    os.system(fire)
else:
  k = input("Please enter the site list> ")
  print("FFUF will run in default mood")
  word = input("Give me the wordlist full path> ")
  print(word)  
  l = open(k, "r")
  rid = l.readlines()
  o = 0
  for line in rid:
    o += 1
    if 'http://' not in line and 'https://' not in line:
      line = 'http://'+line
    line = line+'FUZZ'    
    test = line
    j = "".join(test.splitlines())
    #print(j)
    com = "ffuf -u %s -w %s -of html -o %s.html"%(j,word,o)
    go = "".join(com.splitlines())
    os.system(go)
print('\n'
r'''  
  _____                     ____                
 |  __ \                   |  _ \               
 | |  | | ___  _ __   ___  | |_) | ___  ___ ___ 
 | |  | |/ _ \| '_ \ / _ \ |  _ < / _ \/ __/ __|
 | |__| | (_) | | | |  __/ | |_) | (_) \__ \__ \
 |_____/ \___/|_| |_|\___| |____/ \___/|___/___/
                                                ''')   
