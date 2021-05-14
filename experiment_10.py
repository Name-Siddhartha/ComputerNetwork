# Experiment 10
# Link State Routing Algorithm
# Basically Dijkstra's algorithm

import CustomError as CE
from collections import defaultdict

MAX_INT = 999999


def minDistance(InputNumberOfNodes, DistanceMatrix, VisitedNode):
    MinimumDistance = MAX_INT
    for EndNode in range(InputNumberOfNodes):
        if DistanceMatrix[EndNode] < MinimumDistance and VisitedNode[EndNode] == False:
            MinimumDistance = DistanceMatrix[EndNode]
            MinimumIndex = EndNode

    return MinimumIndex


def MinCostMatrixFinder(InputNumberOfNodes, StartingNode):
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
    StartingNode = int(StartingNode)

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

    DistanceMatrix = [MAX_INT] * InputNumberOfNodes
    DistanceMatrix[StartingNode] = 0
    VisitedNode = [False] * InputNumberOfNodes

    for cout in range(InputNumberOfNodes):
        Node = minDistance(InputNumberOfNodes, DistanceMatrix, VisitedNode)
        VisitedNode[Node] = True
        for EndNode in range(InputNumberOfNodes):
            if CostMatrix[Node][EndNode] > 0 and VisitedNode[EndNode] == False and DistanceMatrix[EndNode] > DistanceMatrix[Node] + CostMatrix[Node][EndNode]:
                DistanceMatrix[EndNode] = DistanceMatrix[Node] + \
                    CostMatrix[Node][EndNode]

    print(f"Distance of each Node from Source Node {StartingNode}")
    for Node in range(InputNumberOfNodes):
        if Node != StartingNode:
            print(Node, "is at a distance", DistanceMatrix[Node])


def main():
    print("\nLink State Routing Algorithm: ")
    NumberOfNodes = input("Enter the number of nodes in the network: \n")
    for char in NumberOfNodes:
        if char not in list("0123456789"):
            raise CE.InputNotANumberError
    NumberOfNodes = int(NumberOfNodes)

    StartNode = input(
        f"Enter a Start Node in the range 0 to {NumberOfNodes}: \n")
    for char in StartNode:
        if char not in list("0123456789"):
            raise CE.InputNotANumberError
    StartingNode = int(StartNode)
    if not 0 <= StartingNode < NumberOfNodes:
        print("Invalid Start Node")
        raise CE.InvalidInputError
    try:
        MinCostMatrixFinder(NumberOfNodes, StartingNode)
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
