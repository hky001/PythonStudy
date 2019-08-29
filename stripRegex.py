import re
def stripRegex(text,s=None):
    if s == None:
        print(text)
        something1 = re.compile(r'^\s')
        mo = something1.sub('',text)
        print(mo)
        something2 = re.compile(r'\s$')
        mo = something2.sub('',mo)
        return mo
    else:
        # print(text)
        something = re.compile(s)

        return something.sub('',text)
text=' asdafs  a '
s= 'd'

print(stripRegex(text,s))