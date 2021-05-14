# Experiment 03
# Character Stuffing and Destuffing
# Flag and Escape Sequence needed

import CustomError as CE
import re


def CharacterStuffing(InputCharacterString, InputFlagSequence, InputEscapeSequence):
    if len(InputCharacterString) == 0:
        raise CE.NoInputError
    elif str(InputFlagSequence) == str(InputEscapeSequence):
        print("Escape Sequence cannot be the same as Flag Sequence")
        raise CE.InvalidInputError
    else:
        StuffedCharacterString = InputCharacterString.replace(
            InputEscapeSequence, InputEscapeSequence*2)
        StuffedCharacterString = StuffedCharacterString.replace(
            InputFlagSequence, InputEscapeSequence + InputFlagSequence)
    print(
        f"Stuffed bit string for input\n\'{InputCharacterString}\' is : \n{StuffedCharacterString}")
    return StuffedCharacterString


def CharacterDestuffing(InputCharacterString, InputFlagSequence, InputEscapeSequence):
    if len(InputCharacterString) == 0:
        raise CE.NoInputError
    CountOnlyFlagSequence = len([index.start() for index in re.finditer(
        InputFlagSequence, InputCharacterString)])
    CountFlagWithEscapeSequence = len([index.start() for index in re.finditer(
        InputEscapeSequence + InputFlagSequence, InputCharacterString)])
    CountOnlyEscapeSequence = len([index.start() for index in re.finditer(
        InputEscapeSequence, InputCharacterString)])
    CountEscapeWithEscapeSequence = len([index.start() for index in re.finditer(
        InputEscapeSequence*2, InputCharacterString)])
    if int(CountOnlyFlagSequence) != int(CountFlagWithEscapeSequence):
        print("Flag Sequence must be preceded by the Escape Sequence")
        raise CE.InvalidInputError
    elif int(CountOnlyEscapeSequence) != 2 * int(CountEscapeWithEscapeSequence) + int(CountOnlyFlagSequence):
        print("Escape Sequence must be preceded by the Escape Sequence")
        raise CE.InvalidInputError
    else:
        pass
        DestuffedCharacterString = InputCharacterString.replace(
            InputEscapeSequence*2, InputEscapeSequence)
        DestuffedCharacterString = DestuffedCharacterString.replace(
            InputEscapeSequence + InputFlagSequence, InputFlagSequence)
        print(
            f"Destuffed bit string for input\n\'{InputCharacterString}\' is : \n{DestuffedCharacterString}")
        return DestuffedCharacterString


def main():
    print('\nCharacter stuffing and destuffing:\n')
    InputString = input("Enter a string of characters:\n")
    FlagSequence = input("Enter the flag sequence:\n")
    EscapeSequence = input("Enter the escape sequence:\n")
    try:
        StuffedCharacterString = CharacterStuffing(
            InputString, FlagSequence, EscapeSequence)
        CharacterDestuffing(StuffedCharacterString,
                            FlagSequence, EscapeSequence)
        print('\n')
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
