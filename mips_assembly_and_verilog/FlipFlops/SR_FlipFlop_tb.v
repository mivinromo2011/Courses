module srff_tb;
    wire t_q,t_qb;
    reg t_clk, t_s, t_r;
    srff my_srff(t_s,t_r,t_clk,t_q,t_qb);
    initial
        begin
            $display("|\tCLK\t|\tS\t|\tR\t|\tQ\t|\tQ'\t|\n");
            $monitor("|\t%b \t|\t%b\t|\t%b\t|\t%b\t|\t%b \t|", t_clk,t_s,t_r,t_q,t_qb);

            t_clk=1'b0;
            t_s=1'b0;
            t_r=1'b0;

            #10

            t_clk=1'b1;
            t_s=1'b0;
            t_r=1'b0;

            #10

            t_clk=1'b0;
            t_s=1'b0;
            t_r=1'b0;

            #10

            t_clk=1'b1;
            t_s=1'b0;
            t_r=1'b1;

            #10

            t_clk=1'b0;
            t_s=1'b1;
            t_r=1'b0;

            #10

            t_clk=1'b1;
            t_s=1'b1;
            t_r=1'b0;

            #10

            t_clk=1'b0;
            t_s=1'b1;
            t_r=1'b1;

            #10

            t_clk=1'b1;
            t_s=1'b1;
            t_r=1'b1;

            

        end
endmodule
