#include <openssl/bio.h>
#include <openssl/buffer.h>
#include <openssl/evp.h>
#include <iostream>

std::string base64_encode(const std::string& input) {
    BIO* bio, * b64;
    BUF_MEM* bufferPtr;

    b64 = BIO_new(BIO_f_base64());
    bio = BIO_new(BIO_s_mem());
    bio = BIO_push(b64, bio);

    BIO_set_flags(bio, BIO_FLAGS_BASE64_NO_NL);
    BIO_write(bio, input.c_str(), input.length());
    BIO_flush(bio);

    BIO_get_mem_ptr(bio, &bufferPtr);
    BIO_set_close(bio, BIO_NOCLOSE);
    BIO_free_all(bio);

    return std::string(bufferPtr->data, bufferPtr->length);
}

std::string base64_decode(const std::string& input) {
    BIO* bio, * b64;
    char* buffer = new char[input.size()];
    std::copy(input.begin(), input.end(), buffer);

    bio = BIO_new_mem_buf(buffer, input.size());
    b64 = BIO_new(BIO_f_base64());
    bio = BIO_push(b64, bio);

    BIO_set_flags(bio, BIO_FLAGS_BASE64_NO_NL);
    int length = BIO_read(bio, buffer, input.size());
    BIO_free_all(bio);

    return std::string(buffer, length);
}

int main() {
    std::string originalText = "To the King!";
    std::string encodedText = base64_encode(originalText);
    std::string decodedText = base64_decode(encodedText);

    std::cout << "Original: " << originalText << std::endl;
    std::cout << "Encoded : " << encodedText << std::endl;
    std::cout << "Decoded : " << decodedText << std::endl;

    return 0;
}
