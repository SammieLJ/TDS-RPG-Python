#!/usr/bin/env python
# -*- conding:utf-8 -*-

# TODO:
# Program has four arguments:
#   - min password length is 25 chars, because algorithm requires this way!
#   - file name: male list
#   - file name: female list
#   - iterations, default is 1
# Read two dictionary files, for male and female names
# Shuffles words from each dictionary and adds randomly gen. numbers with special chars

import string
import random
import sys

def readFileNames(fileName):
    text_file = open(fileName, "r")
    lines = text_file.read().split()
    text_file.close()
    return lines


def random_names_from_list(nameList):
    OnceOrTwice = random.choice([1, 2])  
    names = []
    for index in range (0, OnceOrTwice):
        names.append(random.choice(nameList))
    return names

def getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len):
    male_names = random_names_from_list(male_names_array)
    female_names = random_names_from_list(female_names_array)

    # calculate how much numbers we need to add to max length of password
    maxLenDiff = len(''.join(male_names)) + len(''.join(female_names))
    noNumbers = int(max_password_len) - maxLenDiff

    #print ("Number of Numbers :" + str(noNumbers))

    # set array of number and special chars
    chars = string.digits + "-_"
    numbersAndSpecialChars = ''
    if noNumbers > 0:
        for x in range(0,noNumbers):
            numbersAndSpecialChars += random.choice(chars) 

    final_password = male_names + female_names
    final_password.append(numbersAndSpecialChars)
    
    #debug purposes
    #print("Final prepaired words for password: ", end='')
    #print(final_password);

    random.shuffle(final_password)

    #print("Finall password shuffled: ")
    #print(final_password)
    final_password_str = ''.join(final_password)
    
    #print("Password : " + final_password_str)
    return final_password_str


def two_dictionary_passwd_gen_banner():
	two_dictionary_passwd_gen_banner = """
    ##############################################################
    # PYTHON - Dictionary shuffler and Random Password Generetor #
    ############################################################## 
    #                         CONTACT                            #
    ##############################################################
    #               DEVELOPER : SAMMY 76 LJ                      #
    #          Mail Address : sammy76lj@gmail.com                #
    #     DESC: Loads two dictionaries from file for shuffeling  #
    #     DESC: Shuffles 1 or 2 Slovenian male and female name,  #
    #     DESC: and adds rand. numbers to fill up min 25 chars   #
    #            USAGE: Intended as internal tool, now it's o.s. #
    ##############################################################
	"""
	print(two_dictionary_passwd_gen_banner)

def get_arg(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

def writeDownToFile(genList, fileName):
    # Open a file
    print("Write to file: " + fileName)
    fo = open(fileName, "w+")
    
    # Write sequence of lines at the end of the file.
    fo.writelines( "%s\n" % item for item in genList )    

    # Close opend file
    fo.close()

def main(argv):
    #show ico banner
    two_dictionary_passwd_gen_banner()

    #check if number of parameters are ok
    print("List of arguments: ", end='');print(argv)
    print("No of arguments: " + str(len(argv)))
    if (len(argv) < 1):
        print('Parameters are missing! Enter: config.txt file name!')
        sys.exit(2)

    #Read configuration file called 'config.txt'
    configList = readFileNames(get_arg(1))

    #check if third argument has some value, if not default is 25
    max_password_len = configList[0]
    if not max_password_len:
        max_password_len = 25

    #Value shouldn't be less than 25 chars, because algorithm is not optimized for less
    if int(max_password_len) < 25:
        max_password_len = 25
    print("Maximalna dolžina: " + str(max_password_len))

    male_names_array = readFileNames(configList[1])
    female_names_array = readFileNames(configList[2])

    gendNamesList = []
    for i in range(0,int(configList[4])):
        gendNamesList.append(getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len))

    # Write down names to file
    writeDownToFile(gendNamesList, configList[3])

if __name__ == "__main__":
   main(sys.argv[1:])