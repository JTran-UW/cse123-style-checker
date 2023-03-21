public class FieldsNotPrivate {
    private Map<String, Integer> test;
    public static final String THIS_WORKS = 3;

    // VIOLATION: Not in spec
    public String notInSpec;

    public FieldsNotPrivate() {
        String test1 = 3; // NO VIOLATION: Not a class field
    }

    public static class ListNode {
        // NO VIOLATION: Is an exception class
        public ListNode right;
        
        // VIOLATION: Should be public
        private ListNode left;
    }
}
