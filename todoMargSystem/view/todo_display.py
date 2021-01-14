from service.todo_service import TodoService
from entity.todo import Todo


def menu_display():
    print("=======TODO IT 일정 관리 시스템=======")
    print("1.일정 등록 ")
    print("2.일정 보기")
    print("3.일정 수정")
    print("4.일정 삭제")
    print("5.전체 일정 삭제")
    print("0.종료")


# menu select
def menu_select():
    menu = input("메뉴를 선택하세요 : ")
    return int(menu)


# message display
def message_display(message):
    print(message)


# todo list display

def list_display(todos):
    print("===일정 목록===")
    for todo in todos:
        print(todo)


def delete_display():
    todoNum = input("삭제할 일정 번호를 적으세요 :")
    return todoNum


# todo input display
def input_display():
    title = input("일정을 입력하세요 :")
    todoNum = int(input("일정 번호를 입력하세요 "))
    return Todo(todoNum, title)


def update_display():
    todoNum = input("일정 번호를 입력하세요 : ")
    title = input("변경할 일정을 입려하세요 : ")
    return (todoNum, title)
