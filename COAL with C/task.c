#include<stdio.h>


// int max_of_three(int a, int b, int c) {
//     int max = a;
//     if (b > max)
//         max = b;
//     if (c > max)
//         max = c;
//     return max;
// }
// int is_even(int n) {
//     return n % 2 == 0;
// }

// int reverse_number(int n) {
//     int reversed = 0;
//     while (n != 0) {
//         reversed = reversed * 10 + n % 10;
//         n /= 10;
//     }
//     return reversed;
// }
// int factorial(int n) {
//     int result = 1;
//     for (int i = 2; i <= n; i++) {
//         result *= i;
//     }
//     return result;
// }
// int fibonacci(int n) {
//     if (n <= 0)
//         return 0;
//     int a = 0, b = 1, next;
//     for (int i = 2; i <= n; i++) {
//         next = a + b;
//         a = b;
//         b = next;
//     }
//     return b;
// }
int sum_of_digits(int n) {
    int sum = 0;
    while (n != 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}
int is_palindrome(int n) {
    int original = n;
    int reversed = 0;
    while (n != 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return original == reversed;
}
