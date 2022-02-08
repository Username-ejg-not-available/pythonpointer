import random
import os

class _MemAddr:
    def __init__(self,addr):
        self.addr = addr

_heap = {}
NULLPTR = _MemAddr(0x0)

_makeaddr = lambda x: _MemAddr(hex(int(random.random() * 4096)+1))

def new(obj):
    global _heap
    addr = _makeaddr(0)
    while addr in _heap or addr == NULLPTR:
        addr = _makeaddr(0)
    _heap[addr] = obj
    return addr

def deref(pointer):
    global _heap
    if pointer not in _heap or pointer == NULLPTR: raise Exception("Segfault!")
    else: return _heap[pointer]

def delete(pointer):
    if pointer not in _heap or pointer == NULLPTR: raise Exception("Segfault!")
    del _heap[pointer]

def _pHelp(obj,file,addr:str,states,printNull:bool) -> str:
    dic = obj.__dict__
    cname = str(obj.__class__)
    cname = cname[cname.find('.')+1:-2]+str(int(addr,16))
    if cname in states: return cname
    states.add(cname)
    file.write("\t"+cname+" [shape=box]\n")
    for x in dic:
        if dic[x] == NULLPTR: 
            if printNull: file.write("\t"+cname+" -> NULLPTR [label="+x+"]\n")
        elif isinstance(dic[x],_MemAddr): 
            if dic[x] in _heap: 
                pointsto = _pHelp(deref(dic[x]),file,dic[x].addr,states,printNull)
                file.write("\t"+cname+" -> "+pointsto+" [label="+x+"]")
            else: raise Exception("Segfault!")
        else: 
            file.write("\t"+x+addr+" [label=\""+x+": "+str(dic[x])+"\"]\n")
            file.write("\t"+cname+" -> "+x+addr+" []\n")
    return cname

def printObj(pointer: _MemAddr,printNull=True) -> None:
    states = set([])
    if pointer not in _heap: raise Exception("Segfault!")
    if not os.path.isdir("./objs"): os.system("mkdir objs")
    cname = str(_heap[pointer].__class__)
    cname = cname[cname.find('.')+1:-2]+str(int(pointer.addr,16))
    with open("./objs/"+cname+".dot","w") as file:
        file.write("digraph "+cname+" {\n")
        if printNull: file.write("\tNULLPTR [shape=none]\n")
        _pHelp(_heap[pointer],file,pointer.addr,states,printNull)
        file.write("}")
    os.system("dot -Tpng ./objs/"+cname+".dot -o ./objs/"+cname+".png")
