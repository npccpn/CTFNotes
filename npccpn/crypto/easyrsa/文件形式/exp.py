#!/usr/bin/env python3
import gmpy2
import libnum
from factordb.factordb import FactorDB
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import bytes_to_long,long_to_bytes
f=open('public.key','r')
#读入公钥,取得其中的N和e
key = RSA.import_key(f.read())
n=key.n
e=key.e
#尝试分解N
f = FactorDB(n)   
f.connect()
p,q=f.get_factor_list()
#分解得到p和q

#下面一行,需要int强制转换一下,
#因为下面的RSA.construct接收int不接收mpz类型
d=int(gmpy2.invert(e,(p-1)*(q-1)))
print(d)

privatekey = RSA.construct((n,e,d,p,q))
rsa = PKCS1_OAEP.new(privatekey)
m = rsa.decrypt(open('flag.enc','rb').read())
print(m)