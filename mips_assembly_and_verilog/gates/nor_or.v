module nor_or(a,b,y,z);
input a,b;
output y,z;

assign y=a|b;
assign z=(a~|b)~|(a~|b);

initial
begin
	$display("This using NOR");
end
endmodule
