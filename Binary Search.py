#This program was written by Duc Nguyen on Jan 8, 2020.
#This program will ask the user for a part number. If the part number exists,
#the corresponding part name will be printed. If the part number does not exist,
#an appropriate message will be given to the user. The program will stop when
#the user enters a part number of –1. This program will use the Binary Search
#method

import time

PARTSFILE = "largefile.txt"  #The constant for the largefile text file   

def CreateLists(partnums, partnames,filename):
    """This function accepts 2 empty lists and a filename, then creates a list
    of part numbers and a list of part names from the data in this file"""

    #infile - the file object associated with the text file
    #part - the entity existed in the text file
    #partnums - an empty list to store the part numbers
    #partnames - an empty list to store the part names
    
    infile = open(filename, "r")
    part = infile.readline()
    while part != "":
        partnums.append(int(part.strip()))
        part = infile.readline()
        partnames.append(part.strip())
        part = infile.readline()
    infile.close()

def BinarySearch(partnumber,partnums):
    """This function accepts the user's entered part number and the updated
    list of part numbers"""

    #partnums - the updated list of part numbers
    #partnumber - the user's entered part number
    #first - the first slot number
    #last - the last slot number
    #middle - the middle slot number to be determined

    first = 0
    last = len(partnums)-1
    while first <= last:
        middle = (first + last) // 2
        if partnums[middle] == partnumber:
            return middle
        elif partnums[middle] < partnumber:
                first = middle + 1
        else:
                last = middle -1
    return -1
      
def main(): 
    """ This is the main line for the program"""
    
    #starttime - the time for the program to assemble the data
    #endtime - the total time for the program to assemble the data and analyze
    #          them
    #reply - the user's entered part number
    #slot - the position of the item in the list returned by the Binary Search
    #       function
    
    partnums = []    #Initialize an empty list for the part numbers
    partnames = []  #Initialize an empty list for the part names
    
    
    CreateLists(partnums, partnames,PARTSFILE) #The partnums and partnames lists
                                               #are updated
    reply = int(input("Please enter the part number. Enter -1 to quit "))
    while reply != -1:
        starttime = time.time()
        slot = BinarySearch(reply,partnums)
        endtime = time.time()
        #If the item is not in the list, the Binary Search function returns -1.
        if slot == -1:
            print("Sorry. That part does not exist")
        else:
            print("The corresponding part name is",partnames[slot])
        print("Search time:",endtime - starttime,"seconds")
        reply = int(input("Please enter the part number. Enter -1 to quit "))           
main()
    
