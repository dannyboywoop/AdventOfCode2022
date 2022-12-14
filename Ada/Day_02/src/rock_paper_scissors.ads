package Rock_Paper_Scissors with SPARK_Mode is
   pragma Elaborate_Body;
   
   type Move_T is (Rock, Paper, Scissors);
   for Move_T use (Rock => 1, Paper => 2, Scissors => 3);
   type Outcome_T is (Loss, Draw, Win);
   for Outcome_T use (Loss => 0, Draw => 3, Win => 6);
   
   Max_Turns: constant := 3_000;
   Max_Turn_Score : constant := 9;
   
   type Score_T is range 0..Max_Turn_Score * Max_Turns;
   subtype Turn_Score_T is Score_T range 0..Max_Turn_Score;
   
   subtype Turn_Idx_T is Positive range 1..Max_Turns;
   
   type Move_Pair_T is record
      Their_Move: Move_T;
      Your_Move: Move_T;
   end record;
   
   type Char_Pair_T is array (Positive range 1..2) of Character;
   type Char_Pair_Arr is array (Turn_Idx_T range <>) of Char_Pair_T with
     Predicate => Char_Pair_Arr'First = 1 and Char_Pair_Arr'Last >= Char_Pair_Arr'First;
   type Move_Pair_Arr is array (Turn_Idx_T range <>) of Move_Pair_T with
     Predicate => Move_Pair_Arr'First = 1 and Move_Pair_Arr'Last >= Move_Pair_Arr'First;
   
   function Get_Outcome(Move_Pair: Move_Pair_T) return Outcome_T;
   function Calculate_Turn_Score(Move_Pair: Move_Pair_T) return Turn_Score_T;
   function Calculate_Total_Score(Move_Pairs: Move_Pair_Arr) return Score_T;
   
   function Get_Winning_Move(Move: Move_T) return Move_T is
     (case Move is when Rock => Paper, when Paper => Scissors, when Scissors => Rock);

   function Get_Drawing_Move(Move: Move_T) return Move_T is
     (case Move is when Rock => Rock, when Paper => Paper, when Scissors => Scissors);
   
   function Get_Losing_Move(Move: Move_T) return Move_T is
     (case Move is when Rock => Scissors, when Paper => Rock, when Scissors => Paper);
   

end Rock_Paper_Scissors;
