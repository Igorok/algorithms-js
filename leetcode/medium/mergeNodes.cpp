/*
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]

Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]

*/


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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* node = head;
        ListNode* tmp = node;
        head = head->next;

        while (head) {
            if (head->val != 0) {
                tmp->val += head->val;
            }
            if (head->val == 0 && head->next) {
                tmp->next = head;
                tmp = tmp->next;
            }

            head =  head->next;
        }

        return node;
    }
};
