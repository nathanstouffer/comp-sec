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
    BIGNUM* p = BN_new();  BIGNUM* q = BN_new();
    BIGNUM* e = BN_new();  
    BIGNUM* n = BN_new();
    BIGNUM* p_minus_one = BN_new();
    BIGNUM* q_minus_one = BN_new();
    BIGNUM* d = BN_new();

    // init p, q, and e
    BN_hex2bn(&p, "F7E75FDC469067FFDC4E847C51F452DF");
    BN_hex2bn(&q, "E85CED54AF57E53E092113E62F436F4F");
    BN_hex2bn(&e, "0D88C3");
    BN_sub(p_minus_one, p, BN_value_one());
    BN_sub(q_minus_one, q, BN_value_one());
    BN_mul(n, p_minus_one, q_minus_one, ctx);	// compute n

    print_BN("p: ", p);
    print_BN("q: ", q);
    print_BN("e: ", e);
    print_BN("n: ", n);

    // compute d with library call
    BN_mod_inverse(d, e, n, ctx);
    print_BN("private key: ", d);

    return 0;
}
