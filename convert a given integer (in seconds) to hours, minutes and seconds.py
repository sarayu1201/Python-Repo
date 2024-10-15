import java.util.Scanner;
public class ERPUT{
    public static void main(String[] args){
         Scanner scan = new Scanner(System.in);
         int totalSeconds= scan.nextInt();
         int seconds = totalSeconds%60;
         int hours = totalSeconds/3600;
         int minutes = (totalSeconds%3600)/60;
         System.out.println("H:"+"M:"+"S-"+hours+":"+minutes+":"+seconds);
    }
}