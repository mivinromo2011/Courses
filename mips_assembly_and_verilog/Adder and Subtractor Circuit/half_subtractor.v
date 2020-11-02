module subtractor(a,b,c,y);
input a,b;
output y,c;

xor(y,a,b);
and(c,~a,b);

initial 
	begin
		$display ("this is half subtractor");
	end
endmodule