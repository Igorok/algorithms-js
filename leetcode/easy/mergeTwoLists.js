/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    if (!list1 && !list2) return;

    let head;
    if (list1.val < list2.val) {
        head = list1;
        list1 = list1.next;
    } else {
        head = list2;
        list2 = list2.next;
    }

    let curr = head;

    while (list1.next && list2.next) {
        if (list1.val < list2.val) {
            curr.next = list1;
            list1 = list1.next;
        } else {
            curr.next = list2;
            list2 = list2.next;
        }
        curr = curr.next;
    }

    while (list1.next) {
        curr.next = list1;
        list1 = list1.next;
        curr = curr.next;
    }

    while (list2.next) {
        curr.next = list2;
        list2 = list2.next;
        curr = curr.next;
    }

    curr.next = undefined;

    return head;
};
