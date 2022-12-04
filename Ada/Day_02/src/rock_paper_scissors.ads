package Rock_Paper_Scissors with SPARK_Mode is
   pragma Elaborate_Body;
   
   Max_Moves: constant := 3_000;
   
   type Char_Pair is array (Positive range 1..2) of Character;
   type Char_Pair_Arr is array (Positive range <>) of Char_Pair with
     Predicate => Char_Pair_Arr'First = 1 and Char_Pair_Arr'Last >= Char_Pair_Arr'First;
   
   type Move is (Rock, Paper, Scissors);
   
   type Move_Pair is record
      Their_Move: Move;
      Your_Move: Move;
   end record;
   
   

end Rock_Paper_Scissors;
