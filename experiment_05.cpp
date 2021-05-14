//Experiment 05
//Stop and Wait Protocol

#include <iostream>
#include <time.h>
#include <cstdlib>
#include <ctime>
#include <unistd.h>

using namespace std;

class timer
{
    private:
        unsigned long StartTime;

    public:
        void start()
        {
            StartTime = clock();
        }
        unsigned long ElapsedTimeCalculator()
        {
            return ((unsigned long)clock() - StartTime) / CLOCKS_PER_SEC;
        }
        bool TimeoutChecker(unsigned long TimeElapsedInSeconds)
        {
            return TimeElapsedInSeconds >= ElapsedTimeCalculator();
        }
};

int main()
{
    printf("Stop and Wait Protocol simulation:\n\n");
    int ArrayOfFrames[] = {1, 2, 3, 4, 5};
    unsigned long TimeElapsedInSeconds = 7;
    srand(time(NULL));
    timer DurationTimer;
    cout << "Sender has to send Frames : ";
    for (int i = 0; i < 4; i++)
        cout << ArrayOfFrames[i] << " ";
    cout << endl;
    int FramesCounter = 0;
    bool DelayInTransmission = false;
    cout << endl
         << "Sender\t\t\t\t\tReceiver" << endl;
    do
    {
        bool TimeoutInTransmission = false;
        cout << "Sending Frame : " << ArrayOfFrames[FramesCounter];
        cout.flush();
        cout << "\t\t";
        DurationTimer.start();
        if (rand() % 2)
        {
            int to = 24600 + rand() % (64000 - 24600) + 1;
            for (int i = 0; i < 64000; i++)
                for (int j = 0; j < to; j++)
                {
                }
        }
        if (DurationTimer.ElapsedTimeCalculator() <= TimeElapsedInSeconds)
        {
            cout << "Received Frame : " << ArrayOfFrames[FramesCounter] << " ";
            if (DelayInTransmission)
            {
                cout << "Duplicate";
                DelayInTransmission = false;
            }
            cout << endl;
            FramesCounter++;
        }
        else
        {
            cout << "Recieved Frame : None" << endl;
            cout << "Timeout" << endl;
            TimeoutInTransmission = true;
        }
        DurationTimer.start();
        if (rand() % 2 || !TimeoutInTransmission)
        {
            int to = 24600 + rand() % (64000 - 24600) + 1;
            for (int i = 0; i < 64000; i++)
                for (int j = 0; j < to; j++)
                {
                }
            if (DurationTimer.ElapsedTimeCalculator() > TimeElapsedInSeconds)
            {
                cout << "Delayed Acknowledgement" << endl;
                FramesCounter--;
                DelayInTransmission = true;
            }
            else if (!TimeoutInTransmission)
                cout << "Acknowledgement Received for Frame : " << ArrayOfFrames[FramesCounter] - 1 << endl;
        }
    } while (FramesCounter != 4);

    printf("\n\nProgram executed successfully\n\n");
    return 0;
}