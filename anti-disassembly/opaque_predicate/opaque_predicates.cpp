#include <iostream>
#include <Windows.h>
using namespace std;

#pragma optimize("", off)

int main() {

    int x = 3;
    int y = 7;
    int z = x * y;

    if (z == 21) { // always true
        // malicious code   
        cout << "ss" << endl;
    }
    else {
        // some confuse
        cout << "xx" << endl;
    }


    return 0;
}
