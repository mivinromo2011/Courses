module mux(a,b,c,d,u,v,y);
input a,b,c,d,u,v;
wire e,f,g,h,s1,s2;
output y;

not(s1,u);
not(s2,v);
and(e,a,s1,s2);
and(f,b,s1,v);
and(g,c,u,s2);
and(h,d,u,v);
or(y,e,f,g,h); 

initial 
	begin
		$display ("CB.EN.U4CSE18439 this is 4x1 Mux");
	end
endmodule
