with Ada.Text_IO;         use Ada.Text_IO;
with File_IO;             use File_IO;
with Array_Stuff;         use Array_Stuff;
with String_Stuff;        use String_Stuff;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Rock_Paper_Scissors; use Rock_Paper_Scissors;

procedure Main is
   function Parse_Strings (strings : Str_Arr) return Char_Pair_Arr is
      Arr : Char_Pair_Arr (strings'Range);
   begin
      for Idx in strings'Range loop
         declare
            Substrings : Str_Arr := Split (strings (Idx), " ");
         begin
            Arr (Idx) :=
              Char_Pair'
                (1 => Element (Substrings (1), 1),
                 2 => Element (Substrings (2), 1));
         end;
      end loop;
      return Arr;
   end Parse_Strings;
   strings    : Str_Arr       := Read_File;
   Char_Pairs : Char_Pair_Arr := Parse_Strings (strings);
begin
   Put_Line (Char_Pairs'Image);
end Main;
