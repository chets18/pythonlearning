# match-case statement (switch-case): AN alternative to using many 'elif' statements
# Execute some code if a value matches a 'case' 
# Benefits: cleaner and suntax is more readable

def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is wednesday"
    elif day == 5:
        return "It is Thrusday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday" 
    else: 
        return "Not a valid day"

print(day_of_week(2)) 

# instead this we use:
def days_of_week(day):
 match day:
    case 1:
        return "It is Sunday"
    case 2:
        return "It is Monday"
    case 3:
        return "It is Tuesday"
    case 4:
        return "It is wednesday"
    case 5:
        return "It is Thrusday"
    case 6:
        return "It is Friday"
    case 7:  
        return "It is Saturday"
    case _:
        return "Not a valid day"

print(days_of_week(6))  

#to match case we can use string such as:
# match day:
# case "sunday":
#  return True

# using | will return "or" such as: case "Saturday" | "Sunday":