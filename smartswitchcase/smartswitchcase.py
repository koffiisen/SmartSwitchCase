import types
import warnings


class Case:
    value = None
    func = None

    def __init__(self, value=None, func=None):
        self.value = value
        self.func = func


class SmartSwitchCase:
    def __init__(self, obj):
        self.__obj__ = obj
        self.__cases__ = []
        self.__dft__ = None
        self.__isExec__ = False
        self.__match__ = None

    def case(self, case=Case):
        if case.value and case.func:
            self.__cases__.append(case)
        else:
            warnings.warn("case value or func can't not None")
            exit()

    def default(self, func=None):
        if func:
            self.__dft__ = func
        else:
            warnings.warn("default func can't not None")
            exit()

    def exc(self):
        temp = False
        self.__isExec__ = True
        for case in self.__cases__:
            if self.__obj__ == case.value:
                self.__match__ = case
                case.func()
                temp = True
        if not temp:
            if self.__dft__:
                self.__match__ = self.__dft__
                self.__dft__()

    def result(self):
        if self.__isExec__:
            if isinstance(self.__match__, types.FunctionType):
                return self.__match__()
            elif isinstance(self.__match__, Case):
                return self.__match__.func()
            else:
                return self.__match__
        else:
            warnings.warn("Please run exec() function to get the match result")
            return None
