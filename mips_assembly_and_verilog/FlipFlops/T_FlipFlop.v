/* Toggle -> Invert : when clock and t bit are both 1 the previous output is toggled and produced as output if not then the previous state remains the same ans is produced as the output */

module tff(t,clk,q,qb);
    output q,qb;
    input t,clk;
    reg q,qb;
    initial
        begin
            q=1'b0;
            qb=1'b1;
        end
    always @(posedge clk)

        begin
            if(clk)
                begin
                    if(t==1'b0)
                        begin
                            q=q;
                            qb=qb;
                        end
                    else
                        begin
                            q=~q;
                            qb=~qb;
                        end
                end
        end
endmodule