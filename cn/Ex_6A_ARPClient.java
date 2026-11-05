import java.net.*;
import java.util.Scanner;

public class Ex_6A_ARPClient {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket();
        InetAddress server = InetAddress.getByName("localhost");
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.print("Enter IP Address (or exit): ");
            String ip = sc.nextLine();
            if (ip.equalsIgnoreCase("exit")) break;

            byte[] data = ip.getBytes();
            DatagramPacket send = new DatagramPacket(data, data.length, server, 9999);
            socket.send(send);

            byte[] buffer = new byte[1024];
            DatagramPacket receive = new DatagramPacket(buffer, buffer.length);
            socket.receive(receive);

            String mac = new String(receive.getData(), 0, receive.getLength());
            System.out.println("MAC Address for " + ip + ": " + mac);
        }

        socket.close();
        sc.close();
    }
}
