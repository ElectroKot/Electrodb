# -*- coding: utf-8 -*-

from ast import Pass
from importlib.resources import path
import os
from io import UnsupportedOperation
from genericpath import exists



print('[Electro-db] db is on ready')
pathdb = 'D://Database//'
if not os.path.exists(pathdb):
    print('[ELECTRO ERROR] Error: main directory is: '+str(pathdb)+' there is no main directory try to chnge main directory')

def ChangePath(dbpath):
    if os.path.exists(str(dbpath)):
        global pathdb
        pathdb = str(dbpath)
        print('[Electro db] - main path is changeed on - '+str(pathdb)+'".')
        return 1
    else:
        print(f'[ELECTRO ERROR] Error: path In "ChangePath({str(dbpath)})": Path not exists.')
        return -1


def Ctable(name):
    if not os.path.exists(str(pathdb)+str(name)):
        os.mkdir(str(pathdb)+str(name))
        return 1
    else:
        print('[ELECTRO SYNTAX] : table alerdy exsist but dont created')
        return 0

def CValue(table, name):
    if os.path.exists(str(pathdb)+(table)):
        global tablepath
        tablepath = str(pathdb)+str(table)+'//'
        f = open(str(tablepath)+str(name)+'.edb', 'w+')
        f.close()
        return 1
    else:
        print('[ELECTRO ERROR] Error: There is no table named - "'+str(table)+'".')
        return 0
def ReplaceValue(table, valuename, value):
    global path
    globalpath = str(pathdb)+str(table)+'//'+(valuename)+'.edb'
    if os.path.exists(str(globalpath)):
        os.remove(globalpath)
        f = open(globalpath, 'w+')
        f.write(value)
        f.close()
        return 1
    else:
        print('[ELECTRO ERROR] Error: no such a value or table named - "'+ str(globalpath)+'".')
        return 0

def AddValue(table, valuename, value):
    if os.path.exists(str(pathdb)+str(table)+'\\'+(valuename)+'.edb'):
        f = open(str(pathdb)+str(table)+'\\'+(valuename)+'.edb')
        v = f.read()
        f.close()
        if v == '':
            print('[ELECTRO ERROR] Error: No such a file or file is empety')
            return 0
    if os.path.exists(str(pathdb)+str(table)+'\\'+(valuename)+'.edb'):
        oldValue = open(str(pathdb)+str(table)+'//'+str(valuename)+'.edb', 'r', encoding='utf-8')
        oldvalue = oldValue.read()
        oldValue.close()
        os.remove(str(pathdb)+str(table)+'//'+str(valuename)+'.edb')
        newValue = open(str(pathdb)+str(table)+'\\'+str(valuename)+'.edb', 'w+', encoding='utf-8')
        newvalue = str(int(oldvalue) + int(value))
        newValue.write(newvalue)
        newValue.close()
    else:
        print('[ELECTRO ERROR] Error: no such a table or value named - "' + str(pathdb)+str(table)+'\\'+str(valuename))
        return


def minValue(table, valuename, value):
    if os.path.exists(str(pathdb)+str(table)+'\\'+(valuename)+'.edb'):
        f = open(str(pathdb)+str(table)+'\\'+(valuename)+'.edb')
        v = f.read()
        f.close()
        if v == '':
            print('[ELECTRO ERROR] Error: No such a file or file is empety')
            return 0
    if os.path.exists(str(pathdb)+str(table)+'\\'+(valuename)+'.edb'):
        oldAddValue = open(str(pathdb)+str(table)+'//'+str(valuename)+'.edb', 'r', encoding='utf-8')
        oldaddvalue = oldAddValue.read()
        oldAddValue.close()
        os.remove(str(pathdb)+str(table)+'//'+str(valuename)+'.edb')
        newAddValue = open(str(table)+'\\'+str(valuename)+'.edb', 'w+', encoding='utf-8')
        newaddvalue = str(int(oldaddvalue) - int(value))
        newAddValue.write(newaddvalue)
        newAddValue.close()

def getValue(table, valuename):
    if os.path.exists(str(pathdb)+str(table)+'\\'+str(valuename)+'.edb'):
        f = open(str(pathdb)+str(table)+'\\'+str(valuename)+'.edb')
        value = f.read()
        return value
    else:
        print('[ELECTRO ERROR] Error: no table or value named"'+(str(pathdb)+str(table)+'\\'+str(valuename)+'.edb')+'".')
        return