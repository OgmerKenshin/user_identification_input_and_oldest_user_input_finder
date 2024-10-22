
# I'm gonne set rules for what names are valid and what names aren't
def is_valid_name(name):
    return name.replace(" ", "").isalpha()
def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 122
# I will return the age and name for the "oldest person"
def get_oldest_person(data):
    if len(data) == 0:
        return None, None
    oldest_person = max(data, key=lambda person: person[1])
    return oldest_person


# Now the array is where the names and ages are stored
#this will be the array
Identification = []

#I can now proceed to making loops and user input texts
while True:
    name = input("please enter your name here: ")
    while not is_valid_name(name):
        print("HAHA wrong!!! names should consist of letters and spaces only, if not then that's just sad man")
        name = input("please enter your name here: ")


    age = input("please enter your age here: ")
    while not is_valid_age(age):
        print("seriously? dude...")
        age = input("please input your age here: ")

    # the age variable needs to be an integer and both variables are now stored in the array set earlier
    age = int(age)
    Identification.append((name,age))

    #retry and finally the break
    retry = input("do you wanna input another entry? (Yes or No): ").strip().lower()
    if retry != "yes": 
        break


# find and reveal the oldest person
oldest = get_oldest_person(Identification)
if oldest:
    print(f"the oldest person is {oldest[0]} with {oldest[1]}.")
else: 
    print("No valid entries")
       
            

        
            
        
          