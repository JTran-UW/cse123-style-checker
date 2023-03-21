public class NonSpecMethodNotPrivate {
    // VIOLATION: Should be private
    public String test2() {
        return "test";
    }
}
