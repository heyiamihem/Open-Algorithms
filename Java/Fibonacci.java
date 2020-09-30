import java.util.Scanner;

public class Fibonacci {

	public static void main(String[] args) {

		System.out.println("How many Fibonacci Sequence would you like to generate?");
		
		Scanner scanner = new Scanner(System.in);

		long input = scanner.nextLong();

		if(input > 0) {
			getFibonacciSequence(input);
		} else{
			System.out.println(input);
		}
	}

	private static void getFibonacciSequence(long input) {
		int a = 0, b = 1; 
		System.out.print(a + " " + b);
        for (int i = 2; i < input; i++) { 
            int c = a + b; 
            a = b; 
            b = c; 
            System.out.print(" " + b);
        }
	}

}