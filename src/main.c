/*
Keep windows screen on while this program is running
https://docs.microsoft.com/en-us/windows/desktop/api/winbase/nf-winbase-setthreadexecutionstate
Joachim Banzhaf, GPL V2, 2019
*/

#include <stdio.h>
#include <windows.h>

int main()
{
    SetThreadExecutionState(ES_CONTINUOUS|ES_DISPLAY_REQUIRED);
    puts("\n  Presenting. Press Enter when done.");
    getchar();
    return 0;
}
