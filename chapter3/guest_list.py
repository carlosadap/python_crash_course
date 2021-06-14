guest_list = ["guest1", "guest2", "guest3"]

print(f"Hey {guest_list[0]}! Come to my party")
print(f"Hey {guest_list[1]}! Come to my party")
print(f"Hey {guest_list[2]}! Come to my party")

print(f"Oh no! {guest_list[2]} can't come!")

guest_list[2] = "new_guest"

print(f"Hey {guest_list[0]}! Come to my party")
print(f"Hey {guest_list[1]}! Come to my party")
print(f"Hey {guest_list[2]}! Come to my party")

print(f"Hey friends! I found a bigger table")

guest_list.insert(0, "guest4")
guest_list.insert(2, "guest5")
guest_list.append("guest6")

print(f"Hey {guest_list[0]}! Come to my party")
print(f"Hey {guest_list[1]}! Come to my party")
print(f"Hey {guest_list[2]}! Come to my party")
print(f"Hey {guest_list[3]}! Come to my party")
print(f"Hey {guest_list[4]}! Come to my party")
print(f"Hey {guest_list[5]}! Come to my party")

print(f"Sorry friends! I can only invite two people")

print(f"Sorry {guest_list.pop()}, not enough places")
print(f"Sorry {guest_list.pop()}, not enough places")
print(f"Sorry {guest_list.pop()}, not enough places")
print(f"Sorry {guest_list.pop()}, not enough places")

print(f"Hey {guest_list[0]}! Come to my party")
print(f"Hey {guest_list[1]}! Come to my party")

del guest_list[0]
del guest_list[0]

print(guest_list)
