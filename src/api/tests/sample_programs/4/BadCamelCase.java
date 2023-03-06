public class BadCamelCase {
    public int ThisNotCamel;

    public BadCamelCase() {
        ThisNotCamel = 3;
        int this_should_be_camel_case = 2;
    }

    public void ThisNeedsToBeCamelCase() {
        int test2 = 3;
    }
}
