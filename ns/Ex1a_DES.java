import javax.swing.*;
import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class Ex1a_DES {

    static byte[] generatesymmetrickey() throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("DES");
        kg.init(56);
        return kg.generateKey().getEncoded();
    }

    static byte[] encrypt(byte[] key, byte[] data) throws Exception {
        Cipher c = Cipher.getInstance("DES");
        c.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(key, "DES"));
        return c.doFinal(data);
    }

    static byte[] decrypt(byte[] key, byte[] data) throws Exception {
        Cipher c = Cipher.getInstance("DES");
        c.init(Cipher.DECRYPT_MODE, new SecretKeySpec(key, "DES"));
        return c.doFinal(data);
    }

    public static void main(String[] args) {
        try {
            byte[] key = generatesymmetrickey();

            System.out.println("DES Symmetric Key = " +
                    Base64.getEncoder().encodeToString(key));

            String msg = JOptionPane.showInputDialog("Enter message to Encrypt:");
            if (msg == null) return;

            byte[] encrypted = encrypt(key, msg.getBytes());
            String enc = Base64.getEncoder().encodeToString(encrypted);

            System.out.println("Encrypted Message: " + enc);
            JOptionPane.showMessageDialog(null, "Encrypted Data:\n" + enc);

            String decrypted = new String(decrypt(key, encrypted));

            System.out.println("Decrypted Message: " + decrypted);
            JOptionPane.showMessageDialog(null, "Decrypted Data:\n" + decrypted);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
