module orgate(a,b,y);
input a,b;
output y;

assign y=a|b;

initial
begin
	$display("This is OR");
end
endmodule

