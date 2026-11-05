import java.io.*;
import java.net.*;


public class Ex_3B_ChatServer {
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(6666);
        Socket clientSocket = serverSocket.accept();

        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            System.out.print("Server: ");
            String inputLine = stdIn.readLine();
            out.println(inputLine);
            if ("END".equalsIgnoreCase(inputLine)) break;

            inputLine = in.readLine();
            if (inputLine == null) break;
            System.out.println("Client: " + inputLine);
        }

        clientSocket.close();
        serverSocket.close();
    }
}
