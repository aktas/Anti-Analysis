#include <windows.h>
#include <iostream>
using namespace std;

void dynamicApiResolving(const char* str, const char* str2)
{
	string decryptedString;
	string decryptedString2;

	for (int i = 0; i < strlen(str); i++) {
		decryptedString += str[i] ^ 0x11;
	}
	for (int i = 0; i < strlen(str2); i++) {
		decryptedString2 += str2[i] ^ 0x11;
	}

	const char* szMessage = "Hello World!";
	const char* szCaption = "Hello!";
	HMODULE hModule = GetModuleHandleA(decryptedString2.c_str());
	if (!hModule)
		cout << "error" << endl;
	FARPROC fFuncProc = GetProcAddress(hModule, decryptedString.c_str());
	((int (WINAPI*)(HWND, LPCSTR, LPCSTR, UINT)) fFuncProc)(0, szMessage, szCaption, 0);
	FreeLibrary(hModule);
}

string xorFunc(const char* str) {
	string encryptedString;

	for (int i = 0; i < strlen(str); i++) {
		encryptedString += str[i] ^ 0x11;
	}

	return encryptedString;
}

int main()
{
	
	//cout << xorFunc("MessageBoxA") << endl;
	ShowWindow(GetConsoleWindow(), 0);
	if (FreeConsole()) {
		dynamicApiResolving("\\tbbpvtS~iP", "dbtc\"#?u}}"); // api, dll
	}

	return 0;
}
