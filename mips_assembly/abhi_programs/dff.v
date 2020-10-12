module dff(clk,d,q,qb);
input clk,d;
output q,qb;
reg q,qb;
initial
begin
 q=1'b0;
 qb=1'b1;

end
always @(posedge clk)
  begin
    q=d;
    qb= ~d;
  end
endmodule
