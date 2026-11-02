import java.io.*;
import java.math.BigInteger;

public class Ex2b_DH {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Publicly shared values: prime modulus (p) and primitive root (g)
        System.out.print("Enter Prime Number: ");
        BigInteger p = new BigInteger(br.readLine());

        System.out.print("Enter Primitive root of " + p + ": ");
        BigInteger g = new BigInteger(br.readLine());

        // Sender's private key (x) and public calculation (R1)
        System.out.print("Enter value for x less than " + p + ": ");
        BigInteger x = new BigInteger(br.readLine());
        BigInteger R1 = g.modPow(x, p);
        System.out.println("R1 = " + R1);

        // Receiver's private key (y) and public calculation (R2)
        System.out.print("Enter value for y less than " + p + ": ");
        BigInteger y = new BigInteger(br.readLine());
        BigInteger R2 = g.modPow(y, p);
        System.out.println("R2 = " + R2);

        // Symmetric Shared Key computation
        BigInteger K1 = R2.modPow(x, p); // Sender side: K1 = R2^x mod p
        System.out.println("Key Calculated at Sender's Side: " + K1);

        BigInteger K2 = R1.modPow(y, p); // Receiver side: K2 = R1^y mod p
        System.out.println("Key Calculated at Receiver's Side: " + K2);

        System.out.println("Diffie-Hellman Secret Key Was Calculated Successfully.");
    }
}
