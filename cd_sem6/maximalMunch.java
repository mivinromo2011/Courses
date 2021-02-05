// V.V.Mithun Rosinth
// CB.EN.U4CSE18439
import java.util.*;
import java.io.*;

public class maximalMunch {
    public static void main(String[] args) {
        Scanner ip;
        try {
            ip = new Scanner(new File("C:\\Users\\mivin\\Desktop\\tc.csv"));
            ip.useDelimiter(",");
            while (ip.hasNext())    
            {  
                String str = ip.next();
                System.out.println("For string \""+str+"\"");
                Stack<String> Index_Stack = new Stack<String>();
                Stack<String> Pro_Stack = new Stack<String>();
                Stack<String> Lexeme = new Stack<String>();
                Pro_Stack.push("Bad"); 
                Index_Stack.push("Bad");
                int n = str.length();
                int cur_st = 1;
                int r=12,c=13;
                int ip_pos=0;
                Boolean failed[][] = new Boolean[r][c];
                for (int x=0;x<r ;x++ ) {
                  for (int y=0;y<c ;y++ ) {
                    failed[x][y]=false;
                  }
                  
                }
                String[][] Trans_Matrix = new String[13][12];
		            int i=0,j=0;
		            BufferedReader bfr;
		            FileReader file = new FileReader("C:\\Users\\mivin\\Desktop\\tt.csv");
		            bfr = new BufferedReader(file);
		            String line;
                int ptr=0;
                while((line=bfr.readLine())!=null) {
                  String[] a = line.split(",");
                  String[] s_arr = new String[11];
                  for(int m=0;m<12;m++) {
                    s_arr[m] = a[m]; 
                  }
                  int k = 0;
                  j = 0;
                  while(j<12) {
                    Trans_Matrix[i][j] = s_arr[k];
                    j++;
                    k++;
                  }
                  i++;
                }
                bfr.close();
                System.out.print("State Transition:"+cur_st + "=>");
                for (int l=ptr;l<n;l++) {
                    char ch = str.charAt(l);
                    cur_st = Integer.parseInt(Trans_Matrix[cur_st][get_edges(ch)]);
                    Lexeme.push(String.valueOf(ch));
                    if(failed[cur_st][ip_pos]){
                      System.out.print("(Final State:" + cur_st + ")");
                    }
                    if(Check_FS(cur_st)){
                      Pro_Stack.clear();
                      Index_Stack.clear();
                    }

                    Pro_Stack.push(String.valueOf(cur_st));
                    Index_Stack.push(String.valueOf(ip_pos));
                    if (cur_st == 0) {
                      System.out.println("Dead state: 0");
                      break;
                    } else {
                      if (l == n - 1)
                        System.out.println("(Final State:"+cur_st+")");
                      else
                        System.out.print(cur_st + "=>");
                    }
                  }
                  Boolean fl=false;
                  while(!Check_FS(cur_st)){
                    if(Pro_Stack.peek()=="bad") { fl=true; break;}
                    cur_st=Integer.parseInt(Pro_Stack.pop());
                    failed[cur_st][ip_pos]=true;
                    ptr=cur_st;
                    if(Check_FS(cur_st))
                      break;
                    Lexeme.pop();
                  }
                  if(fl||!Check_FS(cur_st)){
                      System.out.println("Invalid String");
                  }else{
                    System.out.println("The string is valid till:"+cur_st+" State.");
                    System.out.println(Lexeme.elements());
                    System.out.println("Customer Type:"+ffst(Lexeme.get(5)));
                  }
                  System.out.println("\n");
            }   
        } catch (IOException e) {
            e.printStackTrace();
        }
        
    }
    static Boolean Check_FS(int a){
        if(a==10) return true;
        else return false;
    }
    static int get_edges(char ch) {
        if (ch >= '0' && ch <= '9')
		  return 1;
		if (ch == 'P')
          return 2;
        if (ch == 'C')
          return 3;
        if (ch == 'H')
          return 4;
        if (ch == 'F')
		  return 5;
		if (ch == 'A')
		  return 6;
		if (ch == 'T')
		  return 7;
		if (ch == 'B')
		  return 8;
		if (ch == 'L')
		  return 9;
		if (ch == 'J')
		  return 10;
		if (ch == 'G')
		  return 11;
		if (ch >= 'A' && ch <= 'Z')
          return 12;
        else
          return 13;
      }
      static String ffst(char val) {
		if(val=='P'){
			return "Personal";
		}
		else{
			return "Firm/Government";
		}
      }
}
