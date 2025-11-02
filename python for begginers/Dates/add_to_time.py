print("Enter first time:")
h1 = int(input("Hours: "))
m1 = int(input("Minutes: "))
s1 = int(input("Seconds: "))

print("\nEnter second time:")
h2 = int(input("Hours: "))
m2 = int(input("Minutes: "))
s2 = int(input("Seconds: "))

s = s1 + s2
m = m1 + m2
h = h1 + h2

# seconds to minutes
if s >= 60:
    s -= 60
    m += 1

# minutes to hours
if m >= 60:
    m -= 60
    h += 1

print(f"\nAdded Time = {h} hours {m} minutes {s} seconds")

# ---------- SUBTRACTION ----------
# convert both times to total seconds
total1 = h1*3600 + m1*60 + s1
total2 = h2*3600 + m2*60 + s2
diff = abs(total1 - total2)

h = diff // 3600
m = (diff % 3600) // 60#  --- jitne bhi hours aaynge usme 3600 ka multiply hone k baad total seconds me se minus krnge   phir jo bhi bchega usme se 60 ka divide krdo  flour function k accc check kro kitne minutes  usme 60 ka multipy kro thn  total seconds me se minus kro thn jo bcha  vo hi seconds hai...
s = diff % 60