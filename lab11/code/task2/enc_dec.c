// find_private_key.c

#include <stdio.h>
#include <openssl/bn.h>

void print_BN(char* msg, BIGNUM* a) {
    //char* number_str = BN_bn2dec(a);
    char* number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main() {
    BN_CTX* ctx = BN_CTX_new();
    BIGNUM* n = BN_new();
    BIGNUM* e = BN_new();  
    BIGNUM* d = BN_new();
    BIGNUM* m = BN_new();
    BIGNUM* enc = BN_new();
    BIGNUM* dec = BN_new();

    // init p, q, and e
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
    BN_hex2bn(&m, "4120746f702073656372657421");

    print_BN("n: ", n);
    print_BN("e: ", e);
    print_BN("d: ", d);
    print_BN("m: ", m);

    BN_mod_exp(enc, m, e, n, ctx);
    print_BN("\nenc (m^e mod n): ", enc);

    BN_mod_exp(dec, enc, d, n, ctx);
    print_BN("\ndec (enc^d mod n):", dec);

    return 0;
}
