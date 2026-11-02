
// ------ Command to generate the keystore ------
//
// keytool -genkeypair -keyalg RSA -keysize 2048 -validity 365 -alias myserverkey
// -keystore samlKeystore.jks -storepass password -keypass password -dname
// "CN=localhost, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown"

import javax.net.ssl.*;
import java.io.*;

class Ex5_Server {
    public static void main(String[] args) throws Exception {
        // Set SSL keyStore properties
        System.setProperty("javax.net.ssl.keyStore", "samlKeystore.jks");
        System.setProperty("javax.net.ssl.keyStorePassword", "password");

        // Obtain default SSL socket factory and listen on port 9999
        SSLServerSocketFactory ssf = (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
        SSLServerSocket server = (SSLServerSocket) ssf.createServerSocket(9999);
        System.out.println("Server waiting for client...");

        // Accept client handshake and open secure streams
        SSLSocket socket = (SSLSocket) server.accept();
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        // Read encrypted message from client
        String msg = in.readLine();
        System.out.println("Client message: " + msg);

        // Send encrypted response back to client
        out.println("Message received by server");

        socket.close();
        server.close();
    }
}
