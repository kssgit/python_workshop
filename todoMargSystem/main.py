from view.todo_display import menu_display, menu_select, message_display
from view.todo_display import input_display, update_display, delete_display
from controller.todo_controller import TodoController

controller = TodoController()

controller.file_read()


while True:

    menu_display()
    n = menu_select()

    if n == 1:
        todo = input_display()
        controller.register(todo)

    elif n == 2:
        controller.getAllTodos()

    elif n == 3:
        todoNum, title = update_display()
        controller.update(todoNum, title)

    elif n == 4:
        todoNum = delete_display()
        controller.delete(todoNum)

    elif n == 5:
        print("=======전체 일정 삭제=======")
        controller.delete_all()
    elif n == 0:
        print("=======TODO IT 프로그램이 종료 됩니다.=======")
        controller.file_write()
        break
    else:
        print("1,2,3,4,5,0 중 하나를 선택하세요")
