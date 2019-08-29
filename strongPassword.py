import re
def strongPw(text):
    if len(text) <= 8:
        print('密码小于8位')
        return False
    capital = re.compile(r'[A-Z]+')
    if capital.search(text) == None:
        print('密码缺少大写字母')
        return False
    lowercase = re.compile(r'[a-z]+')
    if lowercase.search(text) == None:
        print('密码缺少小写字母')
        return False
    number = re.compile(r'\d+')
    if number.search(text) == None:
        print('密码缺少数字')
        return False
    print('密码格式正确')
    return True
text = 'AsAAsd123214'
strongPw(text)