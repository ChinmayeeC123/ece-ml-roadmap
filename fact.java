import java.util.Scanner;
public class fact {
    public static void main (String args[]){
    Scanner Sc=new Scanner(System.in);
     System.out.println("Give n:");
    int n=Sc.nextInt();
    int num=1;
     for(int i=n;i>0;i--){
        num=num*i;
     }
     
     System.out.println("Factorial of "+n+ " is:"+num);

    
    }

}
