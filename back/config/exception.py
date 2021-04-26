class UnauthorizedException(Exception):
    def __init__(self):
        super().__init__('인증 실패')


class NotFoundException(Exception):
    def __init__(self):
        super().__init__('해당하는 데이터 없음')
