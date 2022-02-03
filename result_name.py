import win32com.client
inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

list = ['A035420', 'A137310', 'A011780', 'A071050', 'A039490', 'A298020', 'A192080', 'A023590', 'A001120', 'A161890', 'A284740', 'A006040', 'A000640', 'A001880', 'A003070', 'A001720', 'A123890', 'A009410', 'A002020', 'A024720', 'A068290', 'A013580', 'A002780', 'A016450', 'A079980', 'A092230', 'A136490', 'A011760', 'A014790', 'A004960', 'A000700', 'A004150', 'A001260', 'A134790', 'A009180', 'A002870']
result = []
for i in list:
    a = inCpStockCode.CodeToName(i)
    result.append(a)
    print(a)
print(result)