import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import java.io.InputStream;
import java.net.URI; 
import py4j.GatewayServer;

public class Translator {

    private static final String API_KEY = "9aS69YyyqyRQoJxl3RK1TRFK0XRaR9DX";
    private static final String API_URL = "https://api.apilayer.com/language_translation/translate";

    public String translateText(String originalText, String targetLanguage, String sourceLanguage) throws Exception {
        // Construct the URL endpoint
        String endpoint = API_URL + "?target=" + targetLanguage;
        if (sourceLanguage != null && !sourceLanguage.isEmpty()) {
            endpoint += "&source=" + sourceLanguage;
        }

        // Convert endpoint string to URL using URI
        URI uri = new URI(endpoint);
        URL url = uri.toURL();

        // Create the HttpURLConnection object
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        // Set the request properties
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "text/plain");
        conn.setRequestProperty("apikey", API_KEY);
        conn.setDoOutput(true);  // This sets the request method to POST

        // Write the request body
        try (OutputStream os = conn.getOutputStream()) {
            os.write(originalText.getBytes("UTF-8"));
            os.flush();
        }

        // Get the response and return it
        if (conn.getResponseCode() == HttpURLConnection.HTTP_OK) {
            try (InputStream is = conn.getInputStream()) {
                return new String(is.readAllBytes(), "UTF-8");
            }
        } else {
            return "HTTP error code: " + conn.getResponseCode();
        }
    }

    public static void main(String[] args) {
        Translator app = new Translator();
        GatewayServer server = new GatewayServer(app);
        server.start();
        System.out.println("Gateway Server Started");
    }
}
