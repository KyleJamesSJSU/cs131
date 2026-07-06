BEGIN {
	FS = " "
}
{
	totalSalary += $2
	departments[$3]++
}
END {
	# print lines for employee count
	print "Total employees: " NR
	# sum of all salaries
	print "Total salary paid: " totalSalary
	# avg salary (total / employees)
	print "Average salary: " (totalSalary / NR)
	# count last term
	print "Employees per department:"
	for (d in departments) {
		print "\t" d ": " departments[d] " employees"
	}
}
