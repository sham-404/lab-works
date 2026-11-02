import java.math.BigInteger;

public class Ex3_DSA {
    public static void main(String[] args) {
        // Public domain parameters
        BigInteger p = new BigInteger("23");
        BigInteger q = new BigInteger("11");
        BigInteger g = new BigInteger("2");

        // Private Key (x) and Public Key (y = g^x mod p)
        BigInteger x = new BigInteger("3");
        BigInteger y = g.modPow(x, p);

        // Pre-computed Message Hash and Per-message Secret Key (k)
        BigInteger hash = new BigInteger("5");
        BigInteger k = new BigInteger("4");

        // --- Signature Generation ---
        // r = (g^k mod p) mod q
        BigInteger r = g.modPow(k, p).mod(q);
        
        // s = [k^-1 * (hash + x * r)] mod q
        BigInteger s = k.modInverse(q).multiply(hash.add(x.multiply(r))).mod(q);

        System.out.println("Digital Signature Algorithm");
        System.out.println("\nPublic Key:");
        System.out.println("p = " + p);
        System.out.println("q = " + q);
        System.out.println("g = " + g);
        System.out.println("y = " + y);

        System.out.println("\nPrivate Key:");
        System.out.println("x = " + x);

        System.out.println("\nDigital Signature:");
        System.out.println("r = " + r);
        System.out.println("s = " + s);

        // --- Signature Verification ---
        // w = s^-1 mod q
        BigInteger w = s.modInverse(q);
        
        // u1 = (hash * w) mod q
        BigInteger u1 = hash.multiply(w).mod(q);
        
        // u2 = (r * w) mod q
        BigInteger u2 = r.multiply(w).mod(q);
        
        // v = [(g^u1 * y^u2) mod p] mod q
        BigInteger v = g.modPow(u1, p).multiply(y.modPow(u2, p)).mod(p).mod(q);

        System.out.println("\nVerification:");
        System.out.println("v = " + v);

        if (v.equals(r)) {
            System.out.println("Digital Signature Verified Successfully");
        } else {
            System.out.println("Digital Signature Verification Failed");
        }
    }
}
