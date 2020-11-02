module tff_tb;
    wire t_q,t_qb;
    reg t_clk, t_t;
    tff my_tff(t_t,t_clk,t_q,t_qb);
    initial
        begin
            $display("|\tCLK\t|\tT\t|\tQ\t|\tQ'\t|\n");
            $monitor("|\t%b \t|\t%b\t|\t%b\t|\t%b \t|", t_clk,t_t,t_q,t_qb);

            t_clk=1'b0;
            t_t=1'b1;

            #100
    
            t_clk=1'b1;
            t_t=1'b1;

            #100
    
            t_clk=1'b0;
            t_t=1'b0;

            #100

            t_clk=1'b1;
            t_t=1'b0;

        end
endmodule
