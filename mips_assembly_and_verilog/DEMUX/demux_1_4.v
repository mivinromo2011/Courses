module demux(a,u,v,y0,y1,y2,y3);
input a,u,v;
wire s1,s2;
output y0,y1,y2,y3;

not(s1,u);
not(s2,v);
and(y0,a,s1,s2);
and(y1,a,s1,v);
and(y2,a,u,s2);
and(y3,a,u,v);
 

initial 
	begin
		$display ("this is 1x4 DeMux");
	end
endmodule
