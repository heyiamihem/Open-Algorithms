import java.util.Scanner;

public class Factorial {

	public static void main(String[] args) {

		System.out.println("Enter number: ");
		
		Scanner scanner = new Scanner(System.in);

		long input = scanner.nextLong();

		long factorial = calculateFactorial(input);
		System.out.println("Answer: "+factorial);
		
	}
	private static long calculateFactorial(long input) {
		if(input == 0) return 1;
		long fact = 1;
		for(int i=1; i<= input; i++) {
			fact *= i;
		}

		return fact;
	}

}