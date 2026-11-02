import javax.swing.*;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Random;

public class Ex1a_DES {
    static byte[] raw;

    public Ex1a_DES() {
        try {
            // Generate symmetric key
            generatesymmetrickey();

            // Read input message via GUI dialog
            String inputmessage = JOptionPane.showInputDialog(null, "Enter message to Encrypt:");
            if (inputmessage == null) return;

            byte[] ibyte = inputmessage.getBytes();

            // Encrypt plaintext
            byte[] ebyte = encrypt(raw, ibyte);
            String encrypteddata = Base64.getEncoder().encodeToString(ebyte);
            System.out.println("Encrypted Message: " + encrypteddata);
            JOptionPane.showMessageDialog(null, "Encrypted Data:\n" + encrypteddata);

            // Decrypt ciphertext
            byte[] dbyte = decrypt(raw, ebyte);
            String decryptedmessage = new String(dbyte);
            System.out.println("Decrypted Message: " + decryptedmessage);
            JOptionPane.showMessageDialog(null, "Decrypted Data:\n" + decryptedmessage);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    void generatesymmetrickey() {
        try {
            Random r = new Random();
            int num = r.nextInt(1000);
            byte[] knumb = String.valueOf(num).getBytes();

            raw = getRawKey(knumb);
            String sKeyString = Base64.getEncoder().encodeToString(raw);
            System.out.println("DES Symmetric Key = " + sKeyString);
        } catch (Exception e) {
            System.out.println("Key Generation Error: " + e.getMessage());
        }
    }

    private static byte[] getRawKey(byte[] seed) throws Exception {
        KeyGenerator kgen = KeyGenerator.getInstance("DES");
        SecureRandom sr = SecureRandom.getInstance("SHA1PRNG");
        sr.setSeed(seed);
        kgen.init(56, sr);
        SecretKey skey = kgen.generateKey();
        return skey.getEncoded();
    }

    private static byte[] encrypt(byte[] raw, byte[] clear) throws Exception {
        SecretKey seckey = new SecretKeySpec(raw, "DES");
        Cipher cipher = Cipher.getInstance("DES");
        cipher.init(Cipher.ENCRYPT_MODE, seckey);
        return cipher.doFinal(clear);
    }

    private static byte[] decrypt(byte[] raw, byte[] encrypted) throws Exception {
        SecretKey seckey = new SecretKeySpec(raw, "DES");
        Cipher cipher = Cipher.getInstance("DES");
        cipher.init(Cipher.DECRYPT_MODE, seckey);
        return cipher.doFinal(encrypted);
    }

    public static void main(String[] args) {
        new Ex1a_DES();
    }
}
