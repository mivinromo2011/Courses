module dff_tb;
wire t_q,t_qb;
reg t_d,t_clk;

dff mydff(t_d,t_clk,t_q,t_qb);
initial
begin
    $display("|\tCLK\t|\tD\t|\tQ\t|\tQ'\t|\n");
    $monitor("|\t%b \t|\t%b\t|\t%b\t|\t%b \t|", t_clk,t_d,t_q,t_qb);

    t_clk=1'b0;
    t_d=1'b1;

    #10
    
    t_clk=1'b1;
    t_d=1'b1;

    #10
    
    t_clk=1'b0;
    t_d=1'b0;

    #10
    t_clk=1'b1;
    t_d=1'b0;

end
endmodule
