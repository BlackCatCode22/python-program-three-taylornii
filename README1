"""Python Program Three 

Program consists of three major functionalities: 
  1) to be able to add a contact to the contact list called contacts 
  2) to be able to view a list of all the names in your contact list in a user-friendly format
  3) to be able to search contact list and display those contacts

How Program Works:
* main menu: 
  * You're going to input 1 to add contact, 2 to view list, 3 to search contacts, 4 to stay on main menu, or any other key to exit.
  * routing you through these options makes up the main body of the program consisting of many while loops. 
    after each objective is completed you are kicked back to this main menu.

* The the add contact functionality required the most code so I broke it into a few parts:
  * for name: collects a name input, preps the name, validates the name, stores name ready to be added, kicks you to phone input 
  * for phone: collects a phone input, preps the phone, validates the phone, stores phone ready to be added, kicks you to email input
  * for email: collect an email input, preps the email, validates the email, stores email ready to be added, kicks you to add the contact
  * After these are all ready to be added, they are added with function add_contact() which will append the dictionary to your contacts list
    * terms: prepping or cleaning means getting input strings in right format to be able to either search or add them to the data
    * validation assumptions: 
      * name must be alphabetical word(s) i.e. no special chars or numbers. name must not exceed max chars (set to 15). name must be unique 
        (gave user option to overwrite contact with exact match).
      * phone numbers must be either 0, 7, or 10 chars long after prepped. phone numbers must contain only numbers after prepped.
      * emails must be less than 25 chars after prepped. emails must contain an '@' symbol.

* The view contact function consists of a loop to grab all the names, apply formatting for display, put them in a viewing list, 
  sort the list in alphabetical order by first name, and display them

* The search contact function first prompts for search, cleans to searchable format, uses loops to seach contacts that start with the input string 
  and displays these contacts with their info, meanwhile collects all contacts in list to count how many matches


Test Results

input
  ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: 1

input
  new contact name: tay
input
  phone number: 1234567890
input
  email: tay@yahoo.com
output
  new contact added!

input
  ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: 2
output
  Contacts
  Donald Duck
  Minnie M
  Tay
  Taylor Nii
  
input 
  ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: 3
input
  search name: ta
output
  ['ta']
  NAME                PHONE            EMAIL                        
  Taylor Nii          5591234567       tay@gmail.com                
  Tay                 1234567890       tay@yahoo.com                
  2 matches found


ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: a 
goodbye

ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: 1
new contact name: mickey mouse
phone number: 559mick
not a valid phone number.
phone number: 765432!
not a valid phone number.
phone number: 7654321
email: mickeygmail.com
not a valid email.
email: mickey_mouse@gmail.com
new contact added!

ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: 1
new contact name: donald    duck
Donald Duck         5593081234       donduck@gmail.com            
donald duck is already a contact.
do you want to overwrite?(y/n)y
phone number: 781783131894
not a valid phone number.
phone number: 1234567
email: donaldduck@comcast.net
new contact added!

ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: 3
search name: don
['don']
NAME                PHONE            EMAIL                        
Donald Duck         1234567          donaldduck@comcast.net       
1 match found



ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT: 1
new contact name: goofy
phone number: 7654321
phone number:
^^^ This is the error scenerio






Improvements if I had more time:
* There is a bug or design flaw. After the first added contact, will sometimes get stuck in a loop sometime in the process of trying to add another. 
  Have gotten stuck in a loop of inputting phone number.
* More efficent searching.
* Learn to apply the formating or masking better with curly braces
* To be able to search by last name.
* Options to go back.
* Better email validation rules.
