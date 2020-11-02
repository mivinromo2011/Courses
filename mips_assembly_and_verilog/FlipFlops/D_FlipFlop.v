/* The D FLipflop outputs the previous state if the clock is falling and outputs the present input if the clock is rising */

module dff(d,clk,q,qb);
    input d,clk;
    output q,qb;
    reg q,qb;
    initial
    begin
        q=1'b0;      /* Arbitrary previous state values set by us */
        qb=1'b1;
    end

    always @(posedge clk)
        begin
            q=d;
            qb=~d;
        end
endmodule