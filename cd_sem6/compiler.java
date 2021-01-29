import java.util.*;
import java.io.*;

class compiler {
  public static void main(String[] args) {
    Scanner ip_str;
    try{
      ip_str=new Scanner(new File("C:\\Users\\mivin\\Desktop\\tc.csv"));
      ip_str.useDelimiter(",");
      while (ip_str.hasNext()){
        String ip_s = ip_str.next();
        System.out.println("String is : \""+ip_s+"\"");
        int len = ip_s.length();
        int pos = 1;
        String[][] t_matrix = new String[14][9];
        BufferedReader rbuf;
        int r=0;
        FileReader tfile = new FileReader("C:\\Users\\mivin\\Desktop\\tt.csv");
        rbuf=new BufferedReader(tfile);
        String line;
        while((line=rbuf.readLine())!=null){
          String[] str = line.split(",");
          String[] states=new String[11];
          for(int x=0;x<9;x++){
            states[x]=str[x];
          }
          int s=0;
          int y=0;
          while(y<9){
            t_matrix[r][y]= states[s];
            y++;
            s++;
          }
          r++;
        }
        
        rbuf.close();
        System.out.println("States : ");
        System.out.print(pos + " --> ");   
        for (int i=0;i<len;i++) {
          char ch = ip_s.charAt(i);
          pos = Integer.parseInt(t_matrix[pos][matrix_map(ch)]);
          if (pos == 0) {
            System.out.println("Dead state!");
            break;
          } 
          else {
            if (i == len - 1)
            System.out.println("("+pos+")");
            else
            System.out.print(pos + " --> ");
          }        
        }
        if (pos>1){
          System.out.println("String accepted");
        }
        else{
          System.out.println("String rejected");
        }
        System.out.println("\n");
      }
      
    }
    catch(IOException e){
      e.printStackTrace();
    }
  }

  static int matrix_map(char ch) {
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
}
