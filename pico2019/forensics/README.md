# Forensics

## Glory of the Garden - Points: 50
This [garden](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/Glory%20of%20the%20Garden/Glory-of-the-Garden.jpg) contains more than it seems. You can also find the file in /problems/glory-of-the-garden_5_eeb712a9a3bc1998ffcd626af9d63f98 on the shell server.  
- What is a hex editor?  
### Solution
> ```shell 
> $strings filename [| grep pico]
> ```  
---
## unzip - Points: 50
Can you unzip this [file](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/unzip/flag.zip) and get the flag?  
- put the flag in the format picoCTF{XXXXX}  
### Solutions
> ```shell 
> $unzip filename 
> ```  
---
## So Meta - Points: 150
Find the [flag](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/So%20Meta/pico_img.png) in this picture. You can also find the file in /problems/so-meta_4_4e8d17dbd28e1fdfe82ba31ceb021615.
- What does meta mean in the context of files?  
- Ever hear of metadata?
### Solutions
> ```shell 
> $strings filename [| grep pico]
> ```  
---
## What Lies Within - Points: 150
Theres something in the [building](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/What%20Lies%20Within/What-Lies-Within_buildings.png). Can you retrieve the flag?
- There is data encoded somewhere, there might be an online decoder
### Solutions
> it's [steganography](https://en.wikipedia.org/wiki/Steganography).  
> use [online tool](https://stylesuxx.github.io/steganography/) to decode it.  
---
## extensions - Points: 150
This is a really weird text file [TXT](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/extensions/extensions_flag.txt)? Can you find the flag?
- How do operating systems know what kind of file it is? (It's not just the ending!  
- Make sure to submit the flag as picoCTF{XXXXX}  
#### Solutions
> ```shell
> $file filename
> ```
> check the file type, rename it to correct extension.
> it's PNG, open it to get flag.
---
## shark on wire 1 - Points: 150
We found this [packet capture](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/shark%20on%20wire%201/capture.pcap). Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.
- Try using a tool like Wireshark  
- What are streams?
### Solutions
> open it by wireshark like below.
> ![Alt text](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/shark%20on%20wire%201/wireshark_screen_shot.PNG)
> right click any package, try to Follow > Stream.  
> in this case, it's in UDP stream. Right click the package(No.63), and follow the UDP stream to get the flag.
---
## WhitePages - Points: 250
I stopped using YellowPages and moved onto WhitePages... but [the page they gave] me is all blank!
#### Solutions
>
---
## c0rrupt - Points: 250
We found this [file](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/c0rrupt/mystery). Recover the flag. You can also find the file in /problems/c0rrupt_0_1fcad1344c25a122a00721e4af86de13.
- Try fixing the file header
#### Solutions
>
---
## like1000 - Points: 250
This [.tar file](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/like1000/1000.tar) got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.
- Try and script this, it'll save you alot of time
### Solutions
> I write a [script](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/like1000/tarsh.sh) for zsh.  
> or use command line directly:  
> ```shell
> $for i in {1000..1}
> do
>     tar -xvf $i.tar
> done
> ```
> get the flag after tar finish.
---
## m00nwalk - Points: 250
Decode this [message](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/m00nwalk/message.wav) from the moon. You can also find the file in /problems/m00nwalk_2_ddfd37932ded29f58963e8d9c526c2fa.
- How did pictures from the moon landing get sent back to Earth?
- What is the CMU mascot?, that might help select a RX option
#### Solutions
>
---
## c0rrupt - Points: 250
We found this [packet capture](https://github.com/arikoi0703/CTF_writeup/blob/master/pico2019/forensics/shark%20on%20wire%202/capture.pcap). Recover the flag that was pilfered from the network. You can also find the file in /problems/shark-on-wire-2_0_3e92bfbdb2f6d0e25b8d019453fdbf07.
#### Solutions
>




