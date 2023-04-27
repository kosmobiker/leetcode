/*Write a query to print all prime numbers less than or equal to 1000.
Print your result on a single line, and use the ampersand (&) character as your separator 
(instead of a space).*/
--it is not mine, brilliant solution from https://github.com/andrei-kolesnik/hackerrank/blob/master/SQL/Print-Prime-Numbers.SQL

declare @i int, @k int, @ok bit, @result varchar(8000)
set @i = 2
set @result = ltrim(str(@i))
set @i = 3
while @i <= 1000
begin
	set @k = 2
	set @ok  = 1
	while @k <= sqrt(@i)
	begin
		if @i % @k = 0
		begin
			set @ok = 0;
			break
		end
		set @k += 1
	end
	if @ok = 1
		set @result += '&' + ltrim(str(@i))
	set @i += 1
end
print @result;