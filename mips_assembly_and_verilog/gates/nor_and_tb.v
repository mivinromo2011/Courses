module nor_and_tb;

reg t_a,t_b;
wire t_y,t_z;

nor_and my_gate(t_a,t_b,t_y,t_z);

initial
begin
	$monitor("A = %b B = %b Y(using regular AND) = %b  Z(using NOR) = %b", t_a,t_b,t_y,t_z);
	
	t_a=1'b0;
	t_b=1'b0;

	#5

	t_a=1'b0;
	t_b=1'b1;

	#5

	t_a=1'b1;
	t_b=1'b0;

	#5

	t_a=1'b1;
	t_b=1'b1;

end
endmodule