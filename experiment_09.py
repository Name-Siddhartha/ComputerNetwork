# Experiment 09
# Distance Vector Routing Algorithm
# Also known as Bellman Ford algorithm

import CustomError as CE


def MinCostMatrixFinder(InputNumberOfNodes):
    # Check Validity of Cost Matrix.
    print(f"Sample input for Cost Matrix for 3 nodes:")
    print(f"0 1 2")
    print(f"1 0 3")
    print(f"2 3 0")

    print(f"Sample input Cost Matrix for 4 nodes:")
    print(f"0 1 2 3")
    print(f"1 0 4 5")
    print(f"2 4 0 6")
    print(f"3 5 6 0")

    print("1. Distance from a node to itself must be 0")
    print("2. Distance from node i to node j must be")
    print("   equal to distance from node j to node i")
    print("3. Put distance 999999 if no link between two nodes")

    print(f"\n\nEnter the cost matrix for {InputNumberOfNodes} nodes.")
    InputNumberOfNodes = str(InputNumberOfNodes)

    for char in InputNumberOfNodes:
        if char not in list("0123456789"):
            raise CE.InputNotANumberError

    InputNumberOfNodes = int(InputNumberOfNodes)

    CostMatrix = []
    for _ in range(InputNumberOfNodes):
        row = input()
        CostMatrix.append(row)

    # Check for dimensions
    for rowNumber in range(InputNumberOfNodes):
        row = str(CostMatrix[rowNumber]).strip().split(" ")
        if len(row) != InputNumberOfNodes:
            print(
                f"{rowNumber + 1} expected {InputNumberOfNodes}. Recieved {len(row)}")
            raise CE.InputLengthMismatchError
        CostMatrix[rowNumber] = row

    # Check for number
    for rowNumber in range(InputNumberOfNodes):
        for colNumber in range(InputNumberOfNodes):
            for char in str(CostMatrix[rowNumber][colNumber]):
                if char not in list('0123456789'):
                    print(
                        f"Input row {rowNumber + 1}, col {colNumber + 1} is not a number")
                    raise CE.InputNotANumberError
            CostMatrix[rowNumber][colNumber] = int(
                CostMatrix[rowNumber][colNumber])

    # Check for matrix[i][i] = 0 & matrix[i][j] == matrix[j][i]
    for rowNumber in range(InputNumberOfNodes):
        for colNumber in range(InputNumberOfNodes):
            if rowNumber == colNumber and CostMatrix[rowNumber][colNumber] != 0:
                print(
                    f"Distance between node {rowNumber + 1} and {rowNumber + 1} must be 0")
                raise CE.InvalidInputError
            elif CostMatrix[rowNumber][colNumber] != CostMatrix[colNumber][rowNumber]:
                print(
                    f"Distance between node {rowNumber + 1} and {colNumber + 1} undefined")
                raise CE.InvalidInputError
            else:
                pass

    DistanceMatrix = CostMatrix.copy()
    count = 1
    while count != 0:
        count = 0
        for startingNode in range(InputNumberOfNodes):
            for endingNode in range(InputNumberOfNodes):
                for middleNode in range(InputNumberOfNodes):
                    if DistanceMatrix[startingNode][endingNode] != min(
                            CostMatrix[startingNode][middleNode] + DistanceMatrix[middleNode][endingNode], DistanceMatrix[startingNode][endingNode]):
                        count += 1
                        DistanceMatrix[startingNode][endingNode] = min(
                            CostMatrix[startingNode][middleNode] + DistanceMatrix[middleNode][endingNode], DistanceMatrix[startingNode][endingNode])
    return DistanceMatrix


def main():
    print("\nDistance Vector Routing Algorithm")
    NumberOfNodes = input("Enter the number of nodes in the network: \n")
    for char in NumberOfNodes:
        if char not in list("0123456789"):
            raise CE.InputNotANumberError
    NumberOfNodes = int(NumberOfNodes)
    try:
        CostMatrixOfNodes = MinCostMatrixFinder(NumberOfNodes)
        print('\n')
        for startingNode in range(NumberOfNodes):
            for endingNode in range(NumberOfNodes):
                print(
                    f"Min distance between {startingNode + 1} and {endingNode + 1} is {CostMatrixOfNodes[startingNode][endingNode]}")
            print('\n')
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
