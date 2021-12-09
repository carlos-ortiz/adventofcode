#! /usr//bin/octave -qf

% sed 's/./& /g' input > output

% Load data
D=load('09.dat');
%D=load('09_test.dat');


dim=size(D)

LP=zeros(dim);

% Get low points
LP=LP+sign(D-shift(D, 1, 1)); % down
LP=LP+sign(D-shift(D,-1, 1)); % up
LP=LP+sign(D-shift(D, 1, 2)); % right
LP=LP+sign(D-shift(D,-1, 2)); % left
LP=(LP==-4);

% Clear out low points at borders
LP(1     ,      :)=0;
LP(dim(1),      :)=0;
LP(:     ,      1)=0;
LP(:     , dim(2))=0;

% Get low points at edges
a(1,:)=sign(D(1,:)     -shift(D, 1, 2)(1,:))      + sign(D(1,:)     -shift(D,-1,2)(1,:))     + sign(D(1     ,:)-shift(D,-1,1)(1     ,:));
a(2,:)=sign(D(dim(1),:)-shift(D, 1, 2)(dim(1),:)) + sign(D(dim(1),:)-shift(D,-1,2)(dim(1),:))+ sign(D(dim(1),:)-shift(D, 1,1)(dim(1),:));
b(1,:)=sign(D(:,1)     -shift(D, 1, 1)(:,1))      + sign(D(:,1)     -shift(D,-1,1)(:,1))     + sign(D(:,1)     -shift(D,-1,2)(:,1));
b(2,:)=sign(D(:,dim(2))-shift(D, 1, 1)(:,dim(2))) + sign(D(:,dim(2))-shift(D,-1,1)(:,dim(2)))+ sign(D(:,dim(2))-shift(D, 1,2)(:,dim(2)));

a=(a==-3);
b=(b==-3);

LP(1,:)=a(1,:);
LP(dim(1),:)=a(2,:);
LP(:,1)=b(1,:);
LP(:,dim(2))=b(2,:);



corn=[1 1; dim(1) 1; 1 dim(2); dim(1) dim(2)];

% Clear out low points at corners
LP(1     ,      1)=0;
LP(dim(1),      1)=0;
LP(1     , dim(2))=0;
LP(dim(1), dim(2))=0;

% Get low points at corners
clear a

a(1)=sign(D(1     ,      1)-D(1       ,      1+1))+sign(D(1     ,      1)-D(1+1     ,        1));
a(2)=sign(D(dim(1),      1)-D(dim(1)  ,      1+1))+sign(D(dim(1),      1)-D(dim(1)-1,        1));
a(3)=sign(D(1     , dim(2))-D(1       , dim(2)-1))+sign(D(1     , dim(2))-D(1+1     ,   dim(2)));
a(4)=sign(D(dim(1), dim(2))-D(dim(1)-1,   dim(2)))+sign(D(dim(1), dim(2))-D(dim(1)  , dim(2)-1));

a=(a==min(a));

LP(1     ,      1)=a(1);
LP(dim(1),      1)=a(2);
LP(1     , dim(2))=a(3);
LP(dim(1), dim(2))=a(4);

first=sum(D(LP==1)+1)


s=D(LP==1);
whos s
