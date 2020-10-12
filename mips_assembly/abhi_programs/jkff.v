module jkff(j,k,clk,q,qb);
  output q,qb;
  input j,k,clk;
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
          if(j==1'b0 && k==1'b0)
            begin
              q=q;
              qb=qb;
            end
          if(j==1'b0&&k==1'b1)
            begin
              q=1'b0;
              qb=1'b1;
            end
          if(j==1'b1&&k==1'b0)
            begin
              q=1'b1;
              qb=1'b0;
            end
          if(j==1'b1&&k==1'b1)
            begin
              q=~q;
              qb=~qb;
            end
          end
        end
      endmodule
