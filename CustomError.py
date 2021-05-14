CustomErrCodes = {
    0: "No Error",
    1: "Error not defined",
    100: "No input detected",
    101: "Negative Value Encountered",
    102: "Positive Value Encountered",
    103: "Valid input not detected",
    104: "Input not an integer",
    105: "Input Length Mismatch",
    106: "Input out of range"
}


class CustomError(Exception):
    def __init__(self, code=0):
        self.errCode = code
        if code not in CustomErrCodes.keys():
            self.errCode = 1
        # self.errMessage = CustomErrCodes[code]

    def __str__(self):
        super().__init__()
        return (f"Error {self.errCode}: {CustomErrCodes[self.errCode]}")


class NegativeValueError(CustomError):
    def __init__(self):
        pass

    def __str__(self):
        super().__init__()
        return str(CustomError(101))


class PositiveValueError(CustomError):
    def __init__(self):
        pass

    def __str__(self):
        super().__init__()
        return str(CustomError(102))


class NoInputError(CustomError):
    def __init__(self):
        pass

    def __str__(self):
        super().__init__()
        return str(CustomError(100))


class InputNotANumberError(CustomError):
    def __init__(self):
        pass

    def __str__(self):
        super().__init__()
        return str(CustomError(104))


class InvalidInputError(CustomError):
    def __init__(self):
        pass

    def __str__(self):
        super().__init__()
        return str(CustomError(103))


class InputLengthMismatchError(CustomError):
    def __init__(self):
        pass

    def __str__(self):
        super().__init__()
        return str(CustomError(105))


class InputOutOfRangeError(CustomError):
    def __init__(self):
        pass

    def __str__(self):
        super().__init__()
        return str(CustomError(106))
