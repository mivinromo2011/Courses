package sc;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Stream;


public class tabe3 {
	
	static int char_mapping(char c) {
		if (c == 'i')
			return 0;          
		if (c == 'f')
			return 1;
		if (c >= 'a' && c <= 'z')
			return 2;
		if (c == '.') 
			return 3;
		if (c >= '0' && c <= '9')
			return 4;
		if (c == '-')
			return 5;
		if (c == '\n')
			return 6;
		if (c == ' ')
			return 7;
		return 8;
	}


	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		HashMap<Integer, String> final_states = new HashMap<>();
		final_states.put(2, "ID");
		final_states.put(3, "IF");
		final_states.put(4, "ID");
		final_states.put(5, "error");
		final_states.put(6, "REAL");
		final_states.put(7, "NUM");
		final_states.put(8, "REAL");
		final_states.put(9, "error");
		final_states.put(11, "white space");
		final_states.put(12, "white space");
		final_states.put(13, "error");
		int[] finalstates = new int[]{ 2,3,4,5,6,7,8,9,11,12,13 }; 
		int len1=finalstates.length;
		System.out.println(len1);
		String[][] transition_table = new String[13][9];
		int i=0,j=0;
		BufferedReader bfr;
		
		
		FileReader file = new FileReader("C:\\Users\\vishnu\\eclipse\\transitions.csv");
		bfr = new BufferedReader(file);
		String line;
		
		while((line=bfr.readLine())!=null) {
			String[] a = line.split(",");
			String[] s_arr = new String[11];
			
			for(int m=0;m<9;m++) {
				s_arr[m] = a[m]; 
			}
			int k = 0;
			j = 0;
			while(j<9) {
				transition_table[i][j] = s_arr[k];
				j++;
				k++;
			}
			i++;
		}
		
		Stack  stk=new Stack();
		Stack stk1=new Stack();
		stk.push("bad");
		
		Path path = Paths.get("C:\\\\Users\\\\vishnu\\\\eclipse\\\\KeyWestTemp.txt");

		StringBuilder sb = new StringBuilder();

		try (Stream<String> stream = Files.lines(path)) {
			stream.forEach(s -> sb.append(s).append(""));
			
		} catch (IOException ex) {
			// Handle exception
		}

		String contents = sb.toString();
		int len = contents.length();
		System.out.println(len);
		

		int m = 0;
		
		
		char c;
		
	
		int curr_state = 1;
		System.out.println("Transition Steps");
		System.out.print(curr_state + "->");
		
		for (int i1 = 0; i1 < len; i1++) {
			c = contents.charAt(i1);
			System.out.println(c);
			stk1.push(c);
			//curr_state = transition_table[curr_state - 1][char_mapping(c)];
			curr_state = Integer.parseInt(transition_table[curr_state - 1][char_mapping(c)]);
			if (curr_state == -1) {
				stk.push(curr_state);
				System.out.println("TRAP STATE" + "\n");
				break;
			} else
			{
				for(int k=0;k<len1;k++) {
					if(curr_state==finalstates[k]) {
						stk.clear();
					}
				}
			
				}
				stk.push(curr_state);
				System.out.print(curr_state + "->");
		
		     System.out.println("Elements in stack"+stk);
		}
		
		if (final_states.containsKey(curr_state))
		{System.out.println();
		System.out.println("ACCEPTED, Token : " + final_states.get(curr_state) + "\n");
		}
		else
		System.out.println("NOT ACCEPTED" + "\n");
		
		
		System.out.println("Lexeme"+stk1);
	
		}
	}


