import sys
import re

str1 = sys.argv[1]
printFail = False
errorMsg = []

regex_string = re.search('[a-zA-Z]+', str1)
if regex_string is None:
    printFail = True
    errorMsg.append('缺少英文')

regex_number = re.search('[0-9]+', str1)
if regex_number is None:
    printFail = True
    errorMsg.append('缺少數字')

regex_symbol = re.search('[^[a-zA-Z0-9\s]+', str1)
if regex_symbol is None:
    printFail = True
    errorMsg.append('缺少符號')

regex_lenMin = re.search('.{8,16}', str1)
if (regex_lenMin is None):
    printFail = True
    errorMsg.append('長度須大於8')

regex_lenMax = re.search('.{17,}', str1)
if (regex_lenMax is not None):
    printFail = True
    errorMsg.append('長度須小於16')



regex_upper = re.search('[A-Z]+', str1)
if (regex_upper is None):
    printFail = True
    errorMsg.append('缺少英文大寫')

str1 = ''.join(re.findall('[a-zA-Z0-9]*', str1))
for i in range(len(str1)):
    if i>0:
        if ord(str1[i])==(ord(str1[i-1])+1):
            printFail = True
            errorMsg.append('字母與數字不可以連序')
            break


if (printFail):
    print('輸入字串不符合以下規則：')
    print('、'.join(errorMsg))
else :
    print('success')
