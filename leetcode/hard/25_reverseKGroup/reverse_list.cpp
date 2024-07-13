#include<iostream>
#include<vector>

using std::vector;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {

public:
    /*

    1 2 3 4 5 6
    6 5 4 3 2 1

    1
    2
    2 1
    3
    3 2 1

    */
    ListNode* reverseList(ListNode* head) {
        ListNode* node = head;
        head = head->next;
        node->next = nullptr;

        while (head) {
            ListNode* next = head->next;
            head->next = node;
            node = head;
            head = next;
        }

        return node;
    }
};

void test () {
    ListNode* head = new ListNode(0);
    ListNode* node = head;
    for (int i = 1; i <= 10; ++i) {
        node->next = new ListNode(i);
        node = node->next;
    }

    Solution* s = new Solution();
    ListNode* reversed = s->reverseList(head);

    while (reversed) {
        std::cout<< reversed->val << "\n";
        reversed = reversed->next;
    }



}

int main () {

    test();

    return 0;
}
