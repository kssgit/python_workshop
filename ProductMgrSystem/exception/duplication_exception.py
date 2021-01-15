class DuplicationException(Exception):
    def __init__(self, message):
        super().__init__(message + "중복된 p_id 입니다")
