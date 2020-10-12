module dff_tb;
reg t_clk,t_d;
wire t_q,t_qb;

dff my_dff(.clk(t_clk),.d(t_d),.q(t_q),.qb(t_qb));
initial
begin
  $display("|\tClk\t|\td\t|\tq\t|\tqb\t|");
  $monitor("|\t%b\t|\t%b\t|\t%b\t|\t%b\t|",t_clk,t_d,t_q,t_qb);

  t_clk = 1'b0;
  t_d = 1'b1;

  #10
  t_clk = 1'b1;
  t_d = 1'b1;

  #10
  t_clk = 1'b0;
  t_d = 1'b0;

  #10
  t_clk = 1'b1;
  t_d = 1'b0;

end
endmodule
