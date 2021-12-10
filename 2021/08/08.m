#! /usr//bin/octave -qf

% Load data
%
% Convert original data a..g -> 1..7
%
D=load('08.dat');
%D=load('08_test.dat');

nof      = ceil(log10(D));
pow      = power(10,0:7);
notes    = D(:,1:10);
nofnotes = nof(:,1:10);
digits   = D(:,11:14);
nofdigit = nof(:,11:14);

% Find sum of occurrances of 1 7 4 8
first = sum([nofdigit==2 nofdigit==3 nofdigit==4 nofdigit==7](:))


% Decode 1 7 4 8

digits(nofdigit==2)=1;
nofdigit(nofdigit==2)=0;
digits(nofdigit==3)=7;
nofdigit(nofdigit==3)=0;
digits(nofdigit==4)=4;
nofdigit(nofdigit==4)=0;
digits(nofdigit==7)=8;
nofdigit(nofdigit==7)=0;


% Decode 0 2 3 5 6 9
for i=1:size(notes,1)

  one   = num2str(notes(i,find(nofnotes(i,:)==2)));
  four  = num2str(notes(i,find(nofnotes(i,:)==4)));
  seven = num2str(notes(i,find(nofnotes(i,:)==3)));

% A 5 digit signal means a 2 3 5 display.
% A display of 7, which has 3 segments, has 2 3 2 segments in common
%  with signals for 2 3 5
% A display of 4, which has 4 segments, has 2 3 3 segments in common
%  with signals 2 3 5
  for j=find(nofdigit(i,:)==5)
    test=num2str(digits(i,j));
    if (length(intersect(test,seven))==3)
      digits(i,j)=3;
      nofdigit(i,j)=0;
    elseif (length(intersect(test,four))==3)
      digits(i,j)=5;
      nofdigit(i,j)=0;
    else
      digits(i,j)=2;
      nofdigit(i,j)=0;
    endif
  endfor

% A 6 digit signal means a 0 6 9 display.
% A display of 7, which has 3 segments, has 3 2 3 segments in common
%  with signals for 0 6 9
% A display of 4, which has 4 segments, has 3 3 4 segments in common
%  with signals 0 6 9
  for j=find(nofdigit(i,:)==6)
    test=num2str(digits(i,j));
    if (length(intersect(test,seven))==2)
      digits(i,j)=6;
      nofdigit(i,j)=0;
    elseif (length(intersect(test,four))==4)
      digits(i,j)=9;
      nofdigit(i,j)=0;
    else
      digits(i,j)=0;
      nofdigit(i,j)=0;
    endif
  endfor

endfor

second=sum(digits*logspace(3,0,4)')
