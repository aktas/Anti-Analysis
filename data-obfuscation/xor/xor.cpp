#include <iostream>
#include <string>

using namespace std;

string xorEncrypt(string key, string message) {
    string ciphertext = "";
    for (int i = 0; i < message.length(); i++)
    {
        ciphertext += message[i] ^ key[i % key.length()];
    }
    return ciphertext;
}

string xorDecrypt(string key, string message) {
    string res = "";
    for (int i = 0; i < message.length(); i++)
    {
        res += message[i] ^ key[i % key.length()];
    }
    return res;
}

int main()
{
    string key = "rivrivriv"; 
    string message = "Ah nerede Vah nerede!";

    string ciphertext = xorEncrypt(key, message);
    cout << ciphertext << endl;

    string res = xorDecrypt(key, ciphertext);
    cout << res << endl;

    return 0;
}
