// TestForDll.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "DllTest.h"

int _tmain(int argc, _TCHAR* argv[])
{
	int a = 3;
	int b = 4;
	printf("%d", add(a, b));
	return 0;
}

