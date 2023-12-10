#include <iostream>
#include <windows.h>

using namespace std;

bool IsDebugged(DWORD64 qwNativeElapsed) // milisaniye
{
    LARGE_INTEGER liStart, liEnd;
    QueryPerformanceCounter(&liStart);
    // ... 
    QueryPerformanceCounter(&liEnd);
    return (liEnd.QuadPart - liStart.QuadPart) > qwNativeElapsed;
}

int main()
{
    if (IsDebugged(1000)) {
        cout << "Debugger detected!" << endl;
    }
}
