module aluthree_tb;
reg a,b;
reg [2:0]op;
wire y;

aluthree myalu(op,a,b,y);

initial
    begin
        $display("000-add \n001-sub \n010-and \n011-or");
        $display("|op |a|b|y|");
        $monitor("|%3b|%b|%b|%b|",op,a,b,y);

        op=3'b000;
        a=1'b1;
        b=1'b0;

        #10

        op=3'b001;
        a=1'b1;
        b=1'b1;

        #10
        
        op=3'b010;
        a=1'b1;
        b=1'b0;

        #10

        op=3'b011;
        a=1'b1;
        b=1'b0;

    end
endmodule