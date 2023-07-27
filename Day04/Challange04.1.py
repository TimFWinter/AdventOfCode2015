from hashlib import md5

input = "bgvyzdsv"

hash = "99999"

iterator = 0
while hash[:5] != "00000":

    hash = str(md5((input + str(iterator)).encode("ASCII")).hexdigest())

    iterator += 1

print(iterator - 1)