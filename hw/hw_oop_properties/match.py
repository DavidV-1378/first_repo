day = 5
month = 3
match day:
    case 1 | 5 if month == 2:
        print("monday")
    case 2:
        print("tuesady")
    case 3:
        print("wednesady")
    case 4:
        print("thursday")
    case _:
        print("other day")
