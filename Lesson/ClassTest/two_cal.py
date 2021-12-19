from one_cal import OneCal

#상속 테스트
class TwoCal(OneCal):
    def __init__(self, fst, sec):
        super().__init__(fst, sec)
        self.__t_fst = fst
        self.__t_sec = sec
    
    def minus(self):
        __t_result = self.__t_fst - self.__t_sec
        return __t_result