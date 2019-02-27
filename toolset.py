import sys
import random

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