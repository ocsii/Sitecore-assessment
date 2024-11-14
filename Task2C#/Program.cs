public class Task2CSharp
{
    public static void Main(string[] args)
    {
        string inputString1 = "a@b!!b$a";
        string trashSymbolString1 = "!@$";

        Console.WriteLine(IsPalindrome(inputString1, trashSymbolString1));

        string inputString2 = "?Aa#c";
        string trashSymbolString2 = "#?";

        Console.WriteLine(IsPalindrome(inputString2, trashSymbolString2));
    }

    public static bool IsPalindrome(string inputString, string garbageString)
    {
        int n = inputString.Length;

        if (n == 0 || n == 1)
        {
            return true;
        }

        HashSet<char> trashHash = new HashSet<char>();

        foreach (char c in garbageString)
        {
            trashHash.Add(c);
        }

        int left = 0;
        int right = n - 1;

        while (left < right)
        {
            while (left < right && trashHash.Contains(inputString[left]))
            {
                left++;
            }

            while (left < right && trashHash.Contains(inputString[right]))
            {
                right--;
            }

            if (char.ToLower(inputString[left]) != char.ToLower(inputString[right]))
            {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
