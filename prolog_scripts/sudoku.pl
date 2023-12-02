% Rules
valid([]).
valid([H|T]) :- all_diff(H), valid(T).

all_diff([]).
all_diff([H|T]) :- not(member(H, T)), all_diff(T).

sudoku(Puzzle, Solution) :-
   Solution = Puzzle,
   Puzzle = [S11, S12, S13, S14,
             S21, S22, S23, S24,
             S31, S32, S33, S34,
             S41, S42, S43, S44],

   valid([S11, S12, S13, S14,
          S21, S22, S23, S24,
          S31, S32, S33, S34,
          S41, S42, S43, S44]).
