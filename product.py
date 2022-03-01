import os


# 讀取檔案
def read_file(filesname):
    products = []
    with open(filesname, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products


# 使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品：')
        if name == 'q':
            break
        price = input('請輸入價格：')
        products.append([name, price])
    return products


# 印出紀錄
def print_date(products):
    for data in products:
        print(data[0] + '的價格為' + data[1] + '元')

# 寫入紀錄


def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    products = []
    filesname = 'product.csv'
    if os.path.isfile(filesname):
        print('檔案存在')
        products = read_file(filesname)
    else:
        pass
    products = user_input(products)
    print_date(products)
    write_file(filesname, products)


main()
