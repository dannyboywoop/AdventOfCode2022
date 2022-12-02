with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Array_Stuff;           use Array_Stuff;

package Calories with
   SPARK_Mode
is

   Max_Calories_Per_Item : constant := 100_000;
   Max_Items_Per_Elf     : constant := 1_000;
   Max_Elves             : constant := 500;
   type Base_Calories_T is
     range 0 .. 3 * Max_Calories_Per_Item * Max_Items_Per_Elf;
   subtype Elf_Calories_T is
     Base_Calories_T range 0 .. Max_Calories_Per_Item * Max_Items_Per_Elf;
   subtype Item_Calories_T is Elf_Calories_T range 0 .. Max_Calories_Per_Item;

   type Elf_Calories_Arr is array (Positive range <>) of Elf_Calories_T;

   function Count_Calories (Items : Str_Arr) return Elf_Calories_Arr with
      Pre => Items'Last >= Items'First and
      Count_Zero_Length_Strings (Items, Items'Last) < Positive'Last;

   function Find_Max_Calories
     (Calories_Arr : Elf_Calories_Arr) return Elf_Calories_T with
      Post =>
      (for all Calories of Calories_Arr =>
         Calories <= Find_Max_Calories'Result);

      --  function Count_Zero_Length_Strings
      --    (Strings : Str_Arr; Up_To_Idx : Positive) return Natural is
      --    ((if Length (Strings (Up_To_Idx)) = 0 then 1 else 0) +
      --     (if Up_To_Idx = Strings'First then 0
      --      else Count_Zero_Length_Strings (Strings, Up_To_Idx - 1))) with
      --     Pre  => Up_To_Idx in Strings'Range,
      --     Post =>
   --     (Count_Zero_Length_Strings'Result <= Up_To_Idx - Strings'First + 1),
      --     Subprogram_Variant => (Decreases => Up_To_Idx);

   function Count_Zero_Length_Strings
     (Strings : Str_Arr; Up_To_Idx : Natural) return Natural is
     (if Up_To_Idx < Strings'First then 0
      else (if Length (Strings (Up_To_Idx)) = 0 then 1 else 0) +
        Count_Zero_Length_Strings (Strings, Up_To_Idx - 1)) with
      Pre  => (Up_To_Idx <= Strings'Last),
      Post =>
      (Count_Zero_Length_Strings'Result <=
       Natural'Max (0, Up_To_Idx - Strings'First + 1)),
      Subprogram_Variant => (Decreases => up_to_idx);

end Calories;
