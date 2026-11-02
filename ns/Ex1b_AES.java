import java.util.*;
import java.security.MessageDigest;
import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;

public class Ex1b_AES {

    static SecretKeySpec secretKey;

    static void setKey(String myKey) throws Exception {
        byte[] key = MessageDigest.getInstance("SHA-1")
                .digest(myKey.getBytes("UTF-8"));

        key = Arrays.copyOf(key, 16);
        secretKey = new SecretKeySpec(key, "AES");
    }

    static String encrypt(String data, String secret) throws Exception {
        setKey(secret);

        Cipher c = Cipher.getInstance("AES/ECB/PKCS5PADDING");
        c.init(Cipher.ENCRYPT_MODE, secretKey);

        return Base64.getEncoder().encodeToString(
                c.doFinal(data.getBytes("UTF-8")));
    }

    static String decrypt(String data, String secret) throws Exception {
        setKey(secret);

        Cipher c = Cipher.getInstance("AES/ECB/PKCS5PADDING");
        c.init(Cipher.DECRYPT_MODE, secretKey);

        return new String(c.doFinal(Base64.getDecoder().decode(data)), "UTF-8");
    }

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);

            System.out.print("Enter the secret key: ");
            String secret = sc.nextLine();

            System.out.print("Enter the original URL: ");
            String original = sc.nextLine();

            String encrypted = encrypt(original, secret);
            String decrypted = decrypt(encrypted, secret);

            System.out.println("\nURL Encryption using AES Algorithm\n...");
            System.out.println("Original URL: " + original);
            System.out.println("Encrypted URL: " + encrypted);
            System.out.println("Decrypted URL: " + decrypted);

            sc.close();

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
