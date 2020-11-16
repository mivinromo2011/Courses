module add_tb;
wire t_y3,t_y2,t_y1,t_y0,t_co;
reg t_a3,t_a2,t_a1,t_a0,t_b;
add my_adder(t_a3,t_a2,t_a1,t_a0,t_b,t_y3,t_y2,t_y1,t_y0,t_co);
initial 
begin
	$monitor("a3=%b a2=%b a1=%b a0=%b b=%b y3=%b y2=%b y1=%b y0=%b co=%b",t_a3,t_a2,t_a1,t_a0,t_b,t_y3,t_y2,t_y1,t_y0,t_co);
	t_b=1;
    t_a3=1;
	t_a2=0;
	t_a1=1;
	t_a0=0;
	#5
   	t_b=1;
    t_a3=1;
	t_a2=0;
	t_a1=1;
	t_a0=1;
	#5
   	t_b=1;
    t_a3=0;
	t_a2=1;
	t_a1=1;
	t_a0=1;

end
endmodule