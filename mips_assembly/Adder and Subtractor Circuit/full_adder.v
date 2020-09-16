module adder(a,b,ci,co,y);
input a,b,ci;
output y,co;
wire t,u,v,w;

xor(t,b,a);
xor(y,ci,t);
and(u,a,b);
and(v,a,ci);
and(w,b,ci);
or(co,u,v,w);

initial 
	begin
		$display ("this is full adder");
	end
endmodule
