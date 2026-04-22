import java.util.Scanner;
public class condt {
    public static void main (String args[]){
    Scanner Sc=new Scanner(System.in);
    //int a=10;
    //int b=5;
   //int x=0;
   //System.out.print(x=(a>b)?a:b);//ternary op
    System.out.print("Enter a day:");
    int day= Sc.nextInt();
    switch(day){
        case 1:
            System.out.println("Monday");
            break;
        case 2:
            System.out.println("Tuesday");
            break;
        case 3:
            System.out.println("Wednesday");
            break;
        case 4:
            System.out.println("Thursday");
            break;
        case 5:
            System.out.println("Friday");
            break;
        case 6:
            System.out.println("Saturday");
            break;
        case 7:
            System.out.println("Sunday");
            break;
        default:
                 System.out.println("INVALID");

    }

}
}
