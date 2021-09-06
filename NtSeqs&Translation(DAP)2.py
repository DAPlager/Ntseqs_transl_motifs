# CS368 - Programming Assignment 1, problems 1, 2, 3, and 4
# Description: DNA reverse complement, reverse palindromes,
#              and translation from all six reading frames.
# Filename: NtSeqs&Translation(DAP)2.py
# Author: Doug Plager
# Date: 2/1/2020


# Generates reverse complement of a DNA seq argument.
def dna_revc( dna_seq ):            # Problem 1
    
    dna_seq = dna_seq.upper()       # DNA seq into upper case and reassigned to dna_seq.

    # Reverse traversal and complementation of the input DNA sequence.
    revc_seq = ''
        
    for nt in dna_seq[ : : -1 ]:    # Backward iteration thru 'dna_seq' string.
        
        if nt == 'A':               # Building the reverse complement sequence
            revc_seq += 'T'         # from 5' to 3'.
        elif nt == 'C':
            revc_seq += 'G'
        elif nt == 'G':
            revc_seq += 'C'
        elif nt == 'T':
            revc_seq += 'A'
        else:
            revc_seq += '?'
            
    # NOTE: Could "save" the rev. complement with 'File' functions if desired.
    
    return revc_seq


# Identifies the reverse palindromic seqs of the specified length for an input DNA seq.
# Calls dna_revc( _ ).
def rev_palindromes( dna_seq, palin_size ):    # Problem 2
    
    dna_seq = dna_seq.upper()       # DNA seq into upper case and reassigned.
    print()
    
    # "Extract" substrings of the specified size across the DNA sequence.
    start_nt = 1
    num_of_palin = 0
    result = ''
    
    for i in range( 0, len( dna_seq ) - palin_size + 1, 1 ):   # Avoids traversal beyond
                                                               # the end of the dna_seq.
        dna_substr = dna_seq[ i : i + palin_size ]  # Substrings of approp. length;
                                                    # REM: non-inclusive 'right' index. 
        
        revc_seq = dna_revc( dna_substr )   # Generate the substr's reverse complement.
        
        if dna_substr == revc_seq:          # Check for reverse palindromicity.
            result = result + ( "\nPalindromic sequence:  5'-" + dna_substr + 
                                "-3'  at position " + str( start_nt ) )
            
            num_of_palin += 1    # Helps identify if no rev palindromes were found.
            
        start_nt += 1            # Tracks the starting nt of each rev palindrome.
    
    if num_of_palin == 0:
        result = "\nNo palindromic sequences found."
        
     # NOTE: Could "save" identified palindromes and their positions w/ File functions.
    
    return result


# Converts a DNA Coding Strand sequeance to the corresponding mRNA sequence.    
def transcription( dna_seq ):

    rna = dna_seq.replace('T', 'U')   # .replace() string function, Python Standard Library.
    
    return rna


# Translates a "raw" RNA seq into its three possible amino acid seqs (3 reading frames).
def rna_3rf_translation( rna_seq ):    # Central component of Problem 3;
                                       # also see main() menu option 3.

    # RNA codon table/dictionary (from Rosalind Project)
    rna_codon_table = {
        'UUU' : 'F',    'CUU' : 'L',     'AUU' : 'I',     'GUU' : 'V',
        'UUC' : 'F',    'CUC' : 'L',     'AUC' : 'I',     'GUC' : 'V',
        'UUA' : 'L',    'CUA' : 'L',     'AUA' : 'I',     'GUA' : 'V',
        'UUG' : 'L',    'CUG' : 'L',     'AUG' : 'M',     'GUG' : 'V',
        'UCU' : 'S',    'CCU' : 'P',     'ACU' : 'T',     'GCU' : 'A',
        'UCC' : 'S',    'CCC' : 'P',     'ACC' : 'T',     'GCC' : 'A',
        'UCA' : 'S',    'CCA' : 'P',     'ACA' : 'T',     'GCA' : 'A',
        'UCG' : 'S',    'CCG' : 'P',     'ACG' : 'T',     'GCG' : 'A',
        'UAU' : 'Y',    'CAU' : 'H',     'AAU' : 'N',     'GAU' : 'D',
        'UAC' : 'Y',    'CAC' : 'H',     'AAC' : 'N',     'GAC' : 'D',
        'UAA' : '*',    'CAA' : 'Q',     'AAA' : 'K',     'GAA' : 'E',
        'UAG' : '*',    'CAG' : 'Q',     'AAG' : 'K',     'GAG' : 'E',
        'UGU' : 'C',    'CGU' : 'R',     'AGU' : 'S',     'GGU' : 'G',
        'UGC' : 'C',    'CGC' : 'R',     'AGC' : 'S',     'GGC' : 'G',
        'UGA' : '*',    'CGA' : 'R',     'AGA' : 'R',     'GGA' : 'G',
        'UGG' : 'W',    'CGG' : 'R',     'AGG' : 'R',     'GGG' : 'G' 
    }

    # Translates the three reading frames of the input RNA seq into three aa seqs.
    result = ''
    
    for j in range( 0, 3 ):
        rf_seq = rna_seq[ j : ]      # RNA seq substrings of the three reading frames.
        num_of_codons = len( rf_seq ) // 3    # Determines the number of "full" codons.

        # Sequentially translates each of the three 'rf_seq' reading frame substrings.
        peptide = ''
        
        for i in range( 0, num_of_codons ): 
            codon = rf_seq[ i*3 : i*3+3 ]          # Substring of each 3-nt codon.

            amino_acid = rna_codon_table[ codon ] # Codon 'key'/index maps to its aa
                                                  # in the 'rna_codon_table' dictionary.
            peptide = peptide + amino_acid  # Building aa sequence.       
            
            if amino_acid == '*':           # 'Stop' codon termination of aa seq.
                break
            
        result = result + peptide + '\n'    # Accumulation of all three rf results.

    return result


def main( ):
    
    # Menu for the three functions for Problems 1, 2, & 3 of Prog Assignment 1.
    flag = True
    
    try:
        while flag == True:
            
            option = int( input( "\n\nWhich function would you like to perform: \n" +
                            "    1) Reverse complement of a DNA sequence \n" +
                            "    2) Reverse palindromes in a DNA sequences \n" +
                            "    3) Amino acid sequence translated from a DNA sequence \n" +
                            "    4) Exit \n" +
                            "Enter your numeric choice: ") )
    
            if option == 1:
                dna_seq = input( "\nPlease enter the 5'-to-3' DNA sequence for \n" +
                            "which you would like the reverse complement sequence: " )
                dna_seq = dna_seq.upper()     # DNA seq into upper case and reassign.
                
                # Confirming valid DNA sequence.
                dna_nt_set = { 'A', 'C', 'G', 'T' }  
                for nt in dna_seq:
                    if nt not in dna_nt_set:
                        print( '\nPlease try again. Enter DNA sequence with only A, C, G, or T.' )
                        return
                
                revc_seq = dna_revc( dna_seq )    # Call reverse complement function.

                # Display the returned reverse complement 5'-to-3'.
                print( "\nThe starting DNA sequence was:  5'-", dna_seq, "-3'" +
                    "\nThe reverse complement sequence is:  5'-", revc_seq, "-3'" )
            
            elif option == 2:
                dna_seq = input( "\nPlease enter the 5'-to-3' DNA sequence for \n" +
                            "which you would like the reverse palindromes: " )
                dna_seq = dna_seq.upper()
                
                # Confirming valid DNA sequence.
                dna_nt_set = { 'A', 'C', 'G', 'T' }  
                for nt in dna_seq:
                    if nt not in dna_nt_set:
                        print( '\nPlease try again. Enter DNA sequence with only A, C, G, or T.' )
                        return
                
                palindrome_size = int( input(
                                "\nAnd the nucleotide length of the reverse \n" +
                                "palindromes you would like to identify? " ) )
                                       
                result = rev_palindromes( dna_seq, palindrome_size )   # Function call & return.
                
                # Display the returned reverse palindrome result.
                print( "The starting DNA sequence was:  5'-", dna_seq, "-3'\n" + result )
                
            elif option == 3:
                dna_seq = input( "\nPlease enter a single 5'-to-3' DNA sequence that \n" +
                            "you would like translated in both directions: " )
                
                dna_seq = dna_seq.upper()
                
                # Confirming valid DNA sequence.
                dna_nt_set = { 'A', 'C', 'G', 'T' }  
                for nt in dna_seq:
                    if nt not in dna_nt_set:
                        print( '\nPlease try again. Enter DNA sequence with only A, C, G, or T.' )
                        return
                
                # Generate reverse complement of input DNA sequence.
                revc_seq = dna_revc( dna_seq )
                
                # Convert each DNA (coding/sense) strand to its respective upper case
                # mRNA sequence (U for T).
                print( "\nThe starting DNA sequence was:  5'-", dna_seq, "-3'" )
                rna_seq = transcription( dna_seq )
                print( "\nThe forward transcript is:  5'-", rna_seq, "-3'" )
                revc_rna_seq = transcription( revc_seq )
                print( "The backward transcript is:  5'-", revc_rna_seq, "-3'" )  
                
                # Generate the translated amino acid sequences and display them.
                print( "\nForward reading frames:" )
                forward_result = rna_3rf_translation( rna_seq )
                print( forward_result )
                
                print( "Backward reading frames:" )
                backward_result = rna_3rf_translation( revc_rna_seq )
                print( backward_result )
                
            elif option == 4:
                flag = False    # Exit
            
            else:
                flag = False    # Integer entry other than 1 to 4.
            
    except:
        print( "\nPlease try again.  Enter a numeric choice (1, 2, 3, or 4)." )

    return

if __name__ == '__main__':    # To avoid execution of main() if imported; only
    main()                    # executed if 'Run' directly (I still need to understand).

# main()    # 'main()' function call as an alternative execution trigger to 'Run'. 
    
    
    