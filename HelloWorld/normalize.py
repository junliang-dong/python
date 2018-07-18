# _*_ coding: utf-8 _*_
def normalize(name):
    return "%s" %(name[:1].upper() + name[1:].lower())

def formatName(L):
    return map(normalize, L)

names = ["adSjKggL", "IInNNklll", "DSDadgsdg", "SADFgadfasdf"]
ret = formatName(names)
print(list(ret))
