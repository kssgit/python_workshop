from service.todo_service import TodoService
from view.todo_display import message_display, list_display


class TodoController:

    def register(self, todo):
        service = TodoService()
        message = service.register(todo)
        message_display(message)

    def getAllTodos(self):
        service = TodoService()
        todos = service.getAllTodos()
        list_display(todos)

    def update(self, todoNum, title):
        service = TodoService()
        message = service.update(todoNum, title)
        message_display(message)

    def delete(self, todoNum):
        service = TodoService()
        message = service.delete(todoNum)
        message_display(message)

    def delete_all(self):
        service = TodoService()
        message = service.delete_all()
        message_display(message)

    def file_read(self):
        service = TodoService()
        service.file_read()

    def file_write(self):
        service = TodoService()
        service.file_write()
