import java.util.Scanner;
public class Demo{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int year = a/365;
        int week = (a%365)/7;
        System.out.println(year);
        System.out.println(week);
    }
}