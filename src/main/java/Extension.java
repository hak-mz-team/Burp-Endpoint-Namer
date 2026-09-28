import burp.api.montoya.BurpExtension;
import burp.api.montoya.MontoyaApi;
import burp.api.montoya.http.message.requests.HttpRequest;
import burp.api.montoya.ui.hotkey.HotKey;
import burp.api.montoya.ui.hotkey.HotKeyContext;
import burp.api.montoya.ui.hotkey.HotKeyHandler;

public class Extension implements BurpExtension {

    @Override
    public void initialize(MontoyaApi api) {

        api.extension().setName("Quick Repeater");

        HotKey hotKey = HotKey.hotKey(
                "Send request to Repeater",
                "Ctrl+R"
        );

        HotKeyHandler handler = event -> {

            event.messageEditorRequestResponse().ifPresent(editor -> {

                HttpRequest request =
                        editor.requestResponse().request();

                String path = request.pathWithoutQuery();

                String endpointName = getEndpointName(path);

                api.repeater().sendToRepeater(
                        request,
                        endpointName
                );

                api.logging().logToOutput(
                        "Sent to Repeater: " + endpointName
                );
            });
        };

        api.userInterface().registerHotKeyHandler(
                HotKeyContext.HTTP_MESSAGE_EDITOR,
                hotKey,
                handler
        );

        api.logging().logToOutput(
                "Quick Repeater loaded - Ctrl+R"
        );
    }

    private String getEndpointName(String path) {

        if (path == null || path.isEmpty()) {
            return "request";
        }

        while (path.length() > 1 && path.endsWith("/")) {
            path = path.substring(0, path.length() - 1);
        }

        int lastSlash = path.lastIndexOf('/');

        if (lastSlash >= 0 && lastSlash < path.length() - 1) {
            return path.substring(lastSlash + 1);
        }

        return path;
    }
}
