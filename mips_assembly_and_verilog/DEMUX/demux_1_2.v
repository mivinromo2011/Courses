module demux(a,s,y0,y1);
input a,s;
wire e;
output y0,y1;

not(e,s);
and(y1,a,s);
and(y0,a,e);
 

initial 
	begin
		$display ("this is 1x2 Demux");
	end
endmodule