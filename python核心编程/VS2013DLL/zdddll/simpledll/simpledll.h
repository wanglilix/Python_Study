#pragma once; 

//�ú������dll��Ŀ�ڲ�ʹ��__declspec(dllexport)���� 

//��dll��Ŀ�ⲿʹ��ʱ����__declspec(dllimport)���� 

//��DLL_IMPLEMENT��simpledll.cpp�ж��� 

#ifdef DLL_IMPLEMENT 

#define DLL_API __declspec(dllexport) 

#else 

#define DLL_API __declspec(dllimport) 

#endif 

namespace zdd
{

	//������ 

	class DLL_API SimpleDll

	{
	public:

		SimpleDll();

		~SimpleDll();

		int add(int x, int y); //�򵥷��� 

	};
}