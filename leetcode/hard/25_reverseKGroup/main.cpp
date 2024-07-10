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
    vector<ListNode*> reverseList(ListNode* start, ListNode* end) {
        ListNode* newEnd = start;
        ListNode* node = start;
        start = start->next;
        node->next = nullptr;

        while (start) {
            ListNode* next = start->next;
            start->next = node;
            node = start;
            start = next;
        }

        return vector<ListNode*>{node, newEnd};
    }
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head) return head;
        if (k == 1) return head;

        ListNode* start = nullptr;
        ListNode* middle = nullptr;
        ListNode* node = head;
        int length = 1;


        while (head) {
            head = head->next;
            length += 1;

            if (!head) break;

            if (length == k) {
                ListNode* next = head->next;
                head->next = nullptr;

                vector<ListNode*> reversed = this->reverseList(node, head);

                if (!start) {
                    start = reversed[0];
                    middle = reversed[1];
                } else {
                    middle->next = reversed[0];
                    middle = reversed[1];
                }

                node = next;
                head = next;
                length = 1;
            }
        }

        if (!start) return head;

        if (length != 1) {
            while (node) {
                middle->next = node;
                middle = middle->next;
                node = node->next;
            }
        }
        return start;
    }
};

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
