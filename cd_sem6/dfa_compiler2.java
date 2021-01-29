
import java.util.*;
import java.io.*;

public class dfa_compiler2 {
    public static void main(String[] args) {
        Scanner in;
        try {
            in = new Scanner(new File("C:\\Users\\mivin\\Desktop\\tc.csv"));
            in.useDelimiter(",");
            while (in.hasNext())    
            {  
                String str = in.next();
                System.out.println("For string \""+str+"\"");
                Stack<String> stack1 = new Stack<String>();
                Stack<String> Lexeme = new Stack<String>();
                stack1.push("Bad"); 
                int n = str.length();
                int tmp = 1;
                String[][] tranTable = new String[14][9];
		            int i=0,j=0;
		            BufferedReader bfr;
		            FileReader file = new FileReader("C:\\Users\\mivin\\Desktop\\tt.csv");
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
                    tranTable[i][j] = s_arr[k];
                    j++;
                    k++;
                  }
                  i++;
                }
                bfr.close();
                System.out.print("State Transition:"+tmp + "=>");
                for (int l=0;l<n;l++) {
                    char ch = str.charAt(l);
                    tmp = Integer.parseInt(tranTable[tmp][get_edges(ch)]);
                    Lexeme.push(String.valueOf(ch));
                    if(isFinalState(tmp)) stack1.clear();
                    stack1.push(String.valueOf(tmp));
                    if (tmp == 0) {
                      System.out.println("Dead state:0");
                      break;
                    } else {
                      if (l == n - 1)
                        System.out.println("(Final State:"+tmp+")");
                      else
                        System.out.print(tmp + "=>");
                    }
                  }
                  Boolean fl=false;
                  while(!isFinalState(tmp)){
                    if(stack1.peek()=="bad") { fl=true; break;}
                    tmp=Integer.parseInt(stack1.pop());
                    Lexeme.pop();
                  }
                  if(fl||!isFinalState(tmp)){
                      System.out.println("Invalid String");
                  }else{
                    System.out.println("The string is valid till:"+tmp+" State.");
                    System.out.println(Lexeme.elements());
                    System.out.println("ID:"+get_finalState(tmp));
                  }
                  System.out.println("\n");
            }   
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
    }
    static Boolean isFinalState(int a){
        if(a==2||a==3||a==4||a==5||a==6||a==7||a==8||a==9||a==11||a==13||a==12) return true;
        else return false;
    }
    static int get_edges(char ch) {
        if (ch == 'i')
          return 0;
        if (ch == 'f')
          return 1;
        if (ch >= 'a' && ch <= 'z')
          return 2;
        if (ch == '.')
          return 3;
        if (ch >= '0' && ch <= '9')
          return 4;
        if (ch == '-')
          return 5;
        if (ch == '\n')
          return 6;
        if (ch == ' ')
          return 7;
        else
          return 8;
      }
      static String get_finalState(int val) {
        switch(val){
            case 2:
                return "ID";
            case 3:
                return "IF";
            case 4:
                return "ID";
            case 5:
                return "error";
            case 6:
                return "REAL";
            case 7:
                return "NUM";
            case 8:
                return "REAL";
            case 9:
                return "error";
            case 11:
                return "white space";
            case 13:
                return "error";
            case 12:
                return "white space";
            default:
              return "Not in final state";
        }
      }
}
