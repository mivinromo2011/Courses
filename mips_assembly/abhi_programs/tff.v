module tff(clk,t,q,qb);
output q,qb;
input clk,t;
reg q,qb;
initial
  begin
    q=1'b1;
    qb=1'b0;
  end

always@ (posedge clk)
  begin
    if(clk)
      begin
        if(t==1'b0)
          begin
            q=q;
            qb=qb;
          end
        else
        begin
          q=~q;
          qb=~qb;
        end
      end
    end
  endmodule
