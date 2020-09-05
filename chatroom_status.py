def chatroom_status(users):
    if len(users) == 0:
        return "no one online"
    elif len(users) == 1:
        return str(users[0])+" online"
    elif len(users) == 2:
        return str(users[0]) + " and " + str(users[1]) + " online"
    else:
        return str(users[0]) + " , " + str(users[1]) + " and " + str(len(users)-2) + " online"


print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))
