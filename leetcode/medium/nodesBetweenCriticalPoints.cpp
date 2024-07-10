using std::vector;
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
    bool isCritical (ListNode* prev, ListNode* head) {
        if (!head->next) return false;

        if (prev->val < head->val && head->next->val < head->val)
            return true;

        if (prev->val > head->val && head->next->val > head->val)
            return true;

        return false;
    }
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        if (!head || !head->next || !head->next->next)
            return vector<int> {-1, -1};

        ListNode* prev = head;
        head = head->next;
        int firstCriticalId = -1;
        int prevCriticalId = -1;
        int id = 2;
        int criticalCount = 0;
        vector<int> result = {(int)10e6, -1};

        while (head) {
            if (this->isCritical(prev, head)) {
                if (firstCriticalId == -1) {
                    firstCriticalId = id;
                } else {
                    result[0] = std::min(result[0], id - prevCriticalId);
                    result[1] = std::max(result[1], id - firstCriticalId);
                }
                criticalCount += 1;
                prevCriticalId = id;
            }

            id += 1;
            prev = head;
            head = head->next;
        }

        if (criticalCount < 2)
            return vector<int> {-1, -1};

        return result;
    }
};
