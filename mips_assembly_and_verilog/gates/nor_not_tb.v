module nor_not_tb;

reg t_a;
wire t_y, t_z;

nor_not my_gate(t_a,t_y,t_z);

initial
begin
	$monitor("A = %b  Y(Using NOR) = %b  Z(Using NOT) = %b", t_a,t_y,t_z);
	t_a=1'b0;

	#10

	t_a=1'b1;

end
endmodule
