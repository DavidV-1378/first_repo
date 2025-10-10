x = 4.7 # float
y = int(x) # intiger
print(type(x), type(y))

#print( 35 / 0 ), error

mystring = "david's internet "
mystring = 'david\'s internet '
is_bad = "is bad"
my_string_2 = mystring + is_bad
print(my_string_2)
print(mystring[0])
print(len(my_string_2))
username = "david"
timestamp = "3:20"
url = "www.google.com"

print(f"{username} has accesed the site {url} at {timestamp}")
message = "{} has accesed the site {} at {}"
print(message.format(username, timestamp, url))
my_string_3 = my_string_2.split(" ", 2)
print(type(my_string_3))
print(my_string_2.islower())
