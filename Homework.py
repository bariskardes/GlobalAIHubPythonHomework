value1 = input("value1: ")
value2 = input("value2: ")
value3 = input("value3: ")
value4 = input("value4: ")
value5 = input("value5: ")

print(F"f-string usage")
print(F"value1 is a {type(value1)} and it's value {value1}.")
print(F"value2 is a {type(value2)} and it's value {value2}.")
print(F"value3 is a {type(value3)} and it's value {value3}.")
print(F"value4 is a {type(value4)} and it's value {value4}.")
print(F"value5 is a {type(value5)} and it's value {value5}.")

print("format usage")
print("value1 is a {0} and it's value {1}.".format(type(value1),value1))
print("value2 is a {0} and it's value {1}.".format(type(value2),value2))
print("value3 is a {0} and it's value {1}.".format(type(value3),value3))
print("value4 is a {0} and it's value {1}.".format(type(value4),value4))
print("value5 is a {0} and it's value {1}.".format(type(value5),value5))