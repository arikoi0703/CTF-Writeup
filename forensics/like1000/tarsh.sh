#!/bin/zsh
for ((i = 1000; i > 0; i--)); 
do 
	tar -xvf $i.tar; 
	rm $i.tar
done
