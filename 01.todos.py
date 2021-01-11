# github : python_workshop repository 생성 - 01.todos.py 작성해보기
#                                                 {"todoNum": todoNum , "title":title}데이터
#                                                   등록, 수정 , 삭제 , 일정목록 , 전체 삭제 기능

todo_list = []
todoNum = 1

while True:
    print("=======TODO IT 일정 관리 시스템=======")
    print("1.일정 등록 ")
    print("2.일정 보기")
    print("3.일정 수정")
    print("4.일정 삭제")
    print("5.전체 일정 삭제")
    print("0.종료")

    m = input("메뉴를 선택하세요 > ")
    while not m.isdecimal():
        print("올바른 숫자를 입력하세요")
        m = input("메뉴를 선택하세요 > ")
    n = int(m)
    if n == 1:
        print("=======일정 등록=======")
        title = input("일정을 등록하세요 : ")
        todo = {"todoNum": todoNum, "title": title}
        todo_list.append(todo)
        todoNum += 1

    elif n == 2:
        print("=======일정 보기=======")
        print(todo_list)

    elif n == 3:
        print("=======일정 수정=======")
        index = input("수정할 일정 번호를 쓰세요 : ")

        while not index.isdecimal():
            print("올바른 숫자를 입력하세요")
            index = input("수정할 일정 번호를 쓰세요 : ")

        set_title = input("수정할 일정을 적으세요 : ")
        todo_list[int(index)-1]["title"] = set_title

    elif n == 4:
        print("=======일정 삭제=======")
        index = input("삭제할 일정 번호를 쓰세요 : ")
        while not index.isdecimal():
            print("올바른 숫자를 입력하세요")
            index = input("삭제할 일정 번호를 쓰세요 : ")
        delete = input("일정을 정말로 삭제하시겠습니까?[y/n]")
        if delete == "y" or delete == "Y":
            todo_list.pop(int(index)-1)
            print("해당 일정이 정상적으로 삭제 되었습니다.")

    elif n == 5:
        print("=======전체 일정 삭제=======")
        delete = input("일정을 정말로 삭제하시겠습니까?[y/n]")
        if delete == "y" or delete == "Y":
            todo_list.clear()
            print("모든 일정이 정상적으로 삭제 되었습니다.")

    elif n == 0:
        print("=======TODO IT 프로그램이 종료 됩니다.=======")

        break
    else:
        print("1,2,3,4,5,0 중 하나를 선택하세요")
