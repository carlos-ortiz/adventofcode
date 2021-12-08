#! /usr//bin/octave -qf

% Load data
D=load('07.dat');
%D=load('07_test.dat');

for i=min(D):max(D)
  DD=abs(D-i);
  f(i+1)=sum(DD);
endfor

first=min(f) %first=sum(abs(D-median(D)))

for i=min(D):max(D)
  DD=abs(D-i);
  f(i+1)=sum(DD.*(DD+1)/2); sum_{i=1}^{n} i = n(n+1)/2
endfor

second=min(f)
