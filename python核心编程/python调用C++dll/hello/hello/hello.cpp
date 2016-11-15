#include <stdio.h>     

#define DLLEXPORT extern "C" __declspec(dllexport)     

DLLEXPORT int __stdcall hello()
{
	printf("Hello world!\n");
	return 0;
}
