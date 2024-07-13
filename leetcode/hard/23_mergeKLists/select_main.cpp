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
vector<ListNode*> getMinList (vector<ListNode*>& lists) {
    ListNode* start = nullptr;
    ListNode* end = nullptr;
    int minVal = 10e5;

    for (int i = 0; i < lists.size(); ++i) {
        if (lists[i] && lists[i]->val < minVal) {
            minVal = lists[i]->val;
        }
    }

    for (int i = 0; i < lists.size(); ++i) {
        while (lists[i] && lists[i]->val == minVal) {
            if (!start) {
                start = lists[i];
                end = lists[i];
            } else {
                end->next = lists[i];
                end = end->next;
            }
            lists[i] = lists[i]->next;
        }
    }

    if (end)
        end->next = nullptr;

    return vector<ListNode*>{start, end};
}

public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) return nullptr;

        ListNode* start = nullptr;
        ListNode* end = nullptr;

        while (true) {
            vector<ListNode*> part = this->getMinList(lists);
            if (!part[0]) break;

            if (!start) {
                start = part[0];
                end = part[1];
            } else {
                end->next=part[0];
                end = part[1];
            }
        }

        return start;
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
