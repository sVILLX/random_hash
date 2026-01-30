import hashlib

for i in range(1000):
    obj = hashlib.md5()
    obj.update(f"string-{i}".encode("utf-8"))
    string = obj.hexdigest()
    if (string[0] == '0' and string[1] == '0'):
        print(f"Hash founded: {string}")
        break
    if (i == 999):
        print("Hash not founded")