
# I'm gonne set rules for what names are valid and what names aren't
def valid_name(name):
    return name.replace("","").isalpha()
def valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 122
# I will return the age and name for the "oldest person"
def oldest_user(data):
    if len(data) == 0:
        return None, None
    oldest_user = max(data, key=lambda person: person[1])
    return oldest_user


# Now the array is where the names and ages are stored
#this will be the array
Identification = {}

#I can now proceed to making loops and user input texts
while True:
    name = input("please enter your name here: ")
    while not valid_name(name):
        print("HAHA wrong!!! names should consist of letters and spaces only, if not then that's just sad man")
        name = input("please enter your name here: ")


    age = input("please enter your age here: ")
    while not valid_age(age):
        print("seriously? dude...")
        age = input("please input your age here: ")
        

       
            

        
            
        
          