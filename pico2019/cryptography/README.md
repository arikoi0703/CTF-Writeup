# Cryptography

## The Numbers - Points: 50
The [numbers](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/The%20Numbers/the_numbers.png)... what do they mean?
- The flag is in the format PICOCTF{}
#### Solutions
> open the file, turn the number into ascii to get flag.
---
## 13 - Points: 100
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
- This can be solved online if you don't want to do it by hand!
#### Solutions
> use [online tool](https://cryptii.com/) to rot 13, or you prefer to do it by hand.
---
## Easy1 - Points: 100
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/Easy1/table.txt) to solve it?. 
- Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
- Please use all caps for the message.
#### Solutions
> it's [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), use [online tool](https://cryptii.com/) to solve it.
---
## caesar - Points: 100
Decrypt this [message](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/caesar/ciphertext). You can find the ciphertext in /problems/caesar_0_22aa542fadadcc37b6ec6037c493ec9f on the shell server.
-caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)
#### Solutions
> use [online tool](https://cryptii.com/) to solve it.
---
## Flags - Points: 200
What do the [flags](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/flags/flag.png) mean?
- The flag is in the format PICOCTF{}
#### Solutions
> These flags means [International maritime signal flags](https://en.wikipedia.org/wiki/International_maritime_signal_flags).  
> Count it according to wiki.
---
## Mr-Worldwide - Points: 200
A musician left us a [message](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/Mr-Worldwide/message.txt). What's it mean?
#### Solutions
> these are coordinates, put in googlemap, get their position's first alphabet, connect them.
---
## Tapping - Points: 200
Theres tapping coming in from the wires. What's it saying nc 2019shell1.picoctf.com 21897.
- What kind of encoding uses dashes and dots?
- The flag is in the format PICOCTF{}
#### Solutions
> ```
> .--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- ..--- -.... ..... ----. ...-- --... -.... -.... ...-- }
> ```
> This is [Morse code](https://en.wikipedia.org/wiki/Morse_code), use [online decoder](https://cryptii.com/) to solve it!
---
## la cifra de - Points: 200
I found this cipher in an old book. Can you figure out what it says? Connect with nc 2019shell1.picoctf.com 60147.
- There are tools that make this easy.
- Perhaps looking at history will help
#### Solutions
> the [message](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/la%20cifra%20de/cipher)  
> la cifra de as known as [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), use [online tool](https://cryptii.com/) to solve it.  
> Look at the hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xfmel1g3m}, I guess the picoCTF{flag} was hidden in this.  
> guess pohzCZK means picoCTF.  
> then according to [table](https://en.wikipedia.org/wiki/Tabula_recta) to figure out the key 
> Then use online tool to solve like vigenere
---
## rsa-pop-quiz - Points: 200
Class, take your seats! It's PRIME-time for a quiz... nc 2019shell1.picoctf.com 30962
- [RSA info](https://simple.wikipedia.org/wiki/RSA_algorithm)
#### Solutions
> see all [quiz](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/rsa-pop-quiz/rsa-pop-quiz)
> useful [online tool](https://www.cryptool.org/en/cto-highlights/rsa-step-by-step)
---
## miniRSA - Points: 300
Lets decrypt this: [ciphertext](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/miniRSA/ciphertext)? Something seems a bit small
- RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- How could having too small an e affect the security of this 2048 bit key?
- Make sure you dont lose precision, the numbers are pretty big (besides the e value)
#### Solutions
> we get a large N with small e=3, and we know that p^e % N = c  
> but if e too small, what will it happen?  
> if p^e is still less than N, that means p^e == c  
> so let's caculate cube root of c, we will get the plain text.  
> [cuberoot.py](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/cryptography/miniRSA/cuberoot.py) to caculate the cube root without bit losing.  
---
## b00tl3gRSA2 - Points: 400
In RSA d is alot bigger than e, why dont we use d to encrypt instead of e? Connect with nc 2019shell1.picoctf.com 52762.
- What is e generally?
#### Solutions
> ```
> c: 52151482884102864145132545607369299391044837995262346956509908350519349914208299212293910749349917918634127536456226859742604901739834425545950814163988599214946013715283287447531086816270774101845669992389539680535865241443519229701398516959917617798777925698981922380250407624008316025788827939758311109453  
> n: 68820147938161584949547806796280172452242173539948004499190747191744753483871391831310806801841672037549803863668178393572029530206960438192205034638328254542988312067427944699694568326428563982029987055977912640315797546486718871216047835025575653293059775659066599539015405321849205788887399447286571582933  
> e: 68656332946960382464659431407412514382715802496533873722654229551909054847322817176906661267851905938432392792018084006746309149250977011603286042536102331886305516969852870018395642294246775409161716556356365607409646004375475528170870040632424888406360058979286733667847233918947038440669888220551236126397  
> ```
> e is approach to n, so we can use [RSA wiener attack](https://github.com/pablocelayes/rsa-wiener-attack) to get d.  
> get d to decrypt c.








