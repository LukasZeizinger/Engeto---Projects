"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Lukas Zeizinger
email: zeizingerlukas@gmail.com
discord: Lukáš Zeizinger _nantuko
"""

import collections

from task_template import TEXTS
     
from users import users

def _input_log_and_pass():
    """Input login and password.
    If login/password is not correct; terminating the program."""

    while True:
        try:
            login = str(input(f'Enter username: '))
            password = str(input(f'Enter password: '))
            print(f"-"*40) 
        except ValueError:
            print("Please enter correct login and password. Try again ...")
            continue
        if login in users:
            
            if password == users[login]:
                print("Welcome to the app, ", login,"\nWe have ",(len(TEXTS)),
                " text" + str("s" if len(TEXTS) > 1 else "") + 
                " to be analyzed.\n", sep="")

                print(f"-"*40)   
                break
            else:
                continue
        else:
            print(f'unregistered user - wrong login, terminating the program.')
            quit()
    return    

def _inputnumber():
    """Input integer must be in range. 
    If it is out of range program terminated."""

    while True:
        try:
            print("Enter a number btw. 1 and", (len(TEXTS))," :", end = ' ')
            num_texts = int(input())
        except ValueError:
            print("Undefined symbol ..., sorry")
            quit()
        if 0 < num_texts < (len(TEXTS)+1):
            print(f"-"*40) 
            return num_texts
        else:
            print(f"Number is out of range or undefined symbol")
            quit()

def _library_of_words_len():
    """Automatically generate a dictionary of word lengths.
    If the counter is None, create a new key in the dictionary.
    If the key is in the dictionary, increment the value."""
    len_of_the_word = str(len(row))
    counter = word_counter.get(len_of_the_word)

    if counter is None:
        word_counter[len_of_the_word] = 1
    else:
        word_counter[len_of_the_word] = counter + 1

    return
        

def get_len(key):
    return len(key[0])

#def are_or_is(a_i_word):
    """Mechanism for choosing singular or plural form of word"""
    return "are" if a_i_word > 1 else "is"

total_word = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
tresh = 0
sum_of_all_the_numbers = 0

word_counter = {} 

_input_log_and_pass()

# Pro vybraný text spočítá následující statistiky:

text = TEXTS[_inputnumber() - 1].split()

total_word = len(text)

for row in text:
    row = "".join(k for k in row if k.isalnum())
    _library_of_words_len()

    if row.isdecimal():
        numeric_strings += 1
        sum_of_all_the_numbers += int(row)
    elif row.isupper() and row.isalpha():
        uppercase_words += 1
    elif row.islower():
        lowercase_words += 1
    elif row.istitle():
        titlecase_words += 1
    
       
print(
    f"There {'are' if total_word > 1 else 'is'} {total_word} "
    f"word{'s' if total_word > 1 else ''} in the selected text.",
    f"\nThere {'are' if titlecase_words > 1 else 'is'} {titlecase_words} "
    f"titlecase word{'s' if titlecase_words > 1 else ''}.",
    f"\nThere {'are' if uppercase_words > 1 else 'is'} {uppercase_words} "
    f"uppercase word{'s' if uppercase_words > 1 else ''}.",
    f"\nThere {'are' if lowercase_words > 1 else 'is'} {lowercase_words} "
    f"lowercase word{'s' if lowercase_words > 1 else ''}.",
    f"\nThere {'are' if numeric_strings > 1 else 'is'} {numeric_strings} "
    f"numeric string{'s' if numeric_strings > 1 else ''}.",
    f"\nThe sum of all the numbers {sum_of_all_the_numbers}"
)

print(f"-"*40, "\nLEN |    OCCURENCES      |NR.","\n","-"*40)


# initializing dictionary

s_word_counter = collections.OrderedDict(sorted(word_counter.items()))

# sorting using sort()
# external to render logic 
list_of_library = list(s_word_counter.items())
list_of_library.sort(key = get_len)
 
# reordering to dictionary
sorted_library = {ele[0] : ele[1]  for ele in list_of_library}
for key, value in sorted_library.items():
    
    print(f"{key:>3}", "|", value*"*", (17-value)*" ", "|", value)
