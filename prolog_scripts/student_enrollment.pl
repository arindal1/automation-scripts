% Facts
enrolled(john, math101).
enrolled(jane, english102).
enrolled(bob, math101).
enrolled(bob, history103).

% Rules
has_classmate(Student1, Student2, Course) :-
    enrolled(Student1, Course),
    enrolled(Student2, Course),
    Student1 \= Student2.
