import java.util.Scanner;
public class Main {
    public static void main (String args[]){
    Scanner Sc=new Scanner(System.in);
    System.out.println("Enter no:");
    int a=0 , b=1;
    int n=Sc.nextInt();
    System.out.println("FIBONACCI SERIES:");
    for(int i=0;i<=n;i++){
        System.out.println(a);
        int thir= a+b;
        a=b;
        b=thir; 
        
    }
}
}
