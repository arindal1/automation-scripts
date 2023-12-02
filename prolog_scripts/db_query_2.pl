% Facts
works(john, project1).
works(jane, project2).
works(bob, project1).
works(bob, project2).

% Rules
employee_projects(Employee, Projects) :-
   findall(Project, works(Employee, Project), Projects).
