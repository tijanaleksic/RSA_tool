
#public key contain n and e n=3233 e=17
#private key is n=3233 and d=413 

def modular_pow(b, e, n) :
    if (n == 1) :
        return 0
    c = 1
    for e_prime in range(e-1):
        c = (c * b) % n
    return c

#encryption 
#m is numbers that represent text that is sented 
#e is exponent and also public key of the person that recevies text
#n is moduo of m^e/// c(mod n) and 0 ≤ m < n
def encrypttext(m,e,n):
    ciphertext= modular_pow(m,e,n)
    return ciphertext

from sympy.ntheory import factorint
def getList(dict): 
      
    return [*dict]

#with this funtion you can get p and q if you know n=p*q.Returns a list of factors
def getPQfromN(n):
    a=factorint(n)
    print (a)
    list=getList(a);
    print(list)
    return list;
from math import gcd 
def lcm(x, y):
    
    return x * y // gcd(x, y)
 
#Compute the Carmichael's totient function of the product as λ(n) = lcm(p − 1, q − 1) giving 
def NCarmTotFun(n):
    list=getPQfromN(n);
    p=list[0];
    q=list[1];
    lambda_n=lcm(p-1,q-1);
    return lambda_n;
def PQCarmTotFun(p,q):
    lambda_n=lcm(p-1,q-1);
    return lambda_n;
def is_coprime(x, y):
    return gcd(x, y) == 1
def findCoprime(x):
    for i in range(2,x):
        if(is_coprime(i,x)):
            return i;
            break;
            
#modInverse returns a d that is modular multiplicative invers where a is number and m is moduo(in code charmtotfun is m)
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
def NEMencrypt(n,e,m):
    cipher=(pow(m,e)) % n
    return cipher;

def NDCdecrypt(n,d,c):
    message=(pow(c,d)) % n
    return message;
def NECdecrypt(n,e,c):
    arg2=NCarmTotFun(n);
    d=modInverse(e,arg2)
    message=NDCdecrypt(n,d,c);
    return message;



#poruka 65 se enkriptuje sa n=3233 i e=17 i dobija se 2790

print(NEMencrypt(3233,17,65))

#poruka se dekriptuje sa NDC c je tekst d je deo privanog keya n je isto sto i pre 

print(NDCdecrypt(3233,413,2790))

#poruka c se dekripuje sa e poznatim 
print(NECdecrypt(3233,17,2790))