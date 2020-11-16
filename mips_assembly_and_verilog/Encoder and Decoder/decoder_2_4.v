module dec(a,b,y0,y1,y2,y3);
input a,b;
wire e,f;
output y0,y1,y2,y3;

not(e,a);
not(f,b);
and(y0,e,f);
and(y1,a,f);
and(y2,e,b);
and(y3,a,b);

//data flow model
// Y0=(~a)+(~b);
// Y1=(a)+(~b);
// Y2=(~a)+(b);
// Y3=(a)+(b);

initial 
	begin
		$display ("this is 2x4 Decoder");
	end
endmodule