public class BadLoopStatement {
    public static void main(String[] args) {
        // 4 violations: no space after 'for', before '=', after ';'
        // and there should be no space before ')''
        for(int i= 0;i < 10; i++ ) {
            System.out.println(i);
        }

        // 2 violations: no space after 'while', no space after '=='
        while(3 ==5) {
            System.out.println();
        }

        // 2 violations: no space before and after ":"
        for (String s: list) {
            System.out.println();
        }
    }
}