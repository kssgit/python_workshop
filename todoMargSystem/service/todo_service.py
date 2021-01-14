from dao.todo_file import save_todo, load_data
from exception.numbernotfound_exception import NumberNotFoundException


class TodoService:
    todos = []

    def register(self, todo):
        index = self.is_exist(todo.todoNum)
        if index < 0:
            TodoService.todos.append(todo)
            return "{0} 일정이 등록 되었습니다".format(todo.todoNum)
        else:
            return "이미 존재하는 일정번호 입니다 "

    def getAllTodos(self):

        return TodoService.todos

    def update(self, todoNum, title):
        index = self.is_exist(todoNum)
        # print("todoNum :", todoNum)
        # print("index :", index)
        if index > -1:
            TodoService.todos[index].title = title
            return "{0} 번째 일정이 수정 되었습니다".format(todoNum)
        else:
            try:
                raise NumberNotFoundException(todoNum)
            except NumberNotFoundException as updateerror:
                return str(updateerror)

    def delete(self, todoNum):
        index = self.is_exist(todoNum)
        if index > -1:
            TodoService.todos.pop(index)
            return "{0} 번째 일정이 삭제 되었습니다".format(todoNum)
        else:
            try:
                raise NumberNotFoundException(todoNum)
            except NumberNotFoundException as updateerror:
                return str(updateerror)

    def is_exist(self, todoNum):
        for index, todo in enumerate(TodoService.todos):
            # print("todo.todoNum :", todo.todoNum)
            if todo.todoNum == int(todoNum):
                return index
        return -1

    def delete_all(self):
        TodoService.todos.clear()
        return "모든 일정을 삭제 했습니다."

    def file_read(self):
        TodoService.todos = load_data()

    def file_write(self):
        save_todo(TodoService.todos)
