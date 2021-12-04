#! /usr//bin/octave -qf

% Load data
D=load('0402.dat');
B=load('0403.dat');
%D=load('04_test02.dat');
%B=load('04_test03.dat');


%Read dimensions
dimr=size(B,1);
dimc=size(B,2);
nb=dimr/dimc;


% Sort board data into [M x M x nb] matrix
for i=0:nb-1
  boards( :, :, i+1 )=B( i*dimc + 1 : (i+1)*dimc , 1:dimc );
endfor


% Play bingo keeping track of winner boards
score=zeros(size(boards));
d=0;
do
  d = d + 1;
  score = score +  (boards==D(d));

  % Find winner boards
  wboards = unique(ceil([find( sum( score,1 ) >= 5); find( sum( score,2 ) >= 5 )]/dimc));

until ( size(wboards,1) == 1 )

first = sum(boards(:,:,wboards)(find(not(score(:,:,wboards))))) * D(d)


% Replay bingo keeping track of winner boards
score=zeros(size(boards));
d=0;
do
  d = d + 1;
  score = score + (boards==D(d));

  % Find winner boards
  wboards = unique(ceil([find( sum( score,1 ) >= 5); find( sum( score,2 ) >= 5 )]/dimc));

until ( size(wboards,1) == nb -1 )

% Set losing board
lboard = setdiff(1:nb, wboards);


% Keep playing until final boards has bingo
do
  d = d + 1;
  score = score +  (boards==D(d));

  % Find winner boards
  wboards = unique(ceil([find( sum( score,1 ) >= 5); find( sum( score,2 ) >= 5 )]/dimc));

until ( size(wboards,1) == nb )

second = sum(boards(:,:,lboard)(find(not(score(:,:,lboard))))) * D(d)

