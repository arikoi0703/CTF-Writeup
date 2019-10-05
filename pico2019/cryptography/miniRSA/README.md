# miniRSA  

### Question
> Lets decrypt this: ciphertext? Something seems a bit small

### Hints
> RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
> How could having too small an e affect the security of this 2048 bit key?
> Make sure you dont lose precision, the numbers are pretty big (besides the e value)

### Solution
> we get a large N with small e=3, and we know that p^e % N = c  
> but if e too small, what will it happen?  
> if p^e is still less than N, that means p^e == c  
> so let's caculate cube root of c, we will get the plain text.  
> turn it into ascii.  

> cuberoot.py to caculate the cube root without bit losing.  

