/*
Task 1925. Count Square Sum Triples

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
*/

#include <cmath>
#include <numeric>
class Solution {
public:
    int countTriples(int n) {
        int res = 0;
        for (int u = 2; u <= sqrt(n); u++) {
            for (int v = 1; v < u; v++) {
                if (~(u - v) & 1 || gcd(u, v) != 1) continue;
                int c = u * u + v * v;
                if (c > n) continue;
                res += (n / c) << 1;
            }
        }
        return res;
    }
};