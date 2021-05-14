# Experiment 01
# Calculate Hamming Distance

import CustomError as CE


def FindSetBits(number):
    digits = list('0123456789')
    NumberString = list(str(number))

    for digit in NumberString:
        if digit not in digits:
            raise CE.InputNotANumberError
    Sum = 0
    for digit in NumberString:
        Sum = Sum + int(digit)

    return Sum


def BinaryStringXORCalculator(BinaryString1, BinaryString2):
    BinaryDigits1 = list(map(int, BinaryString1))
    BinaryDigits2 = list(map(int, BinaryString2))
    XORValue = []

    for digit in range(len(BinaryDigits1)):
        XORDigit = BinaryDigits1[digit] ^ BinaryDigits2[digit]
        XORValue.append(XORDigit)

    XORValue = int(''.join(list(map(str, XORValue))))
    return XORValue


def CalculateHammingDistance(InputBinaryDataString1, InputBinaryDataString2):
    if len(InputBinaryDataString1) == 0:
        print("No input detected in Input 1")
        raise CE.NoInputError
    elif len(InputBinaryDataString2) == 0:
        print("No input detected in Input 2")
        raise CE.NoInputError
    elif len(InputBinaryDataString1) != len(InputBinaryDataString2):
        raise CE.InputLengthMismatchError
    else:
        digits = list('01')
        CharactersString1 = list(InputBinaryDataString1)
        for char in CharactersString1:
            if char not in digits:
                print("Input 1 not a Binary Data String")
                raise CE.InvalidInputError
        CharactersString2 = list(InputBinaryDataString2)
        for char in CharactersString2:
            if char not in digits:
                print("Input 2 not a Binary Data String")
                raise CE.InvalidInputError

        XORValue = BinaryStringXORCalculator(
            InputBinaryDataString1, InputBinaryDataString2)
        print(
            f"\nHamming Distance betweeen\n{InputBinaryDataString1} and\n{InputBinaryDataString2}\nis: {FindSetBits(XORValue)}")
        return 0


def main():
    print('\nHamming Distance Calculator: \n')
    InputString1 = input("Enter a binary data string: \n")
    InputString2 = input("Enter another binary data string: \n")
    try:
        CalculateHammingDistance(InputString1, InputString2)
        print('\n')
    except CE.InputNotANumberError:
        print(CE.InputNotANumberError())
        print("Try again")
        main()
    except CE.InputLengthMismatchError:
        print(CE.InputLengthMismatchError())
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
        print("Uncatched Exception Occurred")
    finally:
        print("Program executed successfully")
