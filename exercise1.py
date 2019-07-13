documentary = "Apollo 11" 
drama = "Gulliver's Travels" 
comedy = "Diary of a Wimpy Kid"
dramedy = "Boston Legal"
book = "The Pillars of the Earth"

print("Do you enjoy documentaries? yes or no")
my_string1 = str(input())
if my_string1 == "yes":
    print(documentary + " is recommended")
elif my_string1 == "no":
    print("Do you enjoy dramas? yes or no")
    my_string2 = str(input())
    if my_string2 == "yes":
        print("Do you enjoy comedies? yes or no")
        my_string3 = str(input())
        if my_string3 == "yes":
            print(dramedy + " is recommended")
        elif my_string3 == "no":
            print(drama + " is recommended")
    elif my_string2 == "no":
        print("Do you enjoy comedies? yes or no")
        my_string4 = str(input())
        if my_string4 == "yes":
            print(comedy + " is recommended")
        elif my_string4 == "no":
            print(book + " is recommended")