# TwoDictShufflerAndRandPasswdGen
Two dictionary shuffler and random password generator

## Usage
There are two scripts, one is for generating single password, second is for bulk generation.

### Single password generation

How to run: python GenSinglePasswFromTwoDict.py SloMaleNames.txt SloFemaleNames.txt 30

You need to provide two dictionaries, let say male and female names, that will be used for shuffeling. Algorithm will take one or two randomly selected words in one dictionary. Then it will shuffle chosen words from both dictionaries and randomly generetad add-on (which is made up of numbers and/or special character)

First parameter: male names in text file, separated with newline
Second parameter: female names in text file, separated with newline
Third parameter: min length of password. If you set less than 25, or even not provide as third parameter, program will use default 25 as min

### File generator (second python file)

How to run: python GenPasswordsToFile.py config.txt

Same algorithm is applied in generating several dozen passwords, which are stored in "Rezultat.txt". You can set parameters in "config.txt" file.

First parameter: config.txt

config.txt file should contain:
Minimal password length: 25 (note: 25 is minimum, if you set less, 25 will be used as default)
First dictionary file: SloMaleNames.txt
Second dictionary file: SloFemaleNames.txt
Result file: Rezultat.txt
How many randomly generated passwords: 50

Idea is based on project [Python - Random Password Generator ( R.P.G. )](https://github.com/ismailtasdelen/Python-Random-Password-Generator)

Slovenian ancient male and female names were found [Stara izvirna slovenska imena] (https://www.narodne-pesmi.si/?lang=&option=slovenska_imena&stran=Zakladi%20Slovenije)

Why I even did, what I did. Well, several studies suggested that random generated passwords are quite easy to guest to the algorithms. Passwords that use human language are harder to bruteforce.

For eg. password "Xcvc%$54dfg" is much easier to brute force that more human like "NovaStara45_34". That what studies suggest. :)
