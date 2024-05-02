import webbrowser
webbrowser.open("https://www.google.com")
course = "Intro"
print("Intro")
language = input("language please: ")
if language == "English":
    name = input("what is your name? ")
    print("Hello " + name)
    birth_year = input("what is your birth year: ")
    age = int(2024) - int(birth_year)
    print("age:" + str(age))
    state = input("where are you from? ")
    place = ("ok you are from " + state)
    print("place:" + str(place))
    weight = int(input("weight: "))
    unit = input("(K)g or (L)bs: ")
    if unit.upper() == "K":
        converted = weight / 0.45
        print("weight in lbs: " + str(converted))
    else:
        converted = weight * 0.45
        print("weight in kgs: " + str(converted))
    color = input("what is your favourite color? ")
    color = (name + " so you like " + color)
    print("color:" + str(color))
    long = int(input("height: "))
    ans = input("(F)feet or (M)metres: ")
    if ans.upper() == "F":
        converted = float(long) / 3.37
        print("height in metres: " + str(converted))
    else:
        converted = float(long) * 3.37
        print("height in feet: " + str(converted))
    food = input("what is your favourite food? ")
    food = ("what a coincidence, I also like " + food)
    print("food: " + str(food))
    print("thank you")
elif language == "Yoruba":
    name = input("ki ni oruko re? ")
    print("ba wo ni " + name)
    birth_year = input("odun wo lo bi e: ")
    age = int(2024) - int(birth_year)
    print("odun melo:" + str(age))
    state = input("ilu wo lo ti wa? ")
    place = ("owa lati " + state)
    print("ilu:" + str(place))
    weight = int(input("ba wo lo se tobi to: "))
    unit = input("(K)g or (L)bs: ")
    if unit.upper() == "K":
        converted = weight / 0.45
        print("itobi si ni lbs: " + str(converted))
    else:
        converted = weight * 0.45
        print("itobi si ni kgs : " + str(converted))
    color = input("ki ni color ti o feran si? ")
    color = (name + " o feran si " + color)
    print("color:" + str(color))
    long = int(input("ba wo lo se ga si: "))
    ans = input("(F)feet or (M)metres: ")
    if ans.upper() == "F":
        converted = float(long) / 3.37
        print("height in metres: " + str(converted))
    else:
        converted = float(long) * 3.37
        print("height in feet: " + str(converted))
    food = input("ki ni ounje ti o feran si? ")
    food = ("emi no nife si " + food)
    print("ounje: " + str(food))
    print("ese o")
