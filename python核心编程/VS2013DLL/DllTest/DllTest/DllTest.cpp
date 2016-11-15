#define DLL_API __declspec(dllexport)  

#include "DllTest.h"  

int add(int a, int b)
{
	return a + b;
}