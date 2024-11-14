import java.util.HashSet;

public class Task2 {
    public static void main(String[] args) {

        // Example 1
        String inputString1 = "a@b!!b$a";
        String trashSymbolString1 = "!@$";

        System.out.println(isPalindrome(inputString1, trashSymbolString1));

        // Example 2
        String inputString2 = "?Aa#c";
        String trashSymbolString2 = "#?";

        System.out.println(isPalindrome(inputString2, trashSymbolString2));

    }

    public static Boolean isPalindrome(String inputString, String garbageString) {

        int n = inputString.length();

        if (n == 0 || n == 1) {
            return true;
        }

        // Create HashSet
        HashSet<Character> trashHash = new HashSet<>();

        for (char c : garbageString.toCharArray()) {
            trashHash.add(c);
        }

        // Pointers
        int left = 0;
        int right = n - 1;

        while (left < right) {

            while (left < right && trashHash.contains(inputString.charAt(left))) {
                left++;
            }

            while (left < right && trashHash.contains(inputString.charAt(right))) {
                right--;
            }

            System.out.println("Comparing " + Character.toLowerCase(inputString.charAt(left)) + " with "
                    + Character.toLowerCase(inputString.charAt(right)));

            if (Character.toLowerCase(inputString.charAt(left)) != Character.toLowerCase(inputString.charAt(right))) {
                return false;
            }

            left++;
            right--;

        }

        return true;

    }
}
