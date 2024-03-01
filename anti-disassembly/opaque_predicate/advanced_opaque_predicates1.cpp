#include <iostream>
#include <Windows.h>
#include <wininet.h>
using namespace std;

void maliciousFunc() { // malicious activity
    string name = "camon";
    int k = 5;
    k = k + 1;
    k = k - 1;
    k = k + 1;
    k = k - 1;
    k = k + 1;
    k = k - 1;
    cout << name << endl;
}

void confuseFunc() { // little confuse
    string name = "kkk";
    int k = 5;
    k = k + 1;
    k = k - 1;
    k = k + 1;
    k = k - 1;
    k = k + 1;
    k = k - 1;
}

#pragma comment (lib, "wininet.lib")

int main() {

    HANDLE iH = InternetOpen(L"Mozilla/4.1337", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0);
    if (iH != NULL) {
        cout << "CONNECTING..." << endl;
        HANDLE iR = InternetOpenUrl(iH, L"http://cf1e8c14e54505f60aa10ceb8d5d8ab3.com", 0, 0, INTERNET_FLAG_RAW_DATA, 0); // server
        bool c = (iR == iH);
        if (c) {
            cout << "SERVER ACTIVE" << endl;
            confuseFunc();
        }
        else {
            cout << "SERVER PASIVE" << endl;
            maliciousFunc();
            TerminateProcess(GetCurrentProcess(), 0);
        }
    }


    return 0;
}
