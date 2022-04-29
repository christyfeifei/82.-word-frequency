data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))  # 每讀一筆留言，印出數字

print('檔案讀取完了, 總共有', len(data), '筆資料')  # 印出總共幾筆留言

print(data[0])

WC = {}  # word_count
# 巢狀廻圈 Nested loop
for d in data:
    words = d.split(' ')
    for word in words:
        if word in WC:
            WC[word] += 1
        else:
            WC[word] = 1  # 新增新的key進WC(字典)
for word in WC:
    if WC[word] > 1000000:
        print(word, WC[word])

print(len(WC))

while True:
    word = input('請問你想查詢什麼字:')
    if word == 'q':
        break
    if word in WC:
        print(word, '出現過的次數為:', WC[word])
    else:
        print('這個字沒有出現過哦!')

print('感謝使用本查詢功能')


# sum_len = 0
# for d in data:
#     sum_len = sum_len + len(d)

# print('留言平均長度為', sum_len/len(data))

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('一共有', len(new), '筆, 長度小於100的資料')
# print(new[0])
# print(new[1])

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('一共有', len(good), '筆資料有提到good')
# print(good[0])
