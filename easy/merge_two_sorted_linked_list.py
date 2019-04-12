class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        merged_list = list1 + list2
        merged_list = sorted(merged_list)
        result = self.list_to_link(merged_list)
        return result

    @staticmethod
    def list_to_link(source_list):
        head = None
        point = None
        for item in source_list:
            if not head:
                head = ListNode(item)
                point = head
            else:
                n = ListNode(item)
                point.next = n
                point = n

        return head


if __name__ == '__main__':
    solution = Solution()
    l1 = solution.list_to_link([1, 2, 4])
    l2 = solution.list_to_link([1, 3, 4])
    ml = solution.mergeTwoLists(l1, l2)
    while ml:
        print(ml.val,)
        ml = ml.next
