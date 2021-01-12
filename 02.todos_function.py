import os.path
# 모듈화

todo_list = []
todoNum = 0

# 목록


def menu_display():
    print("=======TODO IT 일정 관리 시스템=======")
    print("1.일정 등록 ")
    print("2.일정 보기")
    print("3.일정 수정")
    print("4.일정 삭제")
    print("5.전체 일정 삭제")
    print("0.종료")

# 일정 등록


def register(todo):
    todo_list.append(todo)
    return "{}(을)를 등록했습니다.".format(todo["title"])


# 일정 수정
def update(index):
    i = is_Exist(index)
    if i > -1:
        set_title = input("수정할 일정을 적으세요 : ")
        todo_list[i]["title"] = set_title
        return "{0}번째 일정을 수정하였습니다.".format(index)
    return "해당 번호의 일정이 없습니다."

# 해당 일정 삭제


def del_one(index):
    i = is_Exist(index)
    if i > -1:
        todo_list.pop(i)
        return "{0}번째 일정을 삭제하였습니다.".format(index)
    return "해당 번호의 일정이 없습니다."

# 모든 일정 삭제


def del_all():
    delete = input("일정을 정말로 삭제하시겠습니까?[y/n]")
    if delete == "y" or delete == "Y":
        todo_list.clear()
        print("모든 일정이 정상적으로 삭제 되었습니다.")


# 일정 존재여부 파악


def is_Exist(index):
    for i, todo in enumerate(todo_list):
        if todo["todoNum"] == index:
            return i
    return -1

# 일정 저장


def save_toto():
    save_file = open("todos.dat", "w")
    for i, todo in enumerate(todo_list):
        save_file.write("{0}번째 | {1},{2}\n".format(
            i, todo["todoNum"], todo["title"]))

    save_file.close()

# 일정 로드


def load_data():
    fileExist = os.path.isfile("todos.dat")
    if fileExist:
        read_file = open("todos.dat", "r")
        while True:
            data = read_file.readline()
            if len(data.split("|")) == 2:
                todo = data.split("|")[1].strip("\n").split(",")
                todo_list.append({"todoNum": int(todo[0]), "title": todo[1]})
            if not data:
                break


# ------------------------------------------------
load_data()
while True:

    menu_display()

    m = input("메뉴를 선택하세요 > ")
    while not m.isdecimal():
        print("올바른 숫자를 입력하세요")
        m = input("메뉴를 선택하세요 > ")
    n = int(m)

    if n == 1:
        print("=======일정 등록=======")
        title = input("일정을 등록하세요 : ")
        todo = {"todoNum": todoNum, "title": title}

        todoNum += 1
        print(register(todo))

    elif n == 2:
        print("=======일정 보기=======")
        print(todo_list)

    elif n == 3:
        print("=======일정 수정=======")
        index = input("수정할 일정 번호를 쓰세요 : ")

        while not index.isdecimal():
            print("올바른 숫자를 입력하세요")
            index = input("수정할 일정 번호를 쓰세요 : ")

        print(update(int(index)))

    elif n == 4:
        print("=======일정 삭제=======")
        index = input("삭제할 일정 번호를 쓰세요 : ")
        while not index.isdecimal():
            print("올바른 숫자를 입력하세요")
            index = input("삭제할 일정 번호를 쓰세요 : ")
        delete = input("일정을 정말로 삭제하시겠습니까?[y/n]")
        if delete == "y" or delete == "Y":
            print(del_one(int(index)))

    elif n == 5:
        print("=======전체 일정 삭제=======")
        del_all()

    elif n == 0:
        print("=======TODO IT 프로그램이 종료 됩니다.=======")
        save_toto()
        break
    else:
        print("1,2,3,4,5,0 중 하나를 선택하세요")
