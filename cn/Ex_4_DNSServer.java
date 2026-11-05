import java.net.*;

public class Ex_4_DNSServer {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket(9876);
        System.out.println("DNS Server is running...");

        while (true) {
            byte[] buffer = new byte[1024];
            DatagramPacket receive = new DatagramPacket(buffer, buffer.length);
            socket.receive(receive); // Blocks execution until a packet arrives

            String domain = new String(receive.getData(), 0, receive.getLength());
            System.out.println("Request received: " + domain);

            String ip;
            try {
                ip = InetAddress.getByName(domain).getHostAddress();
            } catch (Exception e) {
                ip = "Domain not found";
            }

            byte[] sendData = ip.getBytes();
            // Extract remote client's IP and Port directly from the incoming packet
            DatagramPacket send = new DatagramPacket(
                sendData, sendData.length, receive.getAddress(), receive.getPort()
            );
            socket.send(send);
            System.out.println("Resolved IP (" + ip + ") sent back.");
        }
    }
}
