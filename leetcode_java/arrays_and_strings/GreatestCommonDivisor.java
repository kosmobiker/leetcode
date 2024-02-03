/*
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that 
x divides both str1 and str2.
 */
class Solution {
    //Euclid’s algorithm to find the GCD (Greatest common divisor).
    private int gcdByEuclidsAlgorithm(int n1, int n2) {
        if (n2 == 0) {
            return n1;
        }
        return gcdByEuclidsAlgorithm(n2, n1 % n2);
    }
    //Find the GDC of two strings
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
    int gcdLength = gcdByEuclidsAlgorithm(str1.length(), str2.length());
        return str1.substring(0, gcdLength);
    }
}