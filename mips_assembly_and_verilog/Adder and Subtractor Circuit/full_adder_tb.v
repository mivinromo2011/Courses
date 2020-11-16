module full_adder_tb;

reg t_a, t_b, t_ci;
wire t_y,t_co; //-> wire data type is not required to be declared explicitly

adder my_adder(t_a,t_b,t_ci,t_co,t_y);

initial
	begin
		$monitor("A = %b B = %b Carry in = %b  Carry out = %b Sum = %b",t_a,t_b,t_ci,t_co,t_y);
		t_a=1'b0;
		t_b=1'b0;
        t_ci=1'b0;
        
		#10

		t_a=1'b0;
		t_b=1'b0;
        t_ci=1'b1;

        #10

		t_a=1'b0;
		t_b=1'b1;
        t_ci=1'b0;
                
        #10

		t_a=1'b0;
		t_b=1'b1;
        t_ci=1'b1;

        #10

		t_a=1'b1;
		t_b=1'b0;
        t_ci=1'b0;
        
		#10

		t_a=1'b1;
		t_b=1'b0;
        t_ci=1'b1;

        #10

		t_a=1'b1;
		t_b=1'b1;
        t_ci=1'b0;
                
        #10

		t_a=1'b1;
		t_b=1'b1;
        t_ci=1'b1;
        
	end
endmodule
