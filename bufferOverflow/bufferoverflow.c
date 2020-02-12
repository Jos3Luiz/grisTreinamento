#include <stdio.h>
#include <unistd.h>
#include <string.h>
void getShell(){
	execv("/bin/sh",NULL);

}

int main(int argc, char** argv)
{	
	char buffer[128];
	if (argc <2){
		printf("uso: ./<programa> <nome>\n");
		return 1;
	}
	strcpy(buffer,argv[1]);
	printf("bom dia %s\n",buffer);
	return 0;
}
