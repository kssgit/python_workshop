class RecoredNotFoundException(Exception):

    def __init__(self, message):
        super().__init__(message + "해당 p_id가 없습니다.")
