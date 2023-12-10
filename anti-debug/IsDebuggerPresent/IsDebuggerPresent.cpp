#include <iostream>
#include <windows.h>

using namespace std;

int main() {

	if (IsDebuggerPresent()) {
		ExitProcess(0);
	}

	// ...

	return 0;
}
