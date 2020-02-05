#include <stdio.h>

void write(void)
{
	char buffer[8];
	gets(buffer);
}
int main()
{
	write();
	return 0;
}
