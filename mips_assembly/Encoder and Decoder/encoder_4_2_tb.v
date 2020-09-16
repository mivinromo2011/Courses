module enc_tb;


reg t_a, t_b, t_c,t_d;
wire t_y0,t_y1; //-> wire data type is not required to be declared explicitly

enc my_enc(t_a,t_b,t_c,t_d,t_y0,t_y1);

initial
	begin
		$monitor("I0 = %b I1 = %b I2 = %b I3 = %b Y0 = %b Y1 = %b",t_b,t_a,t_d,t_c,t_y0,t_y1);
		
        t_d=1'b1;
        t_a=1'b0;
		t_b=1'b0;
        t_c=1'b0;

        #10

        t_d=1'b0;
        t_a=1'b1;
		t_b=1'b0;
        t_c=1'b0;

		#10

        t_d=1'b0;
		t_a=1'b0;
		t_b=1'b1;
        t_c=1'b0;
        
        
    	#10

        t_d=1'b0;
		t_a=1'b0;
		t_b=1'b0;
        t_c=1'b1;

        
	end
endmodule
