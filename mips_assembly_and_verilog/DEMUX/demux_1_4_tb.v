module demux_tb;


reg t_a,t_u, t_v;
wire t_y0,t_y1,t_y2,t_y3; //-> wire data type is not required to be declared explicitly

demux my_demux(t_a,t_u,t_v,t_y0,t_y1,t_y2,t_y3);

initial
	begin
		$monitor("A = %b  Select1 = %b Select2 = %b Y0 = %b Y1 = %b Y2 = %b Y3 = %b",t_a,t_u,t_v,t_y0,t_y1,t_y2,t_y3);
		t_a=1'b1;
		t_u=1'b0;
        t_v=1'b0;

		#10

		t_a=1'b1;
        t_u=1'b0;
        t_v=1'b1;

		#10

		t_a=1'b1;
        t_u=1'b1;
        t_v=1'b0;
        
		
		#10
		
		t_a=1'b1;
        t_u=1'b1;
        t_v=1'b1;

    
	end
endmodule
