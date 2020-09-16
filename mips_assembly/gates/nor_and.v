module nor_and(a,b,y,z);
input a,b;
output y,z;

assign y=a&b;
assign z=(a~|a)~|(b~|b);

initial
begin
	$display("This OR using NOR");
end
endmodule