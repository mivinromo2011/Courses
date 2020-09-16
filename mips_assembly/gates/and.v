module andgate(a,b,y);
input a,b;
output y;

assign y=a&b;  //data flow modeling
//and (y,a,b);  // Gate level design by instantiating gates

initial 
	begin
		$display ("this is AND");
	end
endmodule
