from controller.product_controller import ProductController
from view.view import menu_display, menu_input

# 클래스변수,메서드가 아니면 반드시 객체생성해서 쓰자!!!
controller = ProductController()

controller.file_read()

while True:
    menu_display()
    m = menu_input()

    if m == 1:
        controller.register()

    elif m == 2:
        controller.getAllProduct()

    elif m == 3:
        controller.update()

    elif m == 4:
        controller.delete()

    elif m == 0:
        print("프로그램을 종료합니다")
        controller.file_write()
        break

    else:
        print("0,1,2,3,4 중에 입력하세요")
