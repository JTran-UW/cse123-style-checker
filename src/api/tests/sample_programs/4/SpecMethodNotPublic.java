public class SpecMethodNotPublic {
    public SpecMethodNotPublic() {}

    // NO VIOLATION: Matches specification
    private Map<String, Integer> test(String param) {}

    // VIOLATION: should be public
    private static String anotherMethod(Map<String, Integer> myParam) {}
}
