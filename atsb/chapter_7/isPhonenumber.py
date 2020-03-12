#Finding pattern of text without regular expressions

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
def isPhoneNumber2():
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i : i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)

    print('done')

# finding pattern of text with regualr expressions
def findwithregex():        
    ## Creating Regex Objects
    import re # importing regex module 
    # phoneNumRegex contains regex object
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search('I got this number 989-278-4657, catch or not')
    return print('Phone number found: ' + mo.group())
    #matching regex object 
