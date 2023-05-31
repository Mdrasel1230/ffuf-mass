# ffuf-mass v1.0

## Usage:
You can use this script in two ways
### 1.Default :
`cd ffuf-mass`

`python ffuf-mass-v1.py`

1. Give your List.txt urls should be contain urls like this format https://site.com/

2. Then give wordlist full path like: /your/wordlist.txt

output will save randomely, like for first website output will be 1.html

### 2. Permanent Usage:

1. For this you have to create a file which is `command.txt`

2. This `command.txt` should contains your own command, 
Like: `ffuf -u %s -w /yourwordlist/path/word.txt -of html -o %s.html`

3. Just don't change the `-u %s` and `-of html -o %s.html` [By the way you can change the html format to any which is supported by ffuf]

For Ex: `ffuf -u %s -w /yourwordlist/path/word.txt -of json -o %s.json`

Note: You can add also your own command/attribute which you use in ffuf but don't change the `-u %s` and `-of html -o %s.html` format

# Demo:
https://asciinema.org/a/362816

# Happy Hacking!
