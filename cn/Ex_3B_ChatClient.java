import java.io.*;
import java.net.*;

public class Ex_3B_ChatClient {
    public static void main(String[] args) throws Exception {
        String hostName = "localhost";
        int portNumber = 6666;

        Socket socket = new Socket(hostName, portNumber);
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            System.out.print("Client: ");
            String userInput = stdIn.readLine();
            out.println(userInput);
            if ("END".equalsIgnoreCase(userInput)) break;

            String serverResponse = in.readLine();
            if (serverResponse == null) break;
            System.out.println("Server: " + serverResponse);
        }

        socket.close();
    }
}
