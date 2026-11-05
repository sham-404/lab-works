import java.net.*;
import java.util.Scanner;

public class Ex_4_DNSClient {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket(); // Unbound client socket
        InetAddress server = InetAddress.getByName("localhost");
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Domain name: ");
        String domain = sc.nextLine();

        byte[] data = domain.getBytes();
        DatagramPacket send = new DatagramPacket(data, data.length, server, 9876);
        socket.send(send);

        byte[] buffer = new byte[1024];
        DatagramPacket receive = new DatagramPacket(buffer, buffer.length);
        socket.receive(receive); // Blocks until server replies

        String response = new String(receive.getData(), 0, receive.getLength());
        System.out.println("IP Address: " + response);

        socket.close();
        sc.close();
    }
}
