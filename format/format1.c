#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int target=0;

void vuln()
{
  char buffer[512];

  fgets(buffer,sizeof(buffer),stdin);
  printf(buffer);

  if (target==64){
  	printf("you won!\n");
  }
  else{
  	printf("target is  %d: \n",target);
  }


}

int main(){

  vuln();
  return 0;
}
