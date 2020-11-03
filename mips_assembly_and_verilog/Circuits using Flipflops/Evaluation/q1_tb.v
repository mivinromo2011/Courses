module eight_bit_registers_tb;
wire t_q0,t_q1,t_q2,t_q3,t_q4,t_q5,t_q6,t_q7;
reg [0:7]t_A;
reg t_clk;
eight_bit_register memory(t_A,t_clk,t_q0,t_q1,t_q2,t_q3,t_q4,t_q5,t_q6,t_q7);
initial
    begin
        $monitor("%b | %b | %b | %b | %b | %b | %b | %b | %b | %b |", t_A,t_q0,t_q1,t_q2,t_q3,t_q4,t_q5,t_q6,t_q7,t_clk);
        t_clk=1'b1;
        t_A=8'b11010110;
        

        #10

        t_clk=1'b0;
        t_A=8'b10011100;
        t_clk=1'b1;
        
        #100
        t_clk=1'b0;
        t_clk=1'b1;
        t_A=8'b10011100;
        
    end
endmodule