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

    #aditional checkups, check for two rules (starts and ends with char)
    if final_password_str[0].isalpha() == False: 
        print("Word " + final_password_str + " is not by the rules!" + "Prvi char is " + str(final_password_str[0]))
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)

    if final_password_str[len(final_password_str)-1].isalpha() == False:
        print("Word " + final_password_str + " is not by the rules!" + " Zadnji char is " + str(final_password_str[len(final_password_str)-1]))
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)
    
    #check rule there should not be two __ or --
    if final_password_str.find("__") > -1 or final_password_str.find("--") > -1 or final_password_str.find("_-") > -1 or final_password_str.find("-_") > -1:
        print("Word " + final_password_str + " is not by the rules! Najden je znak __ ali -- ali kombinacija _- ali -_ !")
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)
    
    #check rule that every password should have _ or -
    if final_password_str.find("_") == -1 or final_password_str.find("-") == -1:
        print("Word " + final_password_str + " is not by the rules! Ni najden znak _ ali - !")
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)


    #check rule if only chars are in the password
    if final_password_str.isalpha(): 
        print("Word " + final_password_str + " is not by the rules!" + "ALL CHARS, NO NUMBERS OR SPEC. CHARS!")
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)
    
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
    print("Number of passwords to generate " + str(configList[4]))

    male_names_array = toolset.readFileNames(configList[1])
    female_names_array = toolset.readFileNames(configList[2])

    gendNamesList = []
    for i in range(0,int(configList[4])):
        gendNamesList.append(getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len))

    # Write down names to file
    toolset.writeDownToFile(gendNamesList, configList[3])

if __name__ == "__main__":
   main(sys.argv[1:])