import java.util.Scanner;
public class nanilu{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int x = scan.nextInt();
        if(x==2){
            System.out.println("NO");
        }
        else if(x%2==1 ){
            System.out.println("NO");
        }
        else{
            System.out.println("YES");
        }
    }
}