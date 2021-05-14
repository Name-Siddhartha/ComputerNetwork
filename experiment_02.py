# Experiment 02
# Bit Stuffing and Destuffing

import CustomError as CE


def BitStuffing(InputBinaryDataString):
    if len(InputBinaryDataString) == 0:
        raise CE.NoInputError
    else:
        ListOfCharacters = list(InputBinaryDataString)

        digits = list('0123456789')
        for char in ListOfCharacters:
            if char not in digits:
                raise CE.InputNotANumberError

        digits = list('01')
        for char in ListOfCharacters:
            if char not in digits:
                raise CE.InvalidInputError

        StuffedBitString = []
        CounterFor1Bits = 0
        for char in ListOfCharacters:
            StuffedBitString.append(char)
            if char == '1':
                CounterFor1Bits += 1
            else:
                CounterFor1Bits = 0
            if CounterFor1Bits == 5:
                StuffedBitString.append('0')
                CounterFor1Bits = 0
        StuffedBitString = ''.join(StuffedBitString)
    print(
        f"Stuffed bit string for input\n{InputBinaryDataString} is : \n{StuffedBitString}")
    return StuffedBitString


def BitDestuffing(InputBinaryDataString):
    if len(InputBinaryDataString) == 0:
        raise CE.NoInputError
    else:
        ListOfCharacters = list(InputBinaryDataString)

        digits = list('0123456789')
        for char in ListOfCharacters:
            if char not in digits:
                raise CE.InputNotANumberError

        digits = list('01')
        for char in ListOfCharacters:
            if char not in digits:
                raise CE.InvalidInputError

        CounterFor1Bits = 0

        for char in ListOfCharacters:
            if char == '1':
                CounterFor1Bits += 1
            else:
                CounterFor1Bits = 0
            if CounterFor1Bits > 5:
                raise CE.InvalidInputError

        DestuffedBitString = []
        CounterFor1Bits = 0
        for char in ListOfCharacters:
            if CounterFor1Bits != 5:
                DestuffedBitString.append(char)
            if char == '1':
                CounterFor1Bits += 1
            else:
                CounterFor1Bits = 0
        DestuffedBitString = ''.join(DestuffedBitString)
        print(
            f"Destuffed bit string for input\n{InputBinaryDataString} is : \n{DestuffedBitString}")
        return DestuffedBitString


def main():
    print('\nBit stuffing and destuffing:\n')
    InputString = input("Enter a binary data string:\n")
    try:
        StuffedBitString = BitStuffing(InputString)
        BitDestuffing(StuffedBitString)
        print('\n')
    except CE.InputNotANumberError:
        print(CE.InputNotANumberError())
        print("Try again")
        main()
    except CE.InvalidInputError:
        print(CE.InvalidInputError())
        print("Try again")
        main()
    except CE.NoInputError:
        print(CE.NoInputError())
        print("Try again")
        main()
    finally:
        print("Main Function executed successfully")
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Undefined Exception Occurred")
    finally:
        print("Program executed successfully")
