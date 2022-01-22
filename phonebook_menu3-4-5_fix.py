import sys
from collections import OrderedDict
from collections import Counter



def addRecord():
    firstname = input('What is your first name? ')
    surname = input('What is your surname? ')
    phonenumber = input('What is your phonenumber? ')
    

    for x in phonebook:
        if firstname == phonebook[x].get('firstname') and surname == phonebook[x].get('surname'):
            print('The contact is already in the phonebook')
            break
        else:
            print('The contact has been added to the phonebook')
            phonebook[len(phonebook) + 1] = {'firstname': firstname, 'surname': surname, 'phonenumber': phonenumber}

        return



def deleteRecord(d):
    deleteFirstname = input('What is the first name of the contact you want to delete? ')
    deleteSurname = input('What is the surname of the contact you want to delete? ')

    for x in d:
        if deleteFirstname == d[x].get('firstname') and deleteSurname == d[x].get('surname'):
            del d[x]
            print('The contact has been deleted')
            return d
    print('The contact is not in the phonebook')

def duplicate(d):
    dupl_firstname = input('What is the contact\'s first name? ')
    dupl_surname = input('What is the contact\'s surname? ')

    for x in d:
        if dupl_firstname == d[x].get('firstname') and dupl_surname == d[x].get('surname'):
            print('The contact is already in the phonebook')
            return d
    print('The contact is not in the phonebook')

def changeRecord(d):

    changeFirstname = input('What is the contact\'s first name? ')
    changeSurname = input('What is the contact\'s surname? ')
    print(' ')

    for x in d:
        if changeFirstname == d[x].get('firstname') and changeSurname == d[x].get('surname'):
            print('Please put in the contact\'s new information: ')
            
            return d
    print('The contact is not in the phonebook')


def listFirstname():

    print(sorted(phonebook, key=lambda x: (phonebook[x]['firstname'])))

    sortedphonebook = OrderedDict(sorted(phonebook.items(), key=lambda x: (phonebook[1]['firstname'])))
    print(sortedphonebook)


def listSurname():
    sortedSurname = phonebook.items()
    print(sortedSurname)

    for pNumber, pInfo in phonebook.items():
        
        for key in pInfo:
            print(key + ':', pInfo[key])

        for pNumber, pInfo in phonebook.items():
           
            for key in pInfo:
                print(key + ':', pInfo[key])



def samePhonenumber(d):

    '''
    encountered_entries = set()
    for key, entry in d.items():
        if (entry['phonenumber']) in encountered_entries:
            print(d[key])
        else:
            encountered_entries.add((entry['phonenumber']))
    '''

    c = Counter(x for xs in d.values() for x in xs)
    print(c)

    d_dups = {k: [v for v in vs if c[v] > 1] for k, vs in d.items()}

    print(d_dups)


menu = {0: ''}


def mainmenu():

    while True:
        options = list(menu.keys())


        for choosing in options:
            selection = input("""

                                  ----MENU----
                              1: List the phonebook
                              2: Add a new 
                              3: Delete                               
                              4: Quit/Log Out

                              Please enter your choice: """)
            print(' ')

            if selection == '1':
                for pNumber, pInfo in phonebook.items():
                    
                    for key in pInfo:
                        print(key + ':', pInfo[key])
            elif selection == '2':
                addRecord()
            elif selection == '3':
                deleteRecord(phonebook)
            elif selection == '4':
                duplicate(phonebook)
            elif selection == '5':
                changeRecord(phonebook)
            elif selection == '6':
                listFirstname()
            elif selection == '7':
                listSurname()
            elif selection == '8':
                samePhonenumber(phonebook)
            elif selection == '9':
                return False
            else:
                print('Please choose a valid number')
                # end of mainmenu function

mainmenu() # this is what starts the mainmenu function
