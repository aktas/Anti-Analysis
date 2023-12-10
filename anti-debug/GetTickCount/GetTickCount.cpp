#include <iostream>
#include <windows.h>

using namespace std;
bool IsDebuggedd(DWORD dwNativeElapsed) // milisaniye
{
    DWORD dwStart = GetTickCount();
    // ... 
    return (GetTickCount() - dwStart) > dwNativeElapsed;
}

int main()
{
    if (IsDebuggedd(1000)) {
        cout << "Debugger Detected!" << endl;
    } // Fonksiyon, GetTickCount() işlevini kullanarak işlem başlangıcı ve bitişi arasındaki süreyi ölçer.
}
