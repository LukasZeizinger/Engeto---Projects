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

word_counter = {"1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0,"8": 0,"9": 0,"10": 0,"11": 0,} 

# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,

login = str(input(f'Enter username: '))
password = str(input(f'Enter password: '))

# pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,

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

# pokud není registrovaný, upozorni jej a ukonči program.

print(f"Welcome to the app,", login,"\nWe have 3 texts to be analyzed.\n","-"*40)


# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:

print ("Enter a number btw. 1 and 3 to select:", end = ' ')
num_texts = int(input())
if 0 < num_texts < 4:
    pass
else:
    print(f"Number is out of range or undefined symbol")
    quit()
    

# Pro vybraný text spočítá následující statistiky:

text = TEXTS[num_texts -1].split()

total_word = len(text)


def countword(text):
    listword = text.split()
    return len(listword)

for row in text:

    row = ("".join(k for k in row if k.isalnum()))
    x = str(len(row))
    
    y = word_counter.get(x)

    word_counter[x] = y + 1   
    
    if row.isdecimal():
        numeric_strings+=1
        sum_of_all_the_numbers += int(row)

    elif row.islower():
        lowercase_words+=1
    
    elif row.istitle():
        titlecase_words+=1
    
    else:
        uppercase_words+=1    
    
        
print (f"There are",total_word, "words in the selected text.","\nThere are",titlecase_words, "titlecase words.","\nThere are",uppercase_words, "uppercase words.")
print (f"There are",lowercase_words, "lowercase words.", "\nThere are", numeric_strings, "numeric strings.", "\nThe sum of all the numbers", sum_of_all_the_numbers)
print(f"-"*40, "\nLEN |    OCCURENCES      |NR.","\n","-"*40)

for key, value in word_counter.items():
    
    print(f"{key:>3}", "|", value*"*", (17-value)*" ", "|", value)
