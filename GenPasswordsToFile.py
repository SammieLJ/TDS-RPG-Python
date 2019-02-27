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
import toolset

def getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len):
    male_names = toolset.random_names_from_list(male_names_array)
    female_names = toolset.random_names_from_list(female_names_array)

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


def main(argv):
    #show ico banner
    toolset.two_dictionary_passwd_gen_banner()

    #check if number of parameters are ok
    print("List of arguments: ", end='');print(argv)
    print("No of arguments: " + str(len(argv)))
    if (len(argv) < 1):
        print('Parameters are missing! Enter: config.txt file name!')
        sys.exit(2)

    #Read configuration file called 'config.txt'
    configList = toolset.readFileNames(toolset.get_arg(1))

    #check if third argument has some value, if not default is 25
    max_password_len = configList[0]
    if not max_password_len:
        max_password_len = 25

    #Value shouldn't be less than 25 chars, because algorithm is not optimized for less
    if int(max_password_len) < 25:
        max_password_len = 25
    print("Maximalna dolžina: " + str(max_password_len))

    male_names_array = toolset.readFileNames(configList[1])
    female_names_array = toolset.readFileNames(configList[2])

    gendNamesList = []
    for i in range(0,int(configList[4])):
        gendNamesList.append(getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len))

    # Write down names to file
    toolset.writeDownToFile(gendNamesList, configList[3])

if __name__ == "__main__":
   main(sys.argv[1:])