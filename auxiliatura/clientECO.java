import java.io.*;
import java.net.*;

public class EcoClient {
    public static void main(String[] args) {
        String hostname = "127.0.0.1";
        int port = 12345;

        try (Socket socket = new Socket(hostname, port)) {
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

            String userInput;
            while ((userInput = stdIn.readLine()) != null) {
                out.println(userInput);
                System.out.println("Eco: " + in.readLine());
                if ("adios".equalsIgnoreCase(userInput.trim())) {
                    break;
                }
            }
        } catch (UnknownHostException e) {
            System.err.println("No se conoce al host " + hostname);
        } catch (IOException e) {
            System.err.println("No se pudo obtener I/O para la conexión a " + hostname);
        }
    }
}
