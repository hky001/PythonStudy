import pyperclip,re
#create phone Regex
phoneRegex = re.compile(r'''
(
    (\d{3}|\(\d{3}\))?          #区号
    (\s|-|\.)?                  #分隔符
    (\d{3})                     #前3位
    (\s|-|\.)?                  #分隔符
    (\d{4})                     #中间4位
    (\s|-|\.)?                  #分隔符
    (\d{4})                     #后面4位
)
''',re.VERBOSE)
#create email Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           #username
    @                           #@标志
    [a-zA-Z0-9.-]+              #域名
    (\.[a-zA-Z]{2,4})           #顶级域名
)
''',re.VERBOSE)
#find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+ groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')