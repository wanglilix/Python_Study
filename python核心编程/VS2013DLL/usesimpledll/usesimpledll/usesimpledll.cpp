#include "stdio.h" 
#include "stdlib.h"
#include <iostream>
#include "stdafx.h"
#include "simpledll.h" 
using namespace zdd;
using namespace std;

int main(char argc, char**argv)
{
	SimpleDll sd;

	auto tmp = sd.add(3, 5);
	SimpleDll *psd = new SimpleDll;
	tmp = psd->add(5, 5);

	return 0;
}