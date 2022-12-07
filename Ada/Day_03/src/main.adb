with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Rucksacks; use Rucksacks;
with Set_Stuff; use Set_Stuff;
with File_IO; use File_IO;


procedure Main is
   use Char_Hash_Sets;
   Rucksacks: Rucksack_Arr := Rucksack_Arr(Read_File);
begin
   Put_Line(Star_1(Rucksacks)'Image);
end Main;
