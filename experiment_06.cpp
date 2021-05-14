// Experiment 06
// Sliding Window Protocol

#include <stdio.h>

using namespace std;

int main()
{
    printf("Sliding Window Protocol simulation:\n\n");
    int WindowSize, i, NumberOfFrames, ArrayOfFrames[50];
    printf("Choose a Window size for Transmission: \n");
    scanf("%d", &WindowSize);

    printf("\nChoose the Number of frames to be Tranmitted: \n");
    scanf("%d", &NumberOfFrames);

    printf("\nEnter Data to be transmitted in %d frames \n", NumberOfFrames);
    for (i = 1; i <= NumberOfFrames; i++)
        scanf("%d", &ArrayOfFrames[i]);
    printf("Waiting for acknowledgement\n");
    for (i = 1; i <= NumberOfFrames; i++)
    {
        if (i % WindowSize == 0)
        {
            printf("%d\n", ArrayOfFrames[i]);
            printf("Acknowledgement received for %d frames\n", WindowSize);
        }
        else
            printf("%d ", ArrayOfFrames[i]);
    }
    if (NumberOfFrames % WindowSize != 0)
        printf("\nAcknowledgement recieved for %d frames\n", NumberOfFrames % WindowSize);

    printf("\n\nProgram executed successfully\n\n");
    return 0;
}
