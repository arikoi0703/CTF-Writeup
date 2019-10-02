#include <stdio.h>

int main(){
	int i;
	char code[]="gvzr vf ehaavat bhg jr arrq lbhe uryc\0";
	for(i=0; code[i]!='\0'; i++){
		if(code[i] >109)
			printf("%c", code[i]-13);
		else{
			printf("%c", code[i]+13);
		}
	}

	return 0;
}
