#! /usr//bin/octave -qf

% Load data
D=load('0502.dat');
%D=load('0502_test.dat');

%Read lines x1,y1,x2,y2
% AxBxC matrix
% a line dim=nof lines
% b X coordinates dim=2
% c Y coordinated dim=2
P(:,1,1)=D(:,1);
P(:,1,2)=D(:,2);
P(:,2,1)=D(:,3);
P(:,2,2)=D(:,4);
% Index starts at 1.
P=P+1;

maxp=P;
minp=P;
for i=1:ndims(P)
  maxp = max(maxp);
  minp = min(minp);
endfor
dims=[minp  maxp];
clear minp maxp i

map=zeros(dims(2));

for i=1:size(P,1)
  % Check if line is 90 degrees
  if (sum( diff(P(i,:,:))(:) == 0 ) == 1)
    % draw line on map
    x=linspace(P(i,1,1), P(i,2,1), abs(diff(P(i,:,1)))+1);
    y=linspace(P(i,1,2), P(i,2,2), abs(diff(P(i,:,2)))+1);
    map(x,y)=map(x,y)+1;
  endif
endfor

first=sum(map(:)>1)


%map=zeros(dims(2));

for i=1:size(P,1)

  % calculate angle
  ang=rad2deg(atan2(diff(P(i,:,2)),diff(P(i,:,1))));

  % check for allowed angles
  if (abs(rem(ang,45))==0 & abs(rem(ang,90)!=0))

    % draw map
    x=linspace(P(i,1,1), P(i,2,1), abs(diff(P(i,:,1)))+1);
    y=linspace(P(i,1,2), P(i,2,2), abs(diff(P(i,:,2)))+1);
    for j=1:size(x,2)
      map(x(j),y(j))=map(x(j),y(j))+1;
    endfor

  endif
endfor

second=sum(map(:)>1)

