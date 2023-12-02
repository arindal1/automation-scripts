% Facts
employee(john, developer).
employee(jane, designer).
employee(bob, manager).

salary(developer, 60000).
salary(designer, 50000).
salary(manager, 80000).

% Rules
get_salary(Name, Salary) :- employee(Name, Position), salary(Position, Salary).
