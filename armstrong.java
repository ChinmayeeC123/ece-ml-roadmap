import java.util.Scanner;
public class armstrong {
    public static void main (String args[]){
    Scanner Sc=new Scanner(System.in);
    System.out.println("Enter no:");
    int num=Sc.nextInt();
    int orinum=num;
    int pow=0;
    int dig=0;
    int sum=0;
    //1.Find the number of digits (power)
    while(orinum!=0){
       orinum/=10;
        ++pow;
    }
        orinum=num;
    //2.Reset orinum to original and calculate sum
    while(orinum!=0){
        dig=orinum%10;
        sum+=Math.pow(dig,pow); 
        orinum/=10;
    }
   
    // 3. Check if it matches
        if (sum == num) {
            System.out.println(num + " is an Armstrong number.");
        } else {
            System.out.println(num + " is not an Armstrong number.");
        }
   
    }
}
