documentary = "Apollo 11" 
drama = "Gulliver's Travels" 
comedy = "Diary of a Wimpy Kid"
dramedy = "Boston Legal"
book = "The Pillars of the Earth"

print("rate your appreciation for documentaries on a scale from 1 to 5")
rating1 = int(input())
if rating1 >= 4 and rating1 <= 5:
    print(documentary + " is recommended")
elif rating1 >= 1 and rating1 <= 3:
    print("rate your appreciation for comedies on a scale from 1 to 5")
    rating2 = int(input())
    if rating2 >= 4 and rating2 <= 5:
        print("rate your appreciation for dramas on a scale from 1 to 5")
        rating3 = int(input())
        if rating3 >= 4 and rating3 <= 5:
            print(dramedy + " is recommended")
        elif rating3 >= 1 and rating3 <= 3:
            print(comedy + " is recommended")
    elif rating2 >= 1 and rating2 <= 3:
        print("rate your appreciation for dramas on a scale from 1 to 5")
        rating4 = int(input())
        if rating4 >= 4 and rating4 <= 5:
            print(drama + " is recommended")
        elif rating4 >= 1 and rating4 <= 3:
            print(book + " is recommended")