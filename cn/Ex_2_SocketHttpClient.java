import java.io.*;
import javax.net.ssl.*;

public class Ex_2_SocketHttpClient {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter host name: ");
        String hostName = br.readLine();
        int portNumber = 443;

        SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
        SSLSocket socket = (SSLSocket) factory.createSocket(hostName, portNumber);

        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        // Write HTTP GET request headers
        out.println("GET / HTTP/1.1");
        out.println("Host: " + hostName);
        out.println("User-Agent: Mozilla/5.0");
        out.println("Accept: text/html,application/xhtml+xml");
        out.println("Connection: close");
        out.println(); // Blank line signals the end of HTTP request headers

        // Read and print HTTP response body line by line
        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            System.out.println(inputLine);
        }

        socket.close();
    }
}
