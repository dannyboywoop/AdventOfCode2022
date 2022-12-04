with Ada.Text_IO, File_IO, Array_Stuff;
use Ada.Text_IO, File_IO, Array_Stuff;
with Calories; use Calories;

procedure Main with SPARK_Mode is
   items : Str_Arr:=Read_File;
   -- Have to assume that the file isn't just Positive'Last empty lines
   pragma Assume(Count_Zero_Length_Strings (Items, Items'Last) < Positive'Last);
   calories_arr : Elf_Calories_Arr:=Count_Calories(items);
begin
   Put_Line(Find_Max_Calories(calories_arr)'Image);
   Put_Line(Find_Max_3_Calories(calories_arr)'Image);
end Main;
