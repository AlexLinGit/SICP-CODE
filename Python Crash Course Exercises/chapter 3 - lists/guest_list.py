guest_list = ['Thomas Jefferson', 'Bill Gates', 'Me', 'Bob']
print("I am inviting you, " + guest_list[1] + " to dinner")
print("I am not inviting " + guest_list[0] + " to dinner")
print("I am tired of typing more strings, " + guest_list[2] + ".")
print(guest_list[3] + ", this is the last string.")
#First part
#original guest list invitaitons

print("\tSorry for all the fuss, but " + guest_list[3] + " can not make it tonight")

canceled_man = guest_list.pop(3)

guest_list.insert(3, 'Firestorm')
print(canceled_man + " could not make it tonight, so " +
guest_list[3] + " will replace him in the dinner.  Enjoy")
#second part
#replacement of Firestorm for Bob

guest_list.insert(0, 'Trump')
guest_list.insert(2, 'Gomez')
guest_list.append('Flynn')

print(guest_list[0] + ", " + guest_list[2] + ", and " + guest_list[4] + " will be too joining us for dinner tonight.")
#Adding 3 people to list

print("\tSorry gals, but only two people can come today")
num_one = guest_list.pop(0)
print("You are booted " + num_one)
num_two = guest_list.pop(0)
print("You are booted " + num_two)
num_three = guest_list.pop(0)
print("You are booted " + num_three)
num_four = guest_list.pop(0)
print("You are booted " + num_four)
num_five = guest_list.pop(0)
print("You are booted " + num_five)
#booting person 1-5

print(guest_list[0] + " and " + guest_list[1] + " you guys are invited still.  Hi Jen :)")
#inviting last two people

del guest_list[0]
del guest_list[0]
print(guest_list)
#clearing the guest list

print("\nI'm inviting " + str(len(guest_list)) + " people to dinner.")
