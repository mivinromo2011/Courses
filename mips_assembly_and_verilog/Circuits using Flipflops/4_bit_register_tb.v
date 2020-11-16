module four_bit_registers_tb;
wire q0,q1,q2,q3;
reg [0:3]A;
reg clk;
four_bit_register memory(A,clk,q0,q1,q2,q3);
initial
    begin
        $monitor("%b | %b | %b | %b | %b |", A,q0,q1,q2,q3);
        clk=1'b1;
        A=4'b1101;
        

        #10

        clk=1'b0;
        A=4'b1001;

        #10

        clk=1'b1;
        A=4'b1001;
        
    end
endmodule