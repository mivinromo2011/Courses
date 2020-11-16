module nand_or(a,b,y,z);
input a,b;
output y,z;

assign y=a|b;
assign z=(a~&a)~&(b~&b);

initial
begin
	$display("This OR using NAND");
end
endmodule
