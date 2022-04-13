# 加密算法 MD5 sha1 sha256
import hashlib

msg = '中午一块吃饭呀'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())
