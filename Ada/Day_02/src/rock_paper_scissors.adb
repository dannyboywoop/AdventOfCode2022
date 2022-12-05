package body Rock_Paper_Scissors with SPARK_Mode is
   
   function Get_Outcome(Move_Pair: Move_Pair_T) return Outcome_T is
   begin
      case Move_Pair.Their_Move is
         when Rock => return (case Move_Pair.Your_Move is when Rock => Draw, when Paper => Win, when Scissors => Loss);
         when Paper => return (case Move_Pair.Your_Move is when Rock => Loss, when Paper => Draw, when Scissors => Win);
         when Scissors => return (case Move_Pair.Your_Move is when Rock => Win, when Paper => Loss, when Scissors => Draw);
      end case;
      
   end Get_Outcome;
   
   function Calculate_Turn_Score(Move_Pair: Move_Pair_T) return Turn_Score_T is
   begin
      return Move_T'Enum_Rep(Move_Pair.Your_Move) + Outcome_T'Enum_Rep(Get_Outcome(Move_Pair));
   end Calculate_Turn_Score;
   
   function Calculate_Total_Score(Move_Pairs: Move_Pair_Arr) return Score_T is
      Total : Score_T := 0;
   begin
      for Move_Pair of Move_Pairs loop
         Total := @ + Calculate_Turn_Score(Move_Pair);
      end loop;
      return Total;
   end;

end Rock_Paper_Scissors;
