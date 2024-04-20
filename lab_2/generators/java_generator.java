import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class BinarySequenceGenerator {
    
    public static void main(String[] args) {
        String binarySequence = generateBinarySequence(128);
        
        try {
            writeToFile(binarySequence, "random_java_sequence.txt");
            System.out.println("Двоичная последовательность успешно записана в файл.");
        } catch (IOException e) {
            System.out.println("Ошибка при записи в файл: " + e.getMessage());
        }
    }
    
    public static String generateBinarySequence(int length) {
        Random random = new Random();
        StringBuilder binarySequence = new StringBuilder();
        
        for (int i = 0; i < length; i++) {
            int bit = random.nextInt(2); // генерация случайного бита (0 или 1)
            binarySequence.append(bit);
        }
        
        return binarySequence.toString();
    }
    
    public static void writeToFile(String content, String fileName) throws IOException {
        FileWriter writer = new FileWriter(fileName);
        writer.write(content);
        writer.close();
    }
}