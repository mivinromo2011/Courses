/* Same as SR except for (j=1,k=1) where the previous output is toggled */


module jkff(j,k,clk,q,qb);
    output q,qb;
    input j,k,clk;
    reg q,qb;

    initial
        begin
            q=1'b1;
            qb=1'b0;
        end
    always @(posedge clk)
        begin
            case({j,k})
                {1'b0,1'b0}:
                    begin
                        q=q;
                        qb=qb;
                    end
                {1'b0,1'b1}:
                    begin
                        q=0;
                        qb=1;
                    end
                {1'b1,1'b0}:
                    begin
                        q=1;
                        qb=0;
                    end
                {1'b1,1'b1}:
                    begin
                        q=~q;
                        qb=~qb;
                    end
            endcase
        end
endmodule