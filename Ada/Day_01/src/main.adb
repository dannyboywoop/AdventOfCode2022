with Ada.Text_IO, File_IO, Array_Stuff;
use Ada.Text_IO, File_IO, Array_Stuff;
with Calories; use Calories;

procedure Main with SPARK_Mode is
   strings : Str_Arr:=Read_File;
   calories_arr : Nat_Arr:=Count_Calories(strings);
begin
   Put_Line(Find_Max_Calories(calories_arr)'Image);
end Main;
