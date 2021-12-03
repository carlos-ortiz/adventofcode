#! /usr//bin/octave -qf

D=load('0301.dat');
%D=load('03_test01.dat');
R=round(mean(D));

% Set binary-to-decimal conversion array
i=size(D,2)-1:-1:0;
t=2.^i';  % Transposed. [MxN] * [NxM] = scalar.

first=(R*t)*(not(R)*t)


d1=D;
i=1;
while (size(d1,1) > 1)
  r1=round(mean(d1));
  d1=d1(d1(:,i)==r1(i),:);
  i=i+1;
endwhile

d2=D;
i=1
while (size(d2,1) > 1)
  r2=mean(d2)>=0.5;
  d2=d2(d2(:,i)!=r2(i),:);
  i=i+1;
endwhile

second=(d1*t)*(d2*t)
