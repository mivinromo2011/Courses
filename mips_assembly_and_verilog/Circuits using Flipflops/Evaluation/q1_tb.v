module eight_bit_registers_tb;
wire q0,q1,q2,q3,q4,q5,q6,q7;
reg [0:7]A;
reg clk;
eight_bit_register memory(A,clk,q0,q1,q2,q3,q4,q5,q6,q7);
initial
    begin
        $monitor("%b | %b | %b | %b | %b | %b | %b | %b | %b |%b |", A,q0,q1,q2,q3,q4,q5,q6,q7,clk);
        clk=1'b1;
        A=8'b11010110;
        

        #10

        clk=1'b0;
        A=8'b10011100;

        #10

        clk=1'b1;
        A=8'b10011100;
        
    end
endmodule