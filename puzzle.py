from logic import *

AKnight = Symbol("A adalah Knight")
AKnave = Symbol("A adalah Knave")
BKnight = Symbol("B adalah Knight")
BKnave = Symbol("B adalah Knave")
CKnight = Symbol("C adalah Knight")
CKnave = Symbol("C adalah Knave")


knowledgeBase = And(
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is a knight or a knave but not both:
    knowledgeBase,
    # If A is a knight his sentence is true:
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave his sentence is false:
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B are knights or knaves but not both:
    knowledgeBase,
    # If A is a knight, A and B are both knaves:
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, his statement is false:
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B are knights or knaves but not both:
    knowledgeBase,
    # If A is a knight, A and B are both the same:
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, his statement is false:
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight, A and B are not the same:
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave, his statement is false:
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle Pertama", knowledge0),
        ("Puzzle Kedua", knowledge1),
        ("Puzzle Ketiga", knowledge2),
    ]
    print("------------------------------------SELAMAT DATANG DI PERMAINAN KNIGHT AND KNAVE------------------------------------")
    print("Berikut merupakan jawaban dari puzzle yang kamu buat:")
    print()
    for puzzle, knowledge in puzzles:
        print(f"{puzzle} :")
        if len(knowledge.conjuncts) == 0:
            print("")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")
        print("-------------------------------------------------------------------------------------------------------------------")
    print()
    print("----------------------------------------------------TERIMAKASIH----------------------------------------------------")
if __name__ == "__main__":
    main()
