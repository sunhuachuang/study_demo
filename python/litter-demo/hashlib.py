import hashlib

md5 = hashlib.md5("aaa")
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


# sha1 = hashlib.sha1()
# sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# import hashlib

# md5 = hashlib.md5()
# md5.update('how to use md5 in python?'.encode('utf-8'))
# print(md5.hexdigest())