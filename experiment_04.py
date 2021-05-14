# Experiment 04
# Cyclic Redundancy Check

import CustomError as CE


def PolynomialPowersFinder(InputPolynomial):
    if len(InputPolynomial) == 0 or InputPolynomial == None:
        raise CE.NoInputError
    else:
        ValidCharacters = list("+xX0123456789")

        for char in InputPolynomial:
            if char not in ValidCharacters:
                raise CE.InvalidInputError

        PolynomialTerms = str(InputPolynomial).strip().split("+")
        PolynomialPowers = []
        for Terms in PolynomialTerms:
            if Terms[0] == 'x' or Terms[0] == 'X':
                PolynomialPowers.append(Terms[1:])
            else:
                PolynomialPowers.append(Terms)
        if(str(InputPolynomial)[-2:] == '+1'):
            PolynomialPowers[-1] = '0'
        PolynomialPowers = list(map(int, PolynomialPowers))
        PolynomialPowers.sort(reverse=True)
        return PolynomialPowers


def BitPositionsToBinaryNumberString(ListOfBitPositions):
    BitPositionsString = ''.join(list(map(str, ListOfBitPositions)))
    ValidCharacters = list("0123456789")
    for char in BitPositionsString:
        if char not in ValidCharacters:
            print("Elements of input not a number")
            raise CE.InvalidInputError

    ListOfBitPositions = list(map(int, ListOfBitPositions))
    PowerOfTwo = list(map(lambda x: 2**x, ListOfBitPositions))

    Sum = sum(PowerOfTwo)

    return str(bin(Sum)[2:])


def XORBinaryStrings(BinaryDataString1, BinaryDataString2):
    digits = list('0123456789')

    for char in BinaryDataString1:
        if char not in digits:
            print("Input 1 is not a number")
            raise CE.InputNotANumberError

    for char in BinaryDataString2:
        if char not in digits:
            print("Input 2 is not a number")
            raise CE.InputNotANumberError

    digits = list('01')
    for char in BinaryDataString1:
        if char not in digits:
            print("Input 1 is not a binary number")
            raise CE.InvalidInputError

    for char in BinaryDataString2:
        if char not in digits:
            print("Input 2 is not a binary number")
            raise CE.InvalidInputError

    Number1 = int(BinaryDataString1, 2)
    Number2 = int(BinaryDataString2, 2)
    return bin(Number1 ^ Number2)[2:].zfill(len(BinaryDataString2) - 1)


def BinaryDivision(DividendString, DivisorString):
    digits = list('0123456789')
    for char in DividendString:
        if char not in digits:
            print("Input 1 is not a number")
            raise CE.InputNotANumberError
    for char in DivisorString:
        if char not in digits:
            print("Input 2 is not a number")
            raise CE.InputNotANumberError

    digits = list('01')
    for char in DividendString:
        if char not in digits:
            print("Input 1 is not a binary number")
            raise CE.InvalidInputError
    for char in DivisorString:
        if char not in digits:
            print("Input 2 is not a binary number")
            raise CE.InvalidInputError

    EndPointer = len(DivisorString) - 1
    RemainderString = DividendString[0:EndPointer]  # Part of Logic.
    while(EndPointer != len(DividendString)):
        Number1 = RemainderString + DividendString[EndPointer]
        if Number1[0] == '0':
            RemainderString = Number1[1:]
        else:
            RemainderString = XORBinaryStrings(Number1, DivisorString)
        EndPointer += 1
    return RemainderString


def ValidityChecker(DividendPolynomial, DivisorPolynomial):
    if len(DividendPolynomial) == 0:
        print("No input detected in Input 1")
        raise CE.NoInputError
    elif len(DivisorPolynomial) == 0:
        print("No input detected in Input 2")
        raise CE.NoInputError
    else:
        ValidCharacters = list('+xX0123456789')
        for char in DividendPolynomial:
            if char not in ValidCharacters:
                print("Input 1 not a valid Polynomial")
                raise CE.InvalidInputError

        for char in DivisorPolynomial:
            if char not in ValidCharacters:
                print("Input 2 not a valid Polynomial")
                raise CE.InvalidInputError

        # Check + followed by x
        for charPosition in range(len(DividendPolynomial) - 1):
            if DividendPolynomial[charPosition] == '+':
                if DividendPolynomial[charPosition + 1] not in list('xX1'):
                    print("Coefficient of all terms of Dividend must be 1")
                    raise CE.InvalidInputError
            # Reverse check for missing + sign
            if DividendPolynomial[charPosition] in ['x', 'X'] and charPosition != 0:
                if DividendPolynomial[charPosition - 1] != '+':
                    print("Missing + sign between terms in Input 1")
                    raise CE.InvalidInputError

        for charPosition in range(len(DivisorPolynomial) - 1):
            if DivisorPolynomial[charPosition] == '+':
                if DivisorPolynomial[charPosition + 1] not in list('xX1'):
                    print("Coefficient of all terms of Divisor must be 1")
                    raise CE.InvalidInputError
            # Reverse check for missing + sign
            if DivisorPolynomial[charPosition] in ['x', 'X'] and charPosition != 0:
                if DivisorPolynomial[charPosition - 1] != '+':
                    print("Missing + sign between terms in Input 2")
                    raise CE.InvalidInputError

        # Check + 1 at the end
        CountXAfterLastPlus = 0

        charPosition = len(DividendPolynomial) - 1
        while DividendPolynomial[charPosition] != '+':
            if DividendPolynomial[charPosition] in ['x', 'X']:
                CountXAfterLastPlus += 1
            charPosition -= 1
        if CountXAfterLastPlus == 0 and DividendPolynomial[-2:] != '+1':
            print("Constant term in Input 1 must be 1")
            raise CE.InvalidInputError

        charPosition = len(DivisorPolynomial) - 1
        while DivisorPolynomial[charPosition] != '+':
            if DivisorPolynomial[charPosition] in ['x', 'X']:
                CountXAfterLastPlus += 1
            charPosition -= 1
        if CountXAfterLastPlus == 0 and DivisorPolynomial[-2:] != '+1':
            print("Constant term in Input 2 must be 1")
            raise CE.InvalidInputError

        # Leading character is x

        if DividendPolynomial[0] not in ['x', 'X']:
            print("Coefficient of leading term of Dividend must 1")
            raise CE.InvalidInputError

        if DivisorPolynomial[0] not in ['x', 'X']:
            print("Coefficient of leading term of Divisor must 1")
            raise CE.InvalidInputError

        DividendBitPositions = PolynomialPowersFinder(DividendPolynomial)
        DivisorBitPositions = PolynomialPowersFinder(DivisorPolynomial)

        if DivisorBitPositions[0] > DividendBitPositions[0]:
            print("Degree of Divisor Polynomial must be less than Divdend Polynomial")
            raise CE.InputLengthMismatchError

        ModifiedDividendBitPositions = list(
            map(lambda x: x + DivisorBitPositions[0], DividendBitPositions))

        DividendBinaryString = BitPositionsToBinaryNumberString(
            DividendBitPositions)
        ModifiedDividendBinaryString = BitPositionsToBinaryNumberString(
            ModifiedDividendBitPositions)
        DivisorBinaryString = BitPositionsToBinaryNumberString(
            DivisorBitPositions)

        # Quotient = ModifiedDividend // Divisor
        # Remainder = ModifiedDividend - (Divisor * Quotient)

        CheckValueBinaryString = BinaryDivision(
            ModifiedDividendBinaryString, DivisorBinaryString)
        print(
            f"\nDividend: {DividendBinaryString} {''.zfill(DivisorBitPositions[0])}")
        print(f"Divisor: {DivisorBinaryString}")
        print(f"Check Value: {CheckValueBinaryString}")

        # CheckValue = Remainder
        ModifiedDividendWithCheckValue = DividendBinaryString + CheckValueBinaryString
        # NewQuotient = ModifiedDividendWithCheckValue // Divisor
        # NewRemainder = ModifiedDividendWithCheckValue - (Divisor * NewQuotient)

        FinalRemainderBinaryString = BinaryDivision(
            ModifiedDividendWithCheckValue, DivisorBinaryString)
        print(
            f"\nNew Dividend: {DividendBinaryString} {CheckValueBinaryString.zfill(DivisorBitPositions[0])}")
        print(f"Divisor: {DivisorBinaryString}")
        print(f"NewRemainder: {FinalRemainderBinaryString}")

        if FinalRemainderBinaryString == ''.zfill(DivisorBitPositions[0]):
            print("Cyclic Redundancy Check success")
        else:
            print("Cyclic Redundancy Check failed")

        return 0


def main():
    print('\nCyclic Redundancy Check:\n')
    print("Sample input Polynomial:")
    print("x3+x2+1")
    print("x7+x4+x2+x1")
    print("\nCoefficient of all non zero terms of polynomial must be 1")
    print("Constant term must be 1\n")
    InputDividendPolynomial = input(
        "Enter Message Polynomial (Dividend Polynomial):\n").strip()
    InputDivisorPolynomial = input(
        "Enter Check Polynomial (Divisor Polynomial):\n").strip()
    try:
        ValidityChecker(
            InputDividendPolynomial, InputDivisorPolynomial)
        print('\n')
    except CE.NoInputError:
        print(CE.NoInputError())
        print("Try again")
        main()
    except CE.InputLengthMismatchError:
        print(CE.InputLengthMismatchError())
        print("Try again")
        main()
    except CE.InputNotANumberError:
        print(CE.InputNotANumberError())
        print("Try again")
        main()
    except CE.InvalidInputError:
        print(CE.InvalidInputError())
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
