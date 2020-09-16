module dec_tb;


reg t_a, t_b;
wire t_y0,t_y1,t_y2,t_y3; //-> wire data type is not required to be declared explicitly

dec my_dec(t_a,t_b,t_y0,t_y1,t_y2,t_y3);

initial
	begin
		$monitor("A = %b B = %b Y0 = %b Y1 = %b Y2 = %b Y3 = %b",t_b,t_a,t_y0,t_y1,t_y2,t_y3);
        t_a=1'b0;
		t_b=1'b0;
        
        #10

		t_a=1'b1;
		t_b=1'b0;
        
        #10

		t_a=1'b0;
		t_b=1'b1;
        
        #10

		t_a=1'b1;
		t_b=1'b1;

        
	end
endmodule
