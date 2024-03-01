#include <iostream>
#include <Windows.h>
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

int main() {

    __try {
        int a = 5, b = 9, c = 10;
        int sum = a + b;
        SetErrorMode(140);

        if ((sum * c) % SetErrorMode(10)) {
            cout << "CONNECTING..." << endl;
            confuseFunc();
        }
        else {
            int* p = nullptr;
            *p = 42;
            TerminateProcess(GetCurrentProcess(), 0);
        }

    }
    __except (EXCEPTION_EXECUTE_HANDLER) {
        __asm {
            _emit 0ebH
            _emit 0ffH
            _emit 0c0H
        }
        maliciousFunc();
    }


    return 0;
}
