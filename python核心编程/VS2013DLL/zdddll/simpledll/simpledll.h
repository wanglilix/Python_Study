#pragma once; 

//该宏完成在dll项目内部使用__declspec(dllexport)导出 

//在dll项目外部使用时，用__declspec(dllimport)导入 

//宏DLL_IMPLEMENT在simpledll.cpp中定义 

#ifdef DLL_IMPLEMENT 

#define DLL_API __declspec(dllexport) 

#else 

#define DLL_API __declspec(dllimport) 

#endif 

namespace zdd
{

	//导出类 

	class DLL_API SimpleDll

	{
	public:

		SimpleDll();

		~SimpleDll();

		int add(int x, int y); //简单方法 

	};
}