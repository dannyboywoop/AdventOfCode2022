with Ada.Text_IO;           use Ada.Text_IO;
with File_IO;               use File_IO;
with Array_Stuff;           use Array_Stuff;
with String_Stuff;          use String_Stuff;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Rock_Paper_Scissors;   use Rock_Paper_Scissors;

procedure Main is
   function Parse_Strings (Strings : Str_Arr) return Char_Pair_Arr is
      Arr : Char_Pair_Arr (Strings'Range);
   begin
      for Idx in Strings'Range loop
         declare
            Substrings : Str_Arr := Split (Strings (Idx), " ");
         begin
            Arr (Idx) :=
              Char_Pair_T'
                (1 => Element (Substrings (1), 1),
                 2 => Element (Substrings (2), 1));
         end;
      end loop;
      return Arr;
   end Parse_Strings;

   function Get_Their_Move(Char: Character) return Move_T is
     (case Char is
         when 'A'    => Rock,
         when 'B'    => Paper,
         when 'C'    => Scissors,
         when others => Rock);

   function Generate_Moves_1 (Char_Pairs : Char_Pair_Arr) return Move_Pair_Arr
   is
      Move_Pairs : Move_Pair_Arr (Char_Pairs'Range);
   begin
      for Idx in Char_Pairs'Range loop
         Move_Pairs (Idx) :=
           Move_Pair_T'
             (Their_Move => Get_Their_Move(Char_Pairs(Idx) (1)),
              Your_Move =>
                (case Char_Pairs (Idx) (2) is
                    when 'X' => Rock,
                    when 'Y' => Paper,
                    when 'Z' => Scissors,
                    when others => Rock));
      end loop;
      return Move_Pairs;
   end Generate_Moves_1;

   function Generate_Moves_2 (Char_Pairs : Char_Pair_Arr) return Move_Pair_Arr
   is
      Move_Pairs : Move_Pair_Arr (Char_Pairs'Range);
   begin
      for Idx in Char_Pairs'Range loop
         declare
            Their_Move : Move_T := Get_Their_Move(Char_Pairs(Idx) (1));
         begin
            Move_Pairs (Idx) :=
              Move_Pair_T'
                (Their_Move => Their_Move,
                 Your_Move =>
                   (case Char_Pairs (Idx) (2) is
                       when 'X' => Get_Losing_Move(Their_Move),
                       when 'Y' => Get_Drawing_Move(Their_Move),
                       when 'Z' => Get_Winning_Move(Their_Move),
                       when others => Rock));
         end;
      end loop;
      return Move_Pairs;
   end Generate_Moves_2;

   Strings    : Str_Arr       := Read_File;
   Char_Pairs : Char_Pair_Arr := Parse_Strings (Strings);
begin
   Put_Line (Calculate_Total_Score (Generate_Moves_1 (Char_Pairs))'Image);
   Put_Line (Calculate_Total_Score (Generate_Moves_2 (Char_Pairs))'Image);
end Main;
