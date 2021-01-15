from exception.recordernotfound_exception import RecoredNotFoundException
from exception.duplication_exception import DuplicationException

from dao.product_file import file_read, file_write


class ProductService:
    # 클래스 변수 products
    products = []

    # register

    def register(self, product):
        index = self.is_exist(product.p_id)
        if index < 0:
            ProductService.products.append(product)
            return "{} 상품이 정상 등록 되었습니다.".format(product.p_id)

        else:
            try:
                raise DuplicationException
            except DuplicationException as insertError:
                return str(insertError)

    # 모든 상품 정보 보여주기

    def getAllProduct(self):
        return ProductService.products

    # 상품정보 삭제

    def delete(self, p_id):
        index = self.is_exist(p_id)
        if index > -1:
            ProductService.products.pop(index)
            return "{} 상품정보가 삭제 되었습니다.".format(p_id)
        else:
            try:
                raise RecoredNotFoundException
            except RecoredNotFoundException as notfoundError:
                return str(notfoundError)

    # 상품 정보 수정

    def update(self, p_id, p_name, price):
        index = self.is_exist(p_id)
        if index > -1:
            ProductService.products[index].p_id = p_id
            ProductService.products[index].p_name = p_name
            ProductService.products[index].price = price
            return "{} 상품정보가 수정 되었습니다.".format(p_id)
        else:
            try:
                raise RecoredNotFoundException
            except RecoredNotFoundException as notfoundError:
                return str(notfoundError)

    # 상품 id 조회

    def is_exist(self, p_id):
        for index, product in enumerate(ProductService.products):
            if product.p_id == p_id:
                return index
        return -1

    # 상품 정보 저장

    def file_write(self):
        file_write(ProductService.products)

    # 상품 정보 데이타 가져오기
    def file_read(self):
        ProductService.products = file_read()
