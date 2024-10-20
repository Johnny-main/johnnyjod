import java.util.Scanner;

public class cc {

    // Method to encrypt the message
    public static String encrypt(String text, int shift) {
        StringBuilder result = new StringBuilder();
        
        // Convert the input to uppercase
        text = text.toUpperCase();

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);

            // Encrypt letters and handle wrap-around using modulo 26
            if (Character.isLetter(c)) {
                // char ch = (char)(((int)c + shift - 65) % 26 + 65); 

                int asciiValue = (int) c;  // Step 1: Get ASCII value of the character
                int base = 65;             // Step 2: Base value for 'A' is 65 (uppercase letters)

                int shiftedValue = asciiValue - base;  // Step 3: Convert ASCII to 0-based alphabet index
                shiftedValue += shift;                 // Step 4: Add the shift value
                shiftedValue = shiftedValue % 26;      // Step 5: Modulo 26 to handle wrap-around

                int newAscii = shiftedValue + base;    // Step 6: Convert back to ASCII value (add base)
                char newChar = (char) newAscii;        // Step 7: Convert ASCII value to character

                result.append(newChar);                // Append the encrypted character to the result
            }
            // For other characters (like spaces), just append them as is
            else {
                result.append(c);
            }
        }
        
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter a message: ");
        String text = sc.nextLine();
        
        System.out.print("Enter shift value: ");
        int shift = sc.nextInt();
        
        String encryptedMessage = encrypt(text, shift);
        System.out.println("Encrypted message: " + encryptedMessage);
        
        sc.close();
    }
}
