module comp_tb;
reg [3:0] t_a,t_b;
wire t_eq,t_lt,t_gt;

comp my_gate(.a(t_a),.b(t_b),.eq(t_eq),.lt(t_lt),.gt(t_gt));
initial
begin
  $display("|\tA\t|\tB\t|\teq\t|\tlt\t|\tgt\t|");
  $monitor("|\t%b\t|\t%b\t|\t%b\t|\t%b\t|\t%b\t|",t_a,t_b,t_eq,t_lt,t_gt);

  t_a = 4'b1100;
  t_b = 4'b1100;
  #10;

  t_a = 4'b0100;
  t_b = 4'b1100;
  #10;

  t_a = 4'b1111;
  t_b = 4'b1100;
  #10;

  t_a = 4'b0010;
  t_b = 4'b0100;
  #10;

  t_a = 4'b0000;
  t_b = 4'b1110;
  #10;

  t_a = 4'b0110;
  t_b = 4'b0001;
  #10;

  t_a = 4'b0011;
  t_b = 4'b1100;
  #10;

  t_a = 4'b1010;
  t_b = 4'b0101;
  #10;

  t_a = 4'b1111;
  t_b = 4'b1111;
  #10;
  end
  endmodule
