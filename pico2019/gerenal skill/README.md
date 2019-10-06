# General Skills

## The Factory's Secret - Points: 1
There appear to be some mysterious glyphs hidden inside this [abandoned factory](https://2019game.picoctf.com/game)... I wonder what would happen if you collected them all?
- Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.
#### Solutions
> play the pico game to find it.
---
## 2Warm - Points: 50
Can you convert the number 42 (base 10) to binary (base 2)? 
- Submit your answer in our competition's flag format. For example, if you answer was '11111', you would submit 'picoCTF{11111}' as the flag.
#### Solutions
> there are useful online tools to do this, or do it by hand.
---
## Lets Warm Up - Points: 50
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? 
- Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.
#### Solutions
> search ascii, or use online tool directly.
---
## Warmed Up - Points: 50
What is 0x3D (base 16) in decimal (base 10).
- Submit your answer in our competition's flag format. For example, if you answer was '22', you would submit 'picoCTF{22}' as the flag.
#### Solutions
> there are useful online tools to do this, or do it by hand.
---
## Bases - Points: 100
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.
- Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.
#### Solutions
> it's base64, [online tool](https://www.base64decode.org/) can decode it.
---
## First Grep - Points: 100
Can you find the flag in [file](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/gerenal%20skill/First%20Grep/file)? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_4_6b0be85ad029e98c683231bdafec396c on the shell server.
- grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)
#### Solutions
> ```shell
> $grep pico file
> ```
> or use text editor such as notepad, and find it.  
---
## Resources - Points: 100
We put together a bunch of resources to help you out on our website! If you go over there, you might even find a flag! https://picoctf.com/resources
#### Solutions
> just goto the website.
---
## strings it - Points: 100
Can you find the flag in [file](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/gerenal%20skill/strings%20it/strings) without running it? You can also find the file in /problems/strings-it_1_7a67382a38fc00751a6b9b29b0872813 on the shell server.
- [strings](https://linux.die.net/man/1/strings)
#### Solutions
> ```shell
> $strings strings [| grep pico]
> ```
---
## what's a net cat? - Points: 100
Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 32225 to get the flag?
- nc [tutorial](https://linux.die.net/man/1/nc)
#### Solutions
> ```shell
> $nc 2019shell1.picoctf.com 32225
> ```
---
## Based - Points: 200
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc 2019shell1.picoctf.com 20836.
- I hear python can convert things.
- It might help to have multiple windows open
#### Solutions
> turn binary, octal, hex to ascii, online tool is useful.  
> or you can write a program to deal with this problem.
---
## First Grep: Part II - Points: 200
Can you find the flag in /problems/first-grep--part-ii_3_b4bf3244c2886de1566a28c1b5a465ae/files on the shell server? Remember to use grep.
- grep (tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)
#### Solutions
> there are too many directories and files, but grep can handle it!  
> ```shell
> $grep pico ./ -r
> ```
---
## plumbing - Points: 200
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 57911.
- Remember the flag format is picoCTF{XXXX}
- What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)
#### Solutions
> ```shell
> $nc 2019shell1.picoctf.com 57911 | grep pico
> ```
> or 
> ```shell
> $nc 2019shell1.picoctf.com 57911 > file
> $grep pico file
> ```
---
## whats-the-difference - Points: 200
Can you spot the difference? [kitters](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/gerenal%20skill/whats-the-difference/kitters.jpg) [cattos](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/gerenal%20skill/whats-the-difference/cattos.jpg). They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server
- How do you find the difference between two files?
- Dumping the data from a hex editor may make it easier to compare.
#### Solutions
> ```shell
> $xxd cattos.jpg > cattos
> ```
> this make jpg more easier visible in text.  
> ```shell
> $diff cattos kitters
> ```
> this show the difference between two files.
---
## where-is-the-file
I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_4_f26b413d005c16c61f127740ab242b35.
- What command can see/read files?
- What's in the manual page of ls?
#### Solutions
> find the hidden files.  
> ```shell
> $ls -a
> $cat .cant_see_me
> ```
---
## flag_shop - Points: 300
There's a flag shop selling stuff, can you buy a flag? [Source](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/gerenal%20skill/flag_shop/store.c). Connect with nc 2019shell1.picoctf.com 25858.
- Two's compliment can do some weird things when numbers get really big!
#### Solutions
> ```c
> int number_flags = 0;
> fflush(stdin);
> scanf("%d", &number_flags);
> if(number_flags > 0){
>   int total_cost = 0;
>   total_cost = 900*number_flags;
>   printf("\nThe final cost is: %d\n", total_cost);
>   if(total_cost <= account_balance){
>   account_balance = account_balance - total_cost;
>   printf("\nYour current balance after transaction: %d\n\n", account_balance);
> }
> else{
>   printf("Not enough funds to complete purchase\n");
> }             
> ```
> what will happen when 900*number_flags is out of integer range?  
> give a large number_flags to try it.  
> integer overflow, and your account balance may increase, repeat until it's enough to buy the true flag.    
---
## mus1c - Points: 300
I wrote you a [song](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/gerenal%20skill/mus1c/lyrics.txt). Put it in the picoCTF{} flag format
- Do you think you can master rockstar?
#### Solutions
> do not master rockstar, but understand it.  
> try to become [rockstar](https://codewithrockstar.com/online)!  
> turn the number into ascii after rock.  
---
## 1_wanna_b3_a_r0ck5tar - Points: 350
I wrote you another [song](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/gerenal%20skill/1_wanna_b3_a_r0ck5tar/lyrics.txt). Put the flag in the picoCTF{} flag format
#### Solutions
> [rock](https://codewithrockstar.com/online) it as above.  
> will find some if-else conditions and need input.  
> I can't master it, so I remove the if statement and input( Listen to ) function.  
> then, I can rock it without input and if-else statements.  
> turn the number into ascii after rock.  
