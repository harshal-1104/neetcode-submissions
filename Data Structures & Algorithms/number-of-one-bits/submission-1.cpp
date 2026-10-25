class Solution {
public:
    int hammingWeight(uint32_t n) {
        int counter = 0, mask = 1;
        for(int i=0;i<32;i++) {
            if (n & (mask << i)) {
                ++counter;
            }
        }
        return counter;
    }
};
