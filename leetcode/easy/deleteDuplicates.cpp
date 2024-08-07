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
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return head;

        ListNode* node = head;
        ListNode* curr = node;

        while (curr) {
            if (!curr->next) {
                curr = curr->next;
                continue;
            }
            if (curr->val == curr->next->val) {
                curr->next = curr->next->next;
                continue;
            }
            curr = curr->next;
        }

        return node;
    }
};
