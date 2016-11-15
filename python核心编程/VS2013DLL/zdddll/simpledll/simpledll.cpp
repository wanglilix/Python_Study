//注意此处的宏定义需要写在#include "simpledll.h"之前 

//以完成在dll项目内部使用__declspec(dllexport)导出 

//在dll项目外部使用时，用__declspec(dllimport)导入 

#define DLL_IMPLEMENT 
#include "simpledll.h" 
namespace zdd
{

	SimpleDll::SimpleDll()
	{
	}

	SimpleDll::~SimpleDll()
	{
	}
	int SimpleDll::add(int x, int y)
	{
		return x + y;
	}

}