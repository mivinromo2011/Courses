module nand_not(a,y,z);
input a;
output y,z;

assign y=a~&a;
assign z=~a;
initial
begin
	$display("This Not using NAND");
end
endmodule

