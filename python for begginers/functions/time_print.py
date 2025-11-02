import datetime
# Create a function called print_time
# This function will print the message and current time
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print() 

for x in range(0,10):
    print(x)
# Call print_time() function to display message and current time
print_time()



from datetime import datetime

# What if we want different messages displayed?
# Can we still use a function?
first_name = 'Susan'
print('first name assigned')
print(datetime.now())
print() 

for x in range(0,10):
	print(x)
print('loop completed')
print(datetime.now())
print()