# CS368 - Programming Assignment 2
# Description: Finding motifs (consensus sequences) within a given sequence
#              using regular expressions.
# Filename: RegEx_Motifs(DAP)2.py
# Author: Doug Plager
# Date: 4/18/2020

import re   #Importing the re.py (regular expressions) module of RegEx functions.

def motif_search( seq_file, motif_file ):
    
    #Reading the entire raw sequence into a string.
    f1 = open( seq_file, 'r' )
    seq_str = f1.read()
    
    seq_str = re.sub( r"\n", "", seq_str ) #Removing any new line characters.
    seq_str = seq_str.upper()              #Choosing to make sure sequence is uppercase.
    
    f1.close()
    
    #Reading the entire motif pattern into a string.
    f2 = open( motif_file, 'r' )
    motif_str = f2.read()
    
    motif_str = re.sub( r"\n", "", motif_str )   #Removing any new line characters, just
                                                 #in case.
    motif_str = motif_str.upper()   #Assuming .upper() only affects lowercase letters?!
    
    #Searching for NON-OVERLAPPING pattern matches.
    matches = re.finditer( motif_str, seq_str )   #Returns a 'callable iterator' list
            #of non-overlapping match objects, which apparently should be cast to a
            #true Python 'list' for better handling (see Commments in my preceding
            #version, RegEx_Motifs(DAP).py)!!
    
    match_list = list( matches )    #Casting a callable iterator to a true list.
    
    return match_list
    

def main():
    
    flag = True
    
    while flag:
    
        try:
            #Asking for the amino acid or nucleotide sequence to be searched with a
            #user-input motif (consensus) sequence pattern.
            seq_file = input( "\nPlease enter the name of the file containing" +
                               "\nthe raw sequence to be searched (e.g., ALP.txt): " )
            
            f1 = open( seq_file, 'r' )   #Checking that the seq. file is accessible.
            f1.close()
            
            #Asking for the motif pattern file.
            motif_file = input( "\nPlease enter the name of the .txt file containing" +
                                "\nthe RegEx motif pattern you want to search for: " )
            
            f2 = open( motif_file, 'r' )  #Checking that the motif file is accessible.
            f2.close()
            
            #Calling the motif search function; returns a 'list' of match objects.
            match_list = motif_search( seq_file, motif_file )
            
            #Determining if returned 'list' is empty or printing out match object info.
            if len( match_list ) == 0:
                print( "\nNo matching motif (as indicated in " + motif_file + ")" +
                       "\nwas found in the " + seq_file + " sequence." )
            else:
                print()
                for m in match_list:
                    print( "Motif " + m.group() + " found at position " +
                           str(m.start()+1) + "." )
                    
            answer = input( "\nWould you like to do another motif search (yes or no)? " )
            if answer != "yes":
                flag = False

        except IOError:    #Catches the error if the above input file is not accessible.
            print( "\nThe file cannot be found or opened." )
            answer = input( "Would you like to try again (yes or no)? " )
            
            if answer != "yes":
                flag = False
            
        except Exception as err:  #Catches most other non-Syntax Type errors, presumably.
            print( "\nUnexpected error: " + str(err) )  #NOTE: Only prints out the 
            return                                      #error description, but not the  
                                                        #line number info for the error.
    
    print( "\nThank you for using this program." )
    return


if __name__ == "__main__":   # To avoid execution of main() if imported; only
    main()                   # executed if 'Run' directly.