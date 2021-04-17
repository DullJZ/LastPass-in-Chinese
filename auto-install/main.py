import os
import wget
print(r'''================
作者：DullJZ
博客：http://dulljzblog.jz-home.top
LastPass汉化文章：https://dulljzblog.jz-home.top/2021/02/18/汉化日记--汉化LastPass/
================
''')
ID = ['bbcinlkgjjkejfdpemiealijmmooekmp', 'hdokiejnpimakedhajhdlcegeplioahd']
browser = [
    'Microsoft\\Edge', 'Microsoft\\Edge Beta', 'Microsoft\\Edge Dev',
    'Microsoft\\Edge Canary', 'Google\\Chrome'
]
print('''================
您使用的浏览器是：
1. Microsoft Edge Chromium UWP
2. Microsoft Edge Chromium Beta
3. Microsoft Edge Chromium Dev
4. Microsoft Edge Chromium Canary
5. Google Chrome
================
''')
option1 = int(input('输入序号：'))

print('''================
您的LastPass扩展是在哪里下载的：
1. Microsoft Edge网上应用商店
2. Chrome网上应用店
================
''')
option2 = int(input('输入序号：'))

path = os.getenv('LOCALAPPDATA') + '\\' + browser[
    option1 - 1] + '\\User Data\\Default\\Extensions\\' + ID[option2 - 1]
different_versions = os.listdir(path)

print('===============')

if len(different_versions) != 1:
    print(r'发现不同版本的扩展，请手动安装！语言包目录在 \_locales\en_US 下')
    for dirs in different_versions:
        print(dirs)
    os.system('explorer ' + path)
else:
    path = path + '\\' + different_versions[0] + '\\_locales\\en_US\\'
    try:
        if os.path.exists(path + 'messages.json.bak'):
            os.remove(path + 'messages.json.bak')
        os.rename(path + 'messages.json', path + 'messages.json.bak')
        wget.download(
            'https://cdn.jsdelivr.net/gh/DullJZ/LastPass-in-Chinese/messages.json',
            out=path + 'messages.json')
    except:
        print('\n发生错误！')

print('\n')
exitting = input('按任意键退出')
