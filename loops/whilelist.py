# using while loop in a list

unconfirmedusers = ["joao", "maria", "jose"]
confirmedusers = []

while unconfirmedusers:
    currentuser = unconfirmedusers.pop()
    print(f"user to verify: {currentuser}")
    confirmedusers.append(currentuser)

print("\n")

while confirmedusers:
    print(f"confirmed: {confirmedusers.pop()}")


print(unconfirmedusers)
print("\n")
print(confirmedusers)
