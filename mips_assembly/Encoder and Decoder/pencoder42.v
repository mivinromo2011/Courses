module pencoder42(I1,I2,I3,I4,O1,O2,V);
input I1,I2,I3,I4;
output O1,O2,V;

assign O1=I4|(!I3)&I2;
assign O2=I4|I3;
assign V=I4|I3|I2|I1;

//wire sel_0,sel_1;
//or or1(V,I1,I2,I3,I4);
//or or2(O2,I4,I3);
//not not1(sel_0,I3);
//and and1(sel_1,sel_0,I2);
//or or3(O1,I4,sel_1);

endmodule