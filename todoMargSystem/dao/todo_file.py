import os.path
from entity.todo import Todo


# 일정 저장
def save_todo(todos):
    save_file = open("todos.dat", "w")
    for i, todo in enumerate(todos):
        save_file.write("{0}번째 | {1},{2}\n".format(
            i, todo.todoNum, todo.title))

    save_file.close()


# 일정 로드
def load_data():
    todos = []
    fileExist = os.path.isfile("todos.dat")
    if fileExist:
        read_file = open("todos.dat", "r")
        while True:
            data = read_file.readline()
            if len(data.split("|")) == 2:
                todo = data.split("|")[1].strip("\n").split(",")
                todos.append(Todo(int(todo[0].strip()), todo[1].strip()))

            if not data:
                break

        read_file.close()
    return todos
