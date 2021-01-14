class Todo:
    def __init__(self, todoNum, title):
        self.todoNum = todoNum
        self.title = title

    def __eq__(self, title):
        if self.title == title:
            return True
        else:
            return False

    def __str__(self):
        return "일정 번호:{} 타이틀:{}".format(self.todoNum, self.title)
