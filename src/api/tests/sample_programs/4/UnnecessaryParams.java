public class UnnecessaryParams {
    public void addNode(ListNode node) {}

    // NO VIOLATION: This method is not in the spec
    private ListNode addNode(ListNode node, ListNode root) {
        return new ListNode();
    }

    // VIOLATION: Unnecessary param "myParam"
    public void test1(String myParam) {}
}
