#! /usr//bin/octave -qf

% Load data
D=load('06.dat');
%D=load('06_test.dat');

dup = diag(ones(9));
ind = diag(zeros(9));

for i = unique(D)
  ind(i+1) = 1;
  dup(i+1) = dup(i+1) + sum(D==i) - 1;
endfor

%days=80;
days=256;

for i=1:days

  % Evolve 1 day
  dup=shift(dup, -1);
  ind=shift(ind, -1);

  % A zero becomes a 6 and adds a new 8 to the end of the list
  if (ind(9))
    dup(7)=dup(7)*ind(7)+dup(9);
    ind(7)=1;
    ind(9)=1;
  endif
endfor

first=sum(ind.*dup)
