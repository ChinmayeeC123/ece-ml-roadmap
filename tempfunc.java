import java.util.Scanner;
public class tempfunc {
    public static void main (String args[]){
    Scanner Sc=new Scanner(System.in);
    System.out.print("Enter temperature in Celsius: ");
    float celsius=Sc.nextFloat();
    convert(celsius);
    Sc.close();
    }
    public static void convert(float celsius){
    double far=celsius*(9.0/5.0)+32;
    System.out.printf("Fahrenheit: %.2f", far); 
    }
}



