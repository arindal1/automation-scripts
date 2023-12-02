% Facts
symptom(fever).
symptom(cough).
symptom(headache).

% Rules
diagnosis(cold) :- symptom(fever), symptom(cough).
diagnosis(flu) :- symptom(fever), symptom(headache).
