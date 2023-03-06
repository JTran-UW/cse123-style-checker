public class BadCurlyBraceSpacing { private int test;

    public BadCurlyBraceSpacing() { test = 1;
        if (test == 1) {
            test = 2;
        } else {
            test = 3;
        }}
    
    public void testMethod() {
        System.out.println("test");
    } public void testMethod2() {
        System.out.println("test2");
    }
}
