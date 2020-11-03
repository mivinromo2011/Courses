/* Using 8 SR Flipflops */

module srff(s,r,clk,q,qb);
    output q,qb;
    input s,r,clk;
    reg q,qb;

    initial
        begin
            q=1'b0;
            qb=1'b1;
        end
    always @(posedge clk)
        begin
            case({s,r})
                {1'b0,1'b0}:
                    begin
                        q=q;
                        qb=qb;
                    end
                {1'b0,1'b1}:
                    begin
                        q=0;
                        qb=1;
                    end
                {1'b1,1'b0}:
                    begin
                        q=1;
                        qb=0;
                    end
                {1'b1,1'b1}:
                    begin
                        q=1'bx;
                        qb=1'bx;
                    end
            endcase
        end
endmodule

module eight_bit_register(A,clk,q0,q1,q2,q3,q4,q5,q6,q7);
    input [0:7] A;
    input clk;
    output wire q0,q1,q2,q3,q4,q5,q6,q7;
    wire qb0,qb1,qb2,qb3,qb4,qb5,qb6,qb7;
    reg s0,s1,s2,s3,s4,s5,s6,s7;

    srff srff0(s0,1'b0,clk,q0,qb0);
    srff srff1(s1,1'b0,clk,q1,qb1);
    srff srff2(s2,1'b0,clk,q2,qb2);
    srff srff3(s3,1'b0,clk,q3,qb3);
    srff srff4(s4,1'b0,clk,q4,qb4);
    srff srff5(s5,1'b0,clk,q5,qb5);
    srff srff6(s6,1'b0,clk,q6,qb6);
    srff srff7(s7,1'b0,clk,q7,qb7);

    always @(posedge clk)
        if(clk)
            begin
                s0=A[0];
                s1=A[1];
                s2=A[2];
                s3=A[3];
                s4=A[4];
                s5=A[5];
                s6=A[6];
                s7=A[7];
                
            end
    endmodule

