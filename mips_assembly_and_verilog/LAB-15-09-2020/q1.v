module add(a3,a2,a1,a0,b,y3,y2,y1,y0,co);
input a3,a2,a1,a0,b;
output y3,y2,y1,y0,co;
wire y3,y2,y1,y0,c0,c1,c2;

xor(y0,b,a0);
and(c0,a,b);
xor(y1,c0,a1);
and(c1,a1,c0);
xor(y2,c1,a2);
and(c2,a2,c1);
xor(y3,c2,a3);
and(co,a3,c2);

endmodule




