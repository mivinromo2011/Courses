module mux_tb;


reg t_a, t_b, t_c, t_d,t_u, t_v;
wire t_y; //-> wire data type is not required to be declared explicitly

mux my_mux(t_a,t_b,t_c,t_d,t_u,t_v,t_y);

initial
	begin
		$monitor("A = %b B = %b C = %b D = %b Select1 = %b Select2 = %b Y = %b",t_a,t_b,t_c,t_d,t_u,t_v,t_y);
		t_a=1'b1;
		t_b=1'b0;
        t_c=1'b0;
        t_d=1'b0;
        t_u=1'b0;
        t_v=1'b0;

		#10

		t_a=1'b0;
		t_b=1'b1;
        t_c=1'b0;
        t_d=1'b0;
        t_u=1'b0;
        t_v=1'b1;

		#10

		t_a=1'b0;
		t_b=1'b0;
        t_c=1'b1;
        t_d=1'b0;
        t_u=1'b1;
        t_v=1'b0;
        
		
		#10
		
		t_a=1'b0;
		t_b=1'b0;
        t_c=1'b0;
        t_d=1'b1;
        t_u=1'b1;
        t_v=1'b1;

    
	end
endmodule
