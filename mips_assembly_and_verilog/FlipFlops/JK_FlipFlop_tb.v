module srff_tb;
    wire t_q,t_qb;
    reg t_clk, t_j, t_k;
    jkff my_jkff(t_j,t_k,t_clk,t_q,t_qb);
    initial
        begin
            $display("|\tCLK\t|\tJ\t|\tK\t|\tQ\t|\tQ'\t|\n");
            $monitor("|\t%b \t|\t%b\t|\t%b\t|\t%b\t|\t%b \t|", t_clk,t_j,t_k,t_q,t_qb);

            t_clk=1'b0;
            t_j=1'b0;
            t_k=1'b0;

            #10

            t_clk=1'b1;
            t_j=1'b0;
            t_k=1'b0;

            #10

            t_clk=1'b0;
            t_j=1'b0;
            t_k=1'b0;

            #10

            t_clk=1'b1;
            t_j=1'b0;
            t_k=1'b1;

            #10

            t_clk=1'b0;
            t_j=1'b1;
            t_k=1'b0;

            #10

            t_clk=1'b1;
            t_j=1'b1;
            t_k=1'b0;

            #10

            t_clk=1'b0;
            t_j=1'b1;
            t_k=1'b1;

            #10

            t_clk=1'b1;
            t_j=1'b1;
            t_k=1'b1;

            

        end
endmodule
