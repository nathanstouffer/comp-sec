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
    BIGNUM* m1 = BN_new();
    BIGNUM* m2 = BN_new();
    BIGNUM* s1 = BN_new();
    BIGNUM* s2 = BN_new();    

    // init p, q, and e
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
    BN_hex2bn(&m1, "49206f776520796f752024323030302e");
    BN_hex2bn(&m2, "49206f776520796f752024333030302e");

    print_BN("n: ", n);
    print_BN("e: ", e);
    print_BN("d: ", d);
    print_BN("I owe you $2000.: ", m1);
    print_BN("I owe you $3000.: ", m2);

    BN_mod_exp(s1, m1, d, n, ctx);
    print_BN("\ns1 (m1^d mod n):", s1);

    BN_mod_exp(s2, m2, d, n, ctx);
    print_BN("s2 (m2^d mod n):", s2);
    
    return 0;
}
