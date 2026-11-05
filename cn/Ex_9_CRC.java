import java.io.*;

public class Ex_9_CRC {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter Generator: ");
        String gen = br.readLine();

        System.out.print("Enter Data: ");
        String data = br.readLine();

        // Append (generator length - 1) zeros to data payload
        String code = data + "0".repeat(gen.length() - 1);

        // Transmitted codeword = Data + Remainder
        code = data + div(code, gen);
        System.out.println("The transmitted Code Word is: " + code);

        System.out.print("Enter the received Code Word: ");
        String rec = br.readLine();

        // Check if remainder of received codeword is all zeros
        if (Integer.parseInt(div(rec, gen)) == 0) {
            System.out.println("The received codeword contains no errors.");
        } else {
            System.out.println("The received codeword contains errors.");
        }
    }

    static String div(String a, String b) {
        int n = b.length();
        String rem = a.substring(0, n);
        int p = n;

        while (true) {
            // XOR with generator if leading bit is 1, else XOR with zeros
            rem = xor(rem, rem.charAt(0) == '1' ? b : "0".repeat(n));
            
            // Shift left by dropping the processed MSB
            rem = rem.substring(1);

            // Pull the next bit from dividend payload if available
            if (p < a.length()) {
                rem += a.charAt(p++);
            } else {
                break;
            }
        }
        return rem;
    }

    static String xor(String a, String b) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            res.append(a.charAt(i) == b.charAt(i) ? '0' : '1');
        }
        return res.toString();
    }
}
