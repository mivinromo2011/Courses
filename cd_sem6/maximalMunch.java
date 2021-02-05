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
                int r=13,c=13;
                int ip_pos=0;
                Boolean failed[][] = new Boolean[r][c];
                for (int x=0;i<r ;i++ ) {
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
                    System.out.println("ID:"+ffst(cur_st));
                  }
                  System.out.println("\n");
            }   
        } catch (IOException e) {
            e.printStackTrace();
        }
        
    }
    static Boolean Check_FS(int a){
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
      static String ffst(int val) {
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
