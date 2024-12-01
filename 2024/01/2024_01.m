format long

load 2024_01.dat;
S=sort(X2024_01);
sum(abs(S(:,1)-S(:,2)))


i=1:size(X2024_01,1);
D=sum(X2024_01(:,2)==X2024_01(i));
sum(X2024_01(:,1).*transpose(D))
