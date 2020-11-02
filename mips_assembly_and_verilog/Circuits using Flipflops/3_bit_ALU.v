module aluthree(op,a,b,ty);
input a,b;
input [2:0] op;
output ty;
reg ty;

always @(a or b or op)
    begin
        case(op)
            3'b000: ty=a+b;
            3'b001: ty=a-b;
            3'b010: ty=a&b;
            3'b011: ty=a|b;
            3'b100: ty=ty;
            3'b101: ty=ty;
            3'b110: ty=ty;
            3'b111: ty=ty;
        endcase
    end
endmodule