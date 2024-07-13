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
    vector<ListNode*> reverseList(ListNode* head, int k) {
        ListNode* newHead = head;
        head = head->next;
        newHead->next = nullptr;

        ListNode* newEnd = newHead;

        int i = 1;
        while (head && i < k) {
            ListNode* next = head->next;
            head->next = newHead;
            newHead = head;
            head = next;

            i+= 1;
        }

        return vector<ListNode*>{newHead, newEnd};
    }
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;

        ListNode* newHead = nullptr;
        ListNode* middle = nullptr;

        ListNode* node = head;

        int count = 1;
        while (head) {
            head = head->next;
            count += 1;

            if (!head) break;

            if (count == k) {
                ListNode* next = head->next;

                vector<ListNode*> reversed = this-> reverseList(node, k);

                std::cout
                    << "reversed[0] " << reversed[0]->val
                    << "reversed[1] " << reversed[1]->val
                    << "\n";

                if (!newHead) {
                    newHead = reversed[0];
                    middle = reversed[1];
                } else {
                    middle->next = reversed[0];
                    middle = reversed[1];
                }

                node = next;
                head = next;
                count = 1;
            }
        }

        if (count != 0) {
            while (node) {
                middle->next = node;
                middle = middle->next;
                node = node->next;
            }
        }


        return newHead;
    }
};
/*
1 2 3 4 5 6 7 8 9 10
3 2 1

4 5 6 7 8 9 10
3 2 1 6 5 4

*/

void test () {
    ListNode* head = new ListNode(0);
    ListNode* node = head;
    for (int i = 1; i <= 10; ++i) {
        node->next = new ListNode(i);
        node = node->next;
    }
    /*
    while (head) {
        std::cout<< head->val << "\n";
        head = head->next;
    }
    */

    Solution* s = new Solution();
    ListNode* newHead = s->reverseKGroup(head, 3);

    std::cout<< "newHead" << "\n";
    while (newHead) {
        std::cout<< newHead->val << "\n";
        newHead = newHead->next;
    }
}

int main () {

    test();























    return 0;
}
