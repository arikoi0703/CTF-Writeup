# Flag_shop

### Question
> There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc 2019shell1.picoctf.com 25858.

### Hints
> Two's compliment can do some weird things when numbers get really big!

### Solution
> observe the store.c or run it by nc 2019shell1.picoctf.com 25858
> To buy the 1337 flag, we need 100000 dollars, but we only have 1100 dollars. So we must find some  way to earn money in the store.
> Look at other function, notice that we can buy 'Defintely not the flag Flag', in which the account_balance will be changed by total_cost.  Then, if we can make the total_cost < 0, in other hand, we earn money.
> To make total_cost < 0, we have to overflow it by 900 * number_flags, so when we give a large number like 999999999 to number_flags, 900 * number_flags will be overflow.
> Then we can buy the 1337 flag.
 
