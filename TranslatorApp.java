import py4j.GatewayServer;

public class TranslatorApp {

    private Translator translator;

    public TranslatorApp() {
        translator = new Translator();
    }

    public Translator getTranslator() {
        return translator;
    }

    public static void main(String[] args) {
        TranslatorApp app = new TranslatorApp();
        GatewayServer gatewayServer = new GatewayServer(app);
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}
