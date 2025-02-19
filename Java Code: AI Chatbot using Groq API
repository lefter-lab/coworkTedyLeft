import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;
import org.json.JSONArray;
import org.json.JSONObject;

public class GroqChatbot {
    private static final String API_KEY = "YOUR_API_KEY_HERE"; // Replace with your actual API key
    private static final String API_URL = "https://api.groq.com/v1/chat/completions";

    public static String getAIResponse(String userInput) {
        try {
            // Create JSON request body
            JSONObject requestBody = new JSONObject();
            requestBody.put("model", "llama3-8b-8192");
            JSONArray messages = new JSONArray();
            messages.put(new JSONObject().put("role", "user").put("content", userInput));
            requestBody.put("messages", messages);

            // Create HTTP request
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(API_URL))
                    .header("Authorization", "Bearer " + API_KEY)
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(requestBody.toString()))
                    .build();

            // Send request and get response
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            
            // Parse response
            JSONObject jsonResponse = new JSONObject(response.body());
            JSONArray choices = jsonResponse.getJSONArray("choices");
            return choices.getJSONObject(0).getJSONObject("message").getString("content");

        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to your AI chatbot! Type 'exit' to quit.");

        while (true) {
            System.out.print("\nYou: ");
            String userInput = scanner.nextLine();

            if (userInput.equalsIgnoreCase("exit") || userInput.equalsIgnoreCase("quit")) {
                System.out.println("\nGoodbye! 👋");
                break;
            }

            String response = getAIResponse(userInput);
            System.out.println("AI: " + response);
        }
        scanner.close();
    }
}
