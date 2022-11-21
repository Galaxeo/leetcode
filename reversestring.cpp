class Solution {
public:
    void reverseString(vector<char>& s) {
        int start = 0;
        int end = s.size()-1;
        while (start-end<=0) {
            swap(s[start], s[end]);
            start+=1;
            end-=1;
        }
    }
private:
    void swap(char& a, char& b) {
        char dum = a;
        a = b;
        b = dum;
    }
};