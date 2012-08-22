
s = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''
min = 97
max = 122
def judge(num):
    if num <= max and num >= min:
        rst = num+2
        if rst > max:
            rst = min+rst-max-1
    else:
        rst = num
    return rst

def x(s):
    ss = ''
    for i in s:
        num = ord(i)
        ss += chr(judge(num))
    return ss

print x(s)

table = string.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
s.translate(table)


for x in s:
	if ord(x)>=ord('a') and ord(x)<=ord('z'):
		o+=chr((ord(x)+2-ord('a'))%26+ord('a'))
	else:
		o+=x
print o

