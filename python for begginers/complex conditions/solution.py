first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
if len(first_name)<10 and len(last_name)<10:
    print(f"{first_name}{last_name}")
elif len(first_name)>=10 and len( last_name)<10:
    print(f"{first_name[0]}.{last_name}")
elif len(first_name)<10 and len(last_name)>=10:
    print(f"{first_name}{last_name[0]}.")
else:
    print(f"{last_name}")