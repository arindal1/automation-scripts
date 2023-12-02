% Facts
owns_fish(Person) :- owns_pet(Person, fish).
nationality(Person, norwegian) :- owns_pet(Person, cat).
color(Person, yellow) :- owns_pet(Person, cigar).

% ... (additional rules for the puzzle)
