# importing a module. this time without the argv. This can be added on line 5
import sys

# this is an argument being broken down into 3 variables
script, input_encoding, error = sys.argv

# defining a function called main that has 3 variables
def main(language_file, encoding, errors):
    
    # storing a language file that reads each line in order (readline), inside a variable
    line = language_file.readline()

    # placing a condition
    if line:
        
        # this refers to the next function that is defined 
        print_line(line, encoding, errors)
        
        # if print_line passes then main will fire up
        return main(language_file, encoding, errors)
    
# this function has three variables passed into it 
def print_line(line, encoding, errors):
    
    # this variable stores a variable (that stores the language file that will be read one line ata time)
    # the .strip() removes the empty spaces to the left and right of the language file  
    next_lang = line.strip()
    
    # this variable stores the variable above and stores it in byte form using .encode()
    # 
    raw_bytes = next_lang.encode(encoding, errors=errors)
    
    # this variable stores a debyted version of the variable above that stores the variable that stores the stripped (.strip) language file   
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # this prints the byted version of the language file, a cool random string and the debyted version of the language file
    print(raw_bytes, '<===>', cooked_string)

# this variable opens the text file 
languages = open('languages.txt', encoding='utf-8')

# this is calling the 'main' function and passing in the languages variable and both arguments
main(languages, input_encoding, error)