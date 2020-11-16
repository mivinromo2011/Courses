module and_tb;


reg t_a, t_b;
wire t_y; //-> wire data type is not required to be declared explicitly

andgate my_gate(t_a,t_b,t_y);

initial
	begin
		$monitor("A = %b B = %b Y = %b",t_a,t_b,t_y);
		t_a=1'b0;
		t_b=1'b0;

		#10

		t_a=1'b0;
		t_b=1'b1;

		#10

		t_a=1'b1;
		t_b=1'b0;
		
		#10
		
		t_a=1'b1;
		t_b=1'b1;
	end
endmodule
