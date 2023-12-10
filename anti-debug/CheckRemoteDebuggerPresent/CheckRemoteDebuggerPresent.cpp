#include <iostream>
#include <windows.h>

using namespace std;

int main() {

	BOOL isDebuggerPresent = false;
	HANDLE hProcess = GetCurrentProcess();
	CheckRemoteDebuggerPresent(hProcess, &isDebuggerPresent);
	if (isDebuggerPresent) {
		ExitProcess(0);
	}

	cout << "Everything's OK" << endl;

	return 0;
}
