# TDS-RPG in Python
Two dictionary shuffler and random password generator (originally called: TwoDictShufflerAndRandPasswdGen)

## Usage
There are two scripts, one is for generating single password, second is for bulk generation.

### Single password generation

How to run: python GenSinglePasswFromTwoDict.py TrendyMaleNames.txt TrendyFemaleNames.txt 30

You need to provide two dictionaries, let say in our case, trendy Slovenian male and female names (you can use nouns and adjectives or smth. similar), that will be used for shuffeling. Algorithm will take one or two randomly selected words in one dictionary. Then it will shuffle chosen words from both dictionaries and randomly generetad add-on (which is made up of numbers and/or special character)

First parameter: male names in text file, separated with newline
Second parameter: female names in text file, separated with newline
Third parameter: min length of password. If you set less than 25, or even not provide as third parameter, program will use default 25 as min. Starts and ends with name. Cannot be started with number or dash/underscore, also cannote be ended with number or dash/score.

Correct format: Malename_34534-4Femalename, f.g.: John_3434-4343_Maia or JohnJack-345434_3465_Julia

Incorrect format: 3434234_GeorgeCarol or Michael-349049Clara785

### File generator (second python file)

How to run: python GenPasswordsToFile.py config.txt

Same algorithm is applied in generating several dozen passwords, which are stored in "Rezultat.txt". You can set parameters in "config.txt" file, to rename Result text file.

First parameter: config.txt

config.txt file should contain:
- minimal password length: 25 (note: 25 is minimum, if you set less, 25 will be used as default)
- first dictionary file: TrendyMaleNames.txt
- second dictionary file: TrendyFemaleNames.txt
- result file: Rezultat.txt
- how many randomly generated passwords: 50

Idea is based on project [Python - Random Password Generator ( R.P.G. )](https://github.com/ismailtasdelen/Python-Random-Password-Generator)

Slovenian ancient male and female names were found [Seznam najpogostejših osebnih imen v Sloveniji] (https://sl.wikipedia.org/wiki/Seznam_najpogostej%C5%A1ih_osebnih_imen_v_Sloveniji)

Why I even did, what I did. Well, several studies suggested that random generated passwords are quite easy to guest to the algorithms. Passwords that use human language are harder to bruteforce. Specially if you use special (for your language) dictionaries and shuffle words from both of them.

For eg. password "Xcvc%$54dfg" is much easier to brute force that more human like "NovaStara45_34". That what studies suggest. :)
