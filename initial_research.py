# importing a module. this time without the argv. This can be added on line 5
import sys

# this is an argument being broken down into 3 variables
script, input_encoding, error = sys.argv

# defining a function called main that has 3 variables.
# language_file = our language file.
# encoding = utf-8 
def main(language_file, encoding, errors):
    
    # storing a language file that reads each line in order (readline), inside a variable
    line = language_file.readline()

    # placing a condition
    # this if statement prevents the loop going on for ever
    # a loop has been created by invoking main (at the bottom) inside the main function (at the top)
    if line:
        
        # this refers to the next function that is defined 
        print_line(line, encoding, errors)
        
        # if print_line passes then main will fire up
        return main(language_file, encoding, errors)
    
# this function has three variables passed into it 
def print_line(line, encoding, errors):
    
    # this variable stores a variable (that stores the language file that will be read one line at a time)
    # the .strip() removes the empty spaces to the left and right of the language file  
    next_lang = line.strip()
    
    # this variable stores the variable above and stores it in byte form using .encode()
    # encoding is passed in is the encoding that I want utf-8
    # the errors=errors is passed in because that is how I want the errors to be handled
    raw_bytes = next_lang.encode(encoding, errors=errors)
    
    # this variable stores a debyted version of the variable above that stores the variable that stores the stripped (.strip) language file 
    # .decode() converts raw bytes into utf-8 strings  
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # this prints the byted version of the language file, a cool random string and the debyted version of the language file
    print(raw_bytes, '<===>', cooked_string)

# this variable opens the text file 
languages = open('languages.txt', encoding='utf-8')

# this is calling the 'main' function and passing in the languages variable and both arguments
main(languages, input_encoding, error)

# binary is converted to bits, bytes are sequences of bits
# bytes can be converted into numbers and letters using unicode.
# utf-8 ensures the right amount of bits are being used (if everything was 32 bit then there would be a lot of wasted space) 
# ascii converts binary into text
# unicode is the grander versions of ascii that can handle 5000000 bits

# DBES (deebes) decode bytes, encode strings

