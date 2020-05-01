// dec.c

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
    BIGNUM* s = BN_new();
    BIGNUM* m = BN_new();

    // init p, q, and e
    BN_hex2bn(&n, "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&s, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F");

    print_BN("n: ", n);
    print_BN("e: ", e);
    print_BN("s: ", s);

    BN_mod_exp(m, s, e, n, ctx);
    print_BN("\nm (s^e mod n):", m);

    return 0;
}
