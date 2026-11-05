import java.io.*;
import java.net.*;

public class Ex_3A_EchoServer {
    public static void main(String[] args) throws Exception {
        ServerSocket server = new ServerSocket(6666);
        System.out.println("Echo server started on port 6666");

        while (true) {
            Socket client = server.accept();
            System.out.println("Client connected.");

            BufferedReader r = new BufferedReader(new InputStreamReader(client.getInputStream()));
            PrintWriter w = new PrintWriter(client.getOutputStream(), true);

            w.println("Welcome to the Java Echo server. Type 'bye' to close");

            String line;
            while ((line = r.readLine()) != null && !line.trim().equalsIgnoreCase("bye")) {
                System.out.println("Client: " + line);
                w.println("Got: " + line);
            }

            client.close();
            System.out.println("Client disconnected");
        }

    }
}
