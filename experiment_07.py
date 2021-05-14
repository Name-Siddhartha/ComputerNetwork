# Experiment 07
# Network ID and Host ID of IPv4 address


import CustomError as CE


def DetermineClassfIPv4(InputIPAddressString):
    if len(str(InputIPAddressString)) == 0:
        raise CE.NoInputError
    else:
        # Long and short IP Address
        IPAddressBytes = InputIPAddressString.strip().split(":")
        if len(IPAddressBytes) != 4:
            print("IPv4 Address contains 4 positions arguments.")
            print(f"{len(IPAddressBytes)} positional arguments recieved")
            raise CE.InvalidInputError

        digits = list("0123456789")
        for Byte in range(4):
            for char in str(IPAddressBytes[Byte]):
                if char not in digits:
                    print(f"Byte {Byte + 1} not a number")
                    raise CE.InputNotANumberError

        IPAddressBytes = list(map(int, IPAddressBytes))

        for Byte in range(4):
            if not 0 <= IPAddressBytes[Byte] <= 255:
                print(f"Byte {Byte + 1} must lie between 0 and 255.")
                raise CE.InputOutOfRangeError

        ClassOfIPAddress = ' '
        if 0 <= IPAddressBytes[0] <= 127:
            ClassOfIPAddress = 'A'
        elif 128 <= IPAddressBytes[0] <= 191:
            ClassOfIPAddress = 'B'
        elif 192 <= IPAddressBytes[0] <= 223:
            ClassOfIPAddress = 'C'
        elif 224 <= IPAddressBytes[0] <= 239:
            ClassOfIPAddress = 'D'
        elif 240 <= IPAddressBytes[0] <= 255:
            ClassOfIPAddress = 'E'
        else:
            ClassOfIPAddress = 'Error'

        print(f"Class of IPv4 Address is : Class {ClassOfIPAddress}")
        return ClassOfIPAddress


def NetworkAndHostIDFinder(InputIPAddressString):
    if len(str(InputIPAddressString)) == 0:
        raise CE.NoInputError
    else:
        # Long and short IP Address
        IPAddressBytes = InputIPAddressString.strip().split(":")
        if len(IPAddressBytes) != 4:
            print("IPv4 Address contains 4 positions arguments.")
            print(f"{len(IPAddressBytes)} positional arguments recieved")
            raise CE.InvalidInputError

        digits = list("0123456789")
        for Byte in range(4):
            for char in str(IPAddressBytes[Byte]):
                if char not in digits:
                    print(f"Byte {Byte + 1} not a number")
                    raise CE.InputNotANumberError

        IPAddressBytes = list(map(int, IPAddressBytes))

        for Byte in range(4):
            if not 0 <= IPAddressBytes[Byte] <= 255:
                print(f"Byte {Byte + 1} must lie between 0 and 255.")
                raise CE.InputOutOfRangeError

        ClassOfIPAddress = DetermineClassfIPv4(InputIPAddressString)

        if ClassOfIPAddress == 'A':
            print(
                f"NetworkID : {InputIPAddressString[0:3]}\nHost ID : {InputIPAddressString[4:]}")
        elif ClassOfIPAddress == 'B':
            print(
                f"NetworkID : {InputIPAddressString[0:7]}\nHost ID : {InputIPAddressString[8:]}")
        elif ClassOfIPAddress == 'C':
            print(
                f"NetworkID : {InputIPAddressString[0:11]}\nHost ID : {InputIPAddressString[12:]}")
        elif ClassOfIPAddress == 'D':
            print(f"Multicast Address : {InputIPAddressString}")
        else:
            print(f"Reserved Address : {InputIPAddressString}")

        return 0


def main():
    print("\nNetworkID and HostID of IPv4 Address:")
    InputIPAddress = input("Enter a valid IPv4 address: \n")
    try:
        NetworkAndHostIDFinder(InputIPAddress)
        print('\n')
    except CE.NoInputError:
        print(CE.NoInputError())
        print("Try again")
        main()
    except CE.InputOutOfRangeError:
        print(CE.InputOutOfRangeError())
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
