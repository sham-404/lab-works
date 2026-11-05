import java.net.*;
import java.util.*;

public class Ex_6A_ARPServer {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket(9999);
        Map<String, String> arp = new HashMap<>();
        arp.put("192.168.1.1", "AA:BB:CC:DD:EE:01");
        arp.put("192.168.1.2", "AA:BB:CC:DD:EE:02");
        arp.put("192.168.1.3", "AA:BB:CC:DD:EE:03");

        System.out.println("ARP Server running...");
        while (true) {
            byte[] buffer = new byte[1024];
            DatagramPacket receive = new DatagramPacket(buffer, buffer.length);
            socket.receive(receive); // Receive IP request

            String ip = new String(receive.getData(), 0, receive.getLength());
            System.out.println("Request for IP: " + ip);

            String mac = arp.get(ip);
            if (mac == null) {
                System.out.println("IP not found. Broadcasting request...");
                mac = generateMAC();
                arp.put(ip, mac);
            }

            byte[] data = mac.getBytes();
            DatagramPacket send = new DatagramPacket(
                data, data.length, receive.getAddress(), receive.getPort()
            );
            socket.send(send); // Send MAC reply
        }
    }

    static String generateMAC() {
        Random r = new Random();
        String mac = "";
        for (int i = 0; i < 6; i++) {
            mac += String.format("%02X", r.nextInt(256));
            if (i < 5) mac += ":";
        }
        return mac;
    }
}
