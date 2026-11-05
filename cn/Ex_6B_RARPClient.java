import java.net.*;
import java.util.Scanner;

public class Ex_6B_RARPClient {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket();
        InetAddress server = InetAddress.getByName("localhost");
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter MAC Address: ");
        String mac = sc.nextLine();

        byte[] data = mac.getBytes();
        DatagramPacket send = new DatagramPacket(data, data.length, server, 5555);
        socket.send(send);

        byte[] buffer = new byte[1024];
        DatagramPacket receive = new DatagramPacket(buffer, buffer.length);
        socket.receive(receive);

        String ip = new String(receive.getData(), 0, receive.getLength());
        System.out.println("IP Address for " + mac + ": " + ip);

        socket.close();
        sc.close();
    }
}
