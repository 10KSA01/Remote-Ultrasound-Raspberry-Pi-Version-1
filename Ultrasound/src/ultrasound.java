import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class ultrasound {
    
    public static void main(String[] args) throws IOException {
        Ultrasound();
    }
    public static double Ultrasound() throws IOException{
        String text = "";
        double distance = 0;
        
        // This will run the Ultrasound script from python
        ProcessBuilder builder = new ProcessBuilder("python", 
             System.getProperty("user.dir") +"/Ultrasound.py");
        Process process = builder.start();
        // Read every line that is being outputted from the pythons script
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));  
        // Output every line from python script
        while((text = reader.readLine())!= null) {
            System.out.println("Distance: " + text + "cm");
            distance = Double.valueOf(text);
        }
        return distance;
    } 
}