//ע��˴��ĺ궨����Ҫд��#include "simpledll.h"֮ǰ 

//�������dll��Ŀ�ڲ�ʹ��__declspec(dllexport)���� 

//��dll��Ŀ�ⲿʹ��ʱ����__declspec(dllimport)���� 

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