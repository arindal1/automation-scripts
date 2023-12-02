% Facts
has_gene(john, brown_eyes).
has_gene(jane, blue_eyes).
has_gene(bob, green_eyes).

% Rules
has_brown_eyes(Person) :- has_gene(Person, brown_eyes).
