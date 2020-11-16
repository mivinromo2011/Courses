module demux_tb;


reg t_a, t_s;
wire t_y0,t_y1; //-> wire data type is not required to be declared explicitly

demux my_mux(t_a,t_s,t_y0,t_y1);

initial
	begin
		$monitor("A = %b Select = %b Y0 = %b Y1 = %b" ,t_a,t_s,t_y0,t_y1);
		t_a=1'b1;
		t_s=1'b0;
        

		#10

		t_a=1'b1;
		t_s=1'b1;
        

        
	end
endmodule
