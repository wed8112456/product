import os 

product = []

#判斷是否存在檔案 

if os.path.isfile('product.csv'):
    print('檔案存在')
    with open('product.csv', 'r', encoding='utf-8')as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            product.append([name,price])
else:
    pass


#請使用者輸入商品，價格
while True:
    name = input('請輸入商品：')
    if name == 'q':
        break
    price = input('請輸入價格：')
    product.append([name,price])

#印出所有資訊
for data in product:
    print(data[0] + '的價格為' + data[1] + '元')

#寫入csv 
with open('product.csv', 'w', encoding='utf-8')as f:
    f.write('商品,價格\n')
    for p in product:
        f.write(p[0] + ',' + p[1] + '\n')