/*
CODE CHALLENGE: Finding an Element in an Arbitrary Array List

Given an arbitrary Array List of integers arr and an integer n, return true if n appears in arr, or false if it does not.
*/


bool find(vector<int> arr, int n) {
    for (int i = 0; i< arr.size(); ++i) {
        if (arr[i] == n) {
            return true;
        }
    }
    return false;
}

int main () {
    return 0;
}