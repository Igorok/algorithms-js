#include<iostream>
#include<vector>
#include<algorithm>

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

ListNode* mergeList(ListNode* l1, ListNode* l2) {
    if (!l2)
        return l1;

    ListNode* start = nullptr;
    ListNode* end = nullptr;

    if (l1->val <= l2->val) {
        start = l1;
        end = l1;
        l1 = l1->next;
    } else {
        start = l2;
        end = l2;
        l2 = l2->next;
    }

    while (l1 && l2) {
        if (l1->val <= l2->val) {
            end->next = l1;
            end = end->next;
            l1 = l1->next;
        } else {
            end->next = l2;
            end = end->next;
            l2 = l2->next;
        }
    }

    while (l1) {
        end->next = l1;
        end = end->next;
        l1 = l1->next;
    }

    while (l2) {
        end->next = l2;
        end = end->next;
        l2 = l2->next;
    }

    end->next = nullptr;

    return start;
}

public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) return nullptr;
        if (lists.size() == 1) return lists[0];

        vector<ListNode*> mergedList;

        int i = 0;
        while (i < lists.size()) {
            ListNode* l1 = lists[i];
            ListNode* l2 = (i + 1 < lists.size()) ? lists[i + 1] : nullptr;

            ListNode* merged = this->mergeList(l1, l2);
            mergedList.push_back(merged);

            i+= 2;
        }

        return this->mergeKLists(mergedList);
    }
};

/*
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
*/


void test () {
    vector<int> v1 = {4,5};
    vector<int> v2 = {3,4};
    vector<int> v3 = {6};


    ListNode* head1 = new ListNode(1);
    ListNode* node1 = head1;
    for (int i = 0; i < v1.size(); ++i) {
        node1->next = new ListNode(v1[i]);
        node1= node1->next;
    }

    ListNode* head2 = new ListNode(1);
    ListNode* node2 = head2;
    for (int i = 0; i < v2.size(); ++i) {
        node2->next = new ListNode(v2[i]);
        node2= node2->next;
    }

    ListNode* head3 = new ListNode(2);
    ListNode* node3 = node3;
    for (int i = 0; i < v3.size(); ++i) {
        node3->next = new ListNode(v2[i]);
        node3= node3->next;
    }

    vector<ListNode*> myVec {head1, head2, head3};

    Solution* s = new Solution();
    ListNode* newHead = s->mergeKLists(myVec);

    std::cout<< "newHead" << "\n";
    while (newHead) {
        std::cout<< newHead->val << "\n";
        newHead = newHead->next;
    }
}




int main () {
    test();

    return 0;
};
