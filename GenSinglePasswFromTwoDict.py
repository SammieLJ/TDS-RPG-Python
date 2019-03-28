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

import toolset
import string
import random
import sys

#set (global) recursion counter for method getRandomAndShuffledPassword (it will be called more than No of passes to gen.)
genRandPasses = 0

def AddOneToGenRandPasses():
    global genRandPasses
    genRandPasses += 1

def getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len):
    AddOneToGenRandPasses()
    male_names = toolset.random_names_from_list(male_names_array)
    female_names = toolset.random_names_from_list(female_names_array)

    # calculate how much numbers we need to add to max length of password
    maxLenDiff = len(''.join(male_names)) + len(''.join(female_names))
    noNumbers = int(max_password_len) - maxLenDiff

    # set array of number and special chars
    chars = string.digits + "-_"
    numbersAndSpecialChars = ''
    if noNumbers > 0:
        for x in range(0,noNumbers):
            numbersAndSpecialChars += random.choice(chars) 

    #final_password = [male_names,female_names,numbersAndSpecialChars]
    final_password = male_names + female_names
    final_password.append(numbersAndSpecialChars)
    print("Prepaired words for password: ", end='')
    print(final_password)

    random.shuffle(final_password)

    print("Final password shuffled: ", end='')
    print(final_password)
    final_password_str = ''.join(final_password)

     #aditional checkups, check for two rules (starts and ends with char)
    if final_password_str[0].isalpha() == False: 
        print("Word " + final_password_str + " is not by the rules!" + "First char is '" + str(final_password_str[0]) + "'")
        print()
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)

    if final_password_str[len(final_password_str)-1].isalpha() == False:
        print("Word " + final_password_str + " is not by the rules!" + "Last char is '" + str(final_password_str[len(final_password_str)-1]) + "'")
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)
    
    #check rule there should not be two __ or --
    if final_password_str.find("__") > -1 or final_password_str.find("--") > -1 or final_password_str.find("_-") > -1 or final_password_str.find("-_") > -1:
        print("Word " + final_password_str + " is not by the rules! Found char is __ or -- or combination of _- -_")
        print()
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)
    
    #check rule that every password should have _ or -
    if final_password_str.find("_") == -1 or final_password_str.find("-") == -1:
        print("Word " + final_password_str + " is not by the rules! Mandatory char _ or - was not found")
        print()
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)


    #check rule if only chars are in the password
    if final_password_str.isalpha(): 
        print("Word " + final_password_str + " is not by the rules!" + "JUST ALL CHARS, NO NUMBERS OR SPEC. CHARS!")
        print()
        final_password_str = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)    

    return final_password_str

def main(argv):
    #check if no of parameters is ok
    if (len(argv) < 2):
        print('Parameters are missing! Enter: male_txt_file female_txt_file (optional max_len) ')
        sys.exit(2)

    #show banner
    toolset.two_dictionary_passwd_gen_banner()

     #check if number of parameters are ok
    print("List of arguments: ", end='');print(argv)
    print("No of arguments: " + str(len(argv)))

    #check if third argument has some value, if not default is 25
    max_password_len = toolset.get_arg(3)
    if not max_password_len:
        max_password_len = 25

    #Value shouldn't be less than 25 chars, because algorithm is not optimized for less
    if int(max_password_len) < 25:
        max_password_len = 25

    male_names_array = toolset.readFileNames(argv[0])
    female_names_array = toolset.readFileNames(argv[1])
    
    fina_password = getRandomAndShuffledPassword(male_names_array, female_names_array, max_password_len)

    print()
    print("Generated passes: " + str(genRandPasses) + "/1")

    print("Password : " + fina_password)

if __name__ == "__main__":
   main(sys.argv[1:])