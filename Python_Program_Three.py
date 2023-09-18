# Python_Program_Three.py
# Name: Taylor Nii
# Class: CIT-95
# Date: 9/17/2023


contacts = []
name = ""
phone = ""
email = ""
max_chars_name = 15
max_chars_phone = 12
max_chars_email = 25
breathing_room_spaces = 4
header_name = "NAME"
header_phone = "PHONE"
header_email = "EMAIL"
contacts = [{"name": "taylor nii", "phone": "5591234567", "email": "tay@gmail.com"},
            {"name": "donald duck", "phone": "5593081234", "email": "donduck@gmail.com"},
            {"name": "minnie m", "phone": "5596328805", "email": "minniemouse@comacast.net"}]

not_valid_length_message = "not valid length. must not be greater than " + str(max_chars_name) + " chars."
not_alpha_message = "no numbers or special chars."
user_input = "4"
def clean_search_input(searched_name):
    # takes a string, returns a cleaned up string to use for searching
    # "name_temp" is a list of words in string, so you can re-introduce correct amount of spaces between words
    name_temp = searched_name.strip().lower().replace(".", "").split()
    print(name_temp)
    cleaned_name = " ".join(name_temp)
    return cleaned_name

def clean_yn_input(yes_no):
    yes_no_temp = yes_no.lower().replace(".", "").replace(" ", "")
    cleaned_yes_no = yes_no_temp[0]
    return cleaned_yes_no

def clean_num_input(num):
    cleaned_num = num.strip()
    return cleaned_num


def display_entry_header():
    # prints a header that can be used to preface display_entry()
    header_name_cat_spaces = max_chars_name - len(header_name) + breathing_room_spaces
    header_phone_cat_spaces = max_chars_phone - len(header_phone) + breathing_room_spaces
    header_email_cat_spaces = max_chars_email - len(header_email) + breathing_room_spaces
    print("\033[1;4m" + header_name + " " * header_name_cat_spaces + "\033[0m",
          "\033[1;4m" + header_phone+" " * header_phone_cat_spaces + "\033[0m",
          "\033[1;4m" + header_email + " " * header_email_cat_spaces + "\033[0m")


def display_entry(entry):
    # takes dictionary, displays formatted contact info: name, phone, email
    spaces_concat_name = max_chars_name - len(entry["name"]) + breathing_room_spaces
    spaces_concat_phone = max_chars_phone - len(entry["phone"]) + breathing_room_spaces
    spaces_concat_email = max_chars_email - len(entry["email"]) + breathing_room_spaces
    print(entry["name"].title() + " " * spaces_concat_name, entry["phone"] +
          " " * spaces_concat_phone, entry["email"] + " " * spaces_concat_email)


def get_match_index(a_name):
    # looks through contacts and grabs index of matching names // inputs: cleaned name, outputs: index if exact match in contacts
    matches = []
    counter = 0
    for entry in contacts:
        counter += 1
        existing_name = entry.get("name")
        if existing_name == a_name:
            matches.append(entry)
            display_entry(entry)
            index = counter - 1
    num_matches = len(matches)
    if num_matches != 0:
        print(a_name, "is already a contact.")
        return index


def prep_name(a_name):
    # strip, lowercase, no extra spaces // outputs: cleaned name
    name_temp = a_name.strip().lower().split()  # "name_temp" is a list of words in string to add correct amount of spaces
    prepped_name = " ".join(name_temp)
    return prepped_name


def is_unique(a_name):
    # checks for exact matches in contacts// inputs: cleaned name, outputs: bool
    matches = []
    for entry in contacts:
        existing_name = entry.get("name")
        if existing_name == a_name:
            matches.append(entry)
    num_matches = len(matches)
    if num_matches == 0:
        return True
    else:
        return False

def is_valid_length(a_name):
    # checks that name is within set char limit // inputs: cleaned name, outputs: bool
    if len(a_name) <= max_chars_name:
        return True
    else:
        return False

def is_alpha(a_name):
    # checks that name contains only alpha chars // inputs: cleaned name, outputs: bool
    split_name = a_name.split()  # pulled apart into words because .isalpha() set off by spaces
    for i in split_name:
        if i.isalpha() == False:
            return False
    return True


def name_validated(a_name):
    # checks if all requirements met to add name// inputs: cleaned name, outputs: bool
    # valid names are: only alpha chars, strip, lowercase, no extra spaces, <= 15 char
    if is_unique(a_name) == True and is_valid_length(a_name) == True and is_alpha(a_name) == True:
        return True
    elif is_unique(a_name) == False and is_valid_length(a_name) == True and is_alpha(a_name) == True:
        match_index = get_match_index(prepped_name)
        overwrite = input("do you want to overwrite?(y/n)")
        overwrite = clean_yn_input(overwrite)
        if overwrite == "y":
            del contacts[match_index]
            return True
        elif overwrite == "n":
            return False
    else:
        return False


def prep_phone(a_phone):
    phone_temp = a_phone.replace(" ", "").replace("-", "").replace(")", "")
    prepped_phone = phone_temp.replace("(", "").replace(".", "")
    return prepped_phone

def is_valid_phone_len(a_phone):
    if len(a_phone) == 7 or len(a_phone) == 10 or len(a_phone) == 0:
        return True
    else:
        return False

def is_numeric(a_phone):
    if a_phone.isnumeric():
        return True
    else:
        return False

can_move_on_phone = False
can_move_on_email = True
def phone_validated(a_phone):
    global can_move_on_phone
    while can_move_on_phone == False:
        if is_valid_phone_len(a_phone) == True and is_numeric(a_phone) == True:
            can_move_on_phone = True
            return True
        else:
            print("not a valid phone number.")
            return False


def add_contact(a_contact):
    contacts.append(a_contact)
    print("new contact added!\n")


def view_contacts():
    # displays the name of each individual in contacts in alphabetical order
    print("\033[1;4m" + "Contacts" + "\033[0m")  # bolded and underlined header
    viewing_list = []
    for entry in contacts:
        # retrieves contact names, applies formatting, puts them in a viewing list
        contact_for_viewing = entry.get("name").title()
        viewing_list.append(contact_for_viewing)
    viewing_list.sort()  # alphabetizes viewing list by first letter
    for i in viewing_list:
        print(i)  # print alphabetized viewing list
    print("\n")


def search_contacts():
    # prompts user for name to search, displays all contacts that start with the searched name, returns number of matches
    searched_name = input("search name:\n")
    searched_name = clean_search_input(searched_name)  # gets inputted name in searchable format
    matches = []
    display_entry_header()
    for entry in contacts:
        existing_name = entry.get("name")
        if existing_name.startswith(searched_name):
            matches.append(entry)
            display_entry(entry)
    num_matches = len(matches)
    if num_matches == 1:
        print(num_matches, "match found")
    else:
        print(num_matches, "matches found")
    return num_matches


# program main body

contact_stage = "name"
while user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4":  # reserving "4" to bring user back to main menu
    user_input = input("ENTER 1 to ADD new contact, 2 to VIEW contact list, 3 to SEARCH, 4 to stay on MENU, or ANY other key to EXIT:\n")
    user_input = clean_num_input(user_input)
    while user_input == "1":
        # this while loop is for adding contact
        while contact_stage == "name":
            name_input = input("new contact name:\n")
            prepped_name = prep_name(name_input)
            if name_validated(prepped_name) == True:
                name = prepped_name
                contact_stage = "phone"  # after valid name collected, pushes you out to next stage
            else:
                if is_valid_length(prepped_name) == False:
                    print(not_valid_length_message)
                if is_alpha(prepped_name) == False:
                    print(not_alpha_message)
        while contact_stage == "phone":
            phone_input = input("phone number:\n")
            prepped_phone = prep_phone(phone_input)
            if phone_validated(prepped_phone) == True:
                phone = prepped_phone
                contact_stage = "email"  # after valid phone number collected, pushes you out to next stage
        while contact_stage == "email":
            email_input = input("email:\n")
            email_input = email_input.replace(" ", "").lower()
            at_count = email_input.count("@")
            if at_count > 0:
                email = email_input
                contact_stage = "add contact"  # after valid email collected, pushes you out to next stage
            else:
                print("not a valid email.")
        while contact_stage == "add contact":
            new_contact = {"name": name, "phone": phone, "email": email}
            add_contact(new_contact)
            contact_stage = "next"  # after valid email collected, pushes you out to next stage
        user_input = "4"
        contact_stage = "name"
    while user_input == "2":
        view_contacts()
        user_input = "4"
    while user_input == "3":
        search_contacts()
        user_input = "4"
print("goodbye")
