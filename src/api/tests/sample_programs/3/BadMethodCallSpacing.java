public class BadMethodCallSpacing {
    public static void main(String[] args) {
        test1(1,2 );
    }

    public static void test1(int p1, int p2) {
        System.out.println(p1 + p2);
    }
}
