import os.path
from entity.product import Product


# 저장 파일 로드
def file_read():
    products = []
    fileExist = os.path.isfile("product.dat")
    if fileExist:
        read_file = open("product.dat", "r")
        while True:
            data = read_file.readline()
            if len(data.split("|")) == 2:
                product = data.split("|")[1].strip("\n").split(",")
                products.append(Product(product[0].strip, product[1].strip, int(
                    product[2].strip), product[3].strip))
            if not data:
                break
        read_file.close()
    return products


# 데이터 파일에 저장
def file_write(products):
    save_file = open("product.dat", "w")
    for index, product in enumerate(products):
        save_file.write("{0}번째 | {1},{2},{3},{4}\n".format(
            product.p_id, product.p_name, product.price, product.description))

    save_file.close()
