import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;

public class program {
	public static void main(String[] args) {
		
		String inputFile = "input.in"
		String outputFile = "output.out"
		
		String input = "";
		String output = "";
		try {
			Scanner scan = new Scanner(new File(inputFile));
			input = scan.nextLine();
			scan.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		/*
		 * Insert algorithm here!
		 * output = something
		 */
		
		try {
			PrintWriter out = new PrintWriter(new File(outputFile));
			out.println("blablabla");
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}


