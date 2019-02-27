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
    
    print("Password : " + final_password_str)

if __name__ == "__main__":
   main(sys.argv[1:])