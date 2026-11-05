import java.io.*;
import java.net.*;

public class Ex_3A_EchoClient {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket("127.0.0.1", 6666);
        BufferedReader serverIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter serverOut = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader userIn = new BufferedReader(new InputStreamReader(System.in));

        System.out.println(serverIn.readLine()); // Read welcome message

        String line;
        do {
            line = userIn.readLine();
            if (line != null) {
                serverOut.println(line);
                if (!line.trim().equalsIgnoreCase("bye")) {
                    System.out.println(serverIn.readLine()); // Read echoed response
                }
            }
        } while (line != null && !line.trim().equalsIgnoreCase("bye"));

        socket.close();
    }
}
