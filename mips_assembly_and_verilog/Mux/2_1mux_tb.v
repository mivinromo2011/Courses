module mux_tb;


reg t_a, t_b, t_c;
wire t_y; //-> wire data type is not required to be declared explicitly

mux my_mux(t_a,t_b,t_c,t_y);

initial
	begin
		$monitor("A = %b B = %b Select = %b Y = %b",t_a,t_b,t_c,t_y);
		t_a=1'b1;
		t_b=1'b0;
        t_c=1'b0;

		#10

		t_a=1'b0;
		t_b=1'b1;
        t_c=1'b1;

        
	end
endmodule
