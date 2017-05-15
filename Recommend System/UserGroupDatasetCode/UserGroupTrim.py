# UserCount = {}
# with open('D:/Workplace/BigData/DataTrim/usercount_clean.txt', 'r', encoding="utf8") as rf1:
#     for line1 in rf1:
#         line1 = line1.strip()
#         a = line1.split(',')
#         UserCount[str(a[0])] = int(a[1])
#     rf1.close()
#
# with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim.txt', 'r', encoding="utf8") as rf2:
#     with open('D:/Workplace/BigData/DataTrim/review_and_usercount.txt', 'w', encoding="utf8") as wf:
#         n = 0
#         for line2 in rf2:
#             line2 = line2.strip()
#             b = line2.split(',')
#             # print(str(b[0]))
#             try:
#                 UserCount[str(b[0])]
#                 n = n + 1
#             except:
#                 print("=============" + b[0])
#         print(n)
#         wf.close()
#     rf2.close()


UserCount = {}
with open('D:/Workplace/BigData/DataTrim/_user_gz_output_usercounts.txt_part-00000', 'r', encoding="utf8") as rf1:
    for line1 in rf1:
        if 'u' in str(line1):
            print('!')
        if '43836841' in str(line1):
            print('*****')
    rf1.close()