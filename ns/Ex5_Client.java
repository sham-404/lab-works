import javax.net.ssl.*;
import java.io.*;

class Ex5_Client {
    public static void main(String[] args) throws Exception {
        // Set SSL trustStore properties (trusting server's KeyStore)
        System.setProperty("javax.net.ssl.trustStore", "samlKeystore.jks");
        System.setProperty("javax.net.ssl.trustStorePassword", "password");

        // Create SSL socket connection to localhost:9999
        SSLSocketFactory sf = (SSLSocketFactory) SSLSocketFactory.getDefault();
        SSLSocket socket = (SSLSocket) sf.createSocket("localhost", 9999);

        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        // Send encrypted string to server
        out.println("Hello from client");

        // Read encrypted response from server
        String response = in.readLine();
        System.out.println("Server response: " + response);

        socket.close();
    }
}
