#coding:utf-8

import os
import ctypes

CUR_PATH= os.path.dirname('.')

if __name__ == '__main__':
    print('starting...')
    dll = ctypes.WinDLL(os.path.join(CUR_PATH,'hello.dll'))
    dll.hello()
