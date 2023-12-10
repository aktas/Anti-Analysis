#include <iostream>
#include <windows.h>
#include <vector>

using namespace std;

const vector<string> vWindowClasses = {
  "antidbg",
  "ID", // Immunity Debugger
  "ntdll.dll", 
  "ObsidianGUI",
  "OLLYDBG",
  "Rock Debugger",
  "SunAwtFrame",
  "Qt5QWindowIcon",
  "WinDbgFrameClass",
  "Zeta Debugger",
  "IDA", 
  "X32Dbg",
  "x64dbg",
};

bool IsDebugged()
{
    for (const string& sWndClass : vWindowClasses) {
        const char* pszWndClass = sWndClass.c_str();
        if (NULL != FindWindowA(pszWndClass, NULL)) {
            return true;
        }
    }
    return false;
}

int main() {
    bool isDebuggerDetected = IsDebugged();

    if (isDebuggerDetected) {
        cout << "Debugger detected!\n";
    } // Kod, bu pencere sınıflarının varlığını kontrol ederek debugger'ın varlığını tespit etmeyi amaçlar.

    return 0;
}
