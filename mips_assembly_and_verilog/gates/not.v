module notgate(a,y);
input a;
output y;

assign y=~a;
initial
begin
	$display("This is Not");
end
endmodule
