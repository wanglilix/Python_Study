#ifdef DLL_API  
#else  
#define DLL_API __declspec(dllexport)  
#endif  
// ����Ҫ�����ĺ���  
DLL_API int add(int a, int b);