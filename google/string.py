def first_and_last(message):
    if message=="" or message[0] == message[-1]:
       return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


elements=["a", "b", "c", "d", "e", "f", "g"]
for index,element in enumerate(elements):
    print(index, element)
