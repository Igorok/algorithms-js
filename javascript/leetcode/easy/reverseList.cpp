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
    ListNode* reverseList_(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* first = new ListNode(head->val);
        head = head->next;

        while (head) {
            ListNode* curr = new ListNode(head->val, first);
            first = curr;
            head = head->next;
        }

        return first;
    }

    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* prev = nullptr;

        while (head) {
            ListNode* tmp = head->next;
            head->next = prev;
            prev = head;
            head = tmp;
        }

        return prev;
    }
};


/*


1 - 2 - 3 - 4 - 5 - 6 - 7 - 8

0 - 1 - 2 - 3 - 4


*/
