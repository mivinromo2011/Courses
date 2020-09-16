module mux(a,b,c,y);
input a,b,c;
wire e,f,s;
output y;

not(s,c);
and(e,a,s);
and(f,b,c);
or(y,e,f); 

initial 
	begin
		$display ("CB.EN.U4CSE18439 this is 2x1 Mux");
	end
endmodule
