module enc(a,b,c,d,y0,y1);
input a,b,c,d;
output y0,y1;

or(y0,b,c); 
or(y1,a,c);

//data flow 
// y0 = b+c;
// y1 = a+c;

//fourth input is don't care

initial 
	begin
		$display ("this is 4x2 encoder");
	end
endmodule
