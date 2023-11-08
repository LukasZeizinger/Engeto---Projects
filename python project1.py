"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Lukas Zeizinger
email: zeizingerlukas@gmail.com
discord: Lukáš Zeizinger _nantuko
"""

from string_utils import is_camel_case

from task_template import TEXTS
     
from users import user


total_word = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
sum_of_all_the_numbers = 0

Dict = {"1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0,"8": 0,"9": 0,"10": 0,"11": 0,} 

symbols = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")   


# TODO - zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,

login = str(input(f'Enter username: '))
password = str(input(f'Enter password: '))

# TODO - pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,

if login in user:
    if password == user[login]:
        pass
    else:
        print (f'unregistered user - wrong login, terminating the program..')
        quit()
        
else:
    print (f'unregistered user, terminating the program..')
    quit()
print(f"-"*40)

# TODO - pokud není registrovaný, upozorni jej a ukonči program.

print(f"Welcome to the app,", login)
print(f"We have 3 texts to be analyzed.")
print(f"-"*40)

# TODO - Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:

print ("Enter a number btw. 1 and 3 to select:", end = ' ')
num_texts = int(input())
if 0 < num_texts < 4:
    print(TEXTS[num_texts -1])
else:
    print(f"Number is out of range or undefined symbol")
    quit()
    

# TODO - Pro vybraný text spočítá následující statistiky:

text = TEXTS[num_texts -1].split()


def countword(text):
    listword = text.split()
    return len(listword)

for row in text:
    total_word = total_word + countword(row)

    row = ("".join(k for k in row if k.isalnum()))
    x = str(len(row))
    
    y = Dict.get(x)

    Dict[x] = y + 1   
    
    if row.isnumeric():
        numeric_strings+=1
        sum_of_all_the_numbers += int(row)

    elif row.islower():
        lowercase_words+=1
    
    elif is_camel_case(row):
        titlecase_words+=1
        
    elif row.isupper() and row.isalpha():
        uppercase_words+=1
        
    else:
        titlecase_words+=1
        
print (f"There are",total_word, "words in the selected text.")
print (f"There are ",titlecase_words, " titlecase words.")
print (f"There are ",uppercase_words, " uppercase words.")
print (f"There are ",lowercase_words, "  lowercase words.")
print (f"There are ", numeric_strings, " numeric strings.")
print (f"The sum of all the numbers ", sum_of_all_the_numbers)
print(f"-"*40)
print(f"LEN |    OCCURENCES      |NR.")
print(f"-"*40)


for key, value in Dict.items():
    
    print(f"{key:>3}", "|", value*"*", (17-value)*" ", "|", value)
