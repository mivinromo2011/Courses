module tff_tb;
  wire t_q,t_qb;
  reg t_clk,t_t;
  tff my_gate(.clk(t_clk),.t(t_t),.q(t_q),.qb(t_qb));
  initial
    begin
    $display("|\tClk\t|\tt\t|\tq\t|\tqb\t|");
    $monitor("|\t%b\t|\t%b\t|\t%b\t|\t%b\t|",t_clk,t_t,t_q,t_qb);

    t_clk = 0;
    t_t = 1'b0;

    #100
    t_clk = 1'b1;
    t_t = 1'b1;

    #100
    t_clk = 1'b0;
    t_t = 1'b1;

    #100
    t_clk = 1'b1;
    t_t = 1'b1;

    #100
    t_t=1'b0;
    t_clk=1'b1;
    end

  endmodule
