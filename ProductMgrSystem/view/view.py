from entity.product import Product


def menu_display():
    print("=======상품 등록 서비스 프로그램=======")
    print("1.상품 등록 ")
    print("2.등록된 상품 보기")
    print("3.상품 정보 수정")
    print("4.상품 삭제")
    print("0.종료")


def menu_input():
    menu = input("메뉴를 선택하세요 : ")
    return int(menu)


def input_display():
    print("===상품 등록===")
    p_id = input("상품 id를 적으세여 :")
    p_name = input("상품 이름을 적으세여 :")
    price = int(input("상품의 가격을 적으세요 :"))
    description = input("상품 설명:")
    return Product(p_id, p_name, price, description)


def delete_display():
    print("===상품 삭제===")
    p_id = input("삭제할 p_id를 입력하세요 : ")
    return p_id


def message_display(message):
    print(message)


def list_display(products):
    print("===상품 목록 보기===")
    for product in products:
        print(product)


def update_display():
    print("===상품 수정===")
    p_id = input("상품 id를 입력하세요 : ")
    p_name = input("상품 이름을 입력하세요 : ")
    price = input("상품 가격을 입력하세요 : ")
    return (p_id, p_name, price)
