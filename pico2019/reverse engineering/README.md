# Reverse Engineering

## vault-door-training - Points: 50
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoorTraining.java)
- The password is revealed in the program's source code.
#### Solutions
> open the source code, and find flag.  
---
## vault-door-1 - Points: 100
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoor1.java)
- Look up the charAt() method online.
#### Solutions
> reverse the password according to source code.  
> the char and order is given in the source code.
---
## asm1 - Points: 200
What does asm1(0x1f3) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/asm1/test.S) located in the directory at /problems/asm1_2_4ced82d316c06cd3a46ba3bda9f6c144.
- assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
#### Solutions
>
---
## vault-door-3 - Points: 200
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoor3.java)
- Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.
#### Solutions
> password was be substitute, reverse it!  
---
## asm2 - Points: 250
What does asm2(0x6,0x24) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/asm2/test.S) located in the directory at /problems/asm2_6_88bbaaae0b7723b33c39fce07d342e36.
- assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
#### Solutions
>
---
## vault-door-4 - Points: 250
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoor4.java)
- Use a search engine to find an "ASCII table".
- You will also need to know the difference between octal, decimal, and hexademical numbers.
#### Solutions
> [online tool](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html) is helpful.  
> or write a program to convert them.  
---
## asm3 - Points: 300
What does asm3(0xc4bd37e3,0xf516e15e,0xeea4f333) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/asm3/test.S) located in the directory at /problems/asm3_4_c89016e12b8f3cac92a2e637c03f6139.
- more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)
#### Solutions
>
---
## reverse_cipher - Points: 300
We have recovered a [binary](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/reverse_cipher/rev) and a [text](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/reverse_cipher/rev_this) file. Can you reverse the flag. Its also found in /problems/reverse-cipher_2_d8dc36eefa9dfce00eac3dab8f42513c on the shell server.
- objdump and Gihdra are some tools that could assist with this
#### Solutions
>
---
## vault-door-5 - Points: 300
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoor5.java)
- You may find an encoder/decoder tool helpful, such as https://encoding.tools/
- Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.
#### Solutions
> it was base64 encode.  
> online tool make it easy.
---
## vault-door-6 - Points: 350
This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoor6.java)
- If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.
#### Solutions
> ```java
> byte[] myBytes = {
>   0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
>   0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
>   0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
>   0xa , 0x34, 0x30, 0x31, 0x30, 0x36, 0x30, 0x31,
> };
> for (int i=0; i<32; i++) {
>   if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
>     return false;
>   }
> }
> ```
> myBytes[i] ^ 0x55 can get the origin pass.  
---
## vault-door-7 - Points: 400
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: [VaultDoor7.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoor7.java)
- Use a decimal/hexademical converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
- You will also need to consult an ASCII table such as this one: https://www.asciitable.com/
#### Solutions
> ```java
> public boolean checkPassword(String password) {
>   if (password.length() != 32) {
>     return false;
>   }
>   int[] x = passwordToIntArray(password);
>   return x[0] == 1096770097
>       && x[1] == 1952395366
>       && x[2] == 1600270708
>       && x[3] == 1601398833
>       && x[4] == 1716808014
>       && x[5] == 1734304823
>       && x[6] == 962880562
>       && x[7] == 895706419;
> }
> ```
> turn decimal into hex, then turn hex into ascii can get the flag.
---
## vault-door-8 - Points: 450
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/reverse%20engineering/VaultDoor8.java)
- Clean up the source code so that you can read it and understand what is going on.
- Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.
#### Solutions
> it's hard to read? Try [this](https://codebeautify.org/)!  
> since I did not install java, I use [online tool](https://repl.it/languages/) to run it.  
> find the encrypt function, it just switch bits!  
> so decrypt is reverse the encrypt, do the step from last to first can reverse it.  



