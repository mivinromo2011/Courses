import java.util.*;

class compiler {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter the string:");
    String str = input.nextLine();
    int n = str.length();
    int[][] edges = {
      { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
      { 2, 4, 4, 5, 7, 9, 0, 12, 13 },
      { 4, 3, 4, 0, 4, 0, 0, 0, 0 },
      { 4, 4, 4, 0, 4, 0, 0, 0, 0 },
      { 4, 4, 4, 0, 4, 0, 0, 0, 0 },
      { 0, 0, 0, 0, 6, 0, 0, 0, 0 },
      { 0, 0, 0, 0, 6, 0, 0, 0, 0 },
      { 0, 0, 0, 8, 7, 0, 0, 0, 0 },
      { 0, 0, 0, 0, 8, 0, 0, 0, 0 },
      { 0, 0, 0, 0, 0, 10, 0, 0, 0 },
      { 10, 10, 10, 0, 0, 0, 11, 0, 0 },
      { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
      { 0, 0, 0, 0, 0, 0, 0, 12, 0 },
      { 0, 0, 0, 0, 0, 0, 0, 0, 0 } };
    int cur = 1;
    System.out.println("States : ");
    System.out.print(cur + " => ");
    for (int i=0;i<n;i++) {
      char ch = str.charAt(i);
      cur = edges[cur][char_edgeMap(ch)];
      if (cur == 0) {
        System.out.println("Dead state reached");
        break;
      } else {
        if (i == n - 1)
          System.out.println("("+cur+")");
        else
          System.out.print(cur + " => ");
      }
    }
    if (cur>1){
      System.out.println("String accepted");
    }
    else
      System.out.println("String rejected");
    input.close();
  }

  static int char_edgeMap(char ch) {
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
