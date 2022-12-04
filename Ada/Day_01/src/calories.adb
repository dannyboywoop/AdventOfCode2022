package body Calories with
SPARK_Mode
is

   procedure Prove_Length
     (Strings : Str_Arr; Up_To_Idx_1, Up_To_Idx_2 : Natural) with
     Ghost,
     Pre  => Up_To_Idx_1 <= Up_To_Idx_2 and Up_To_Idx_2 <= Strings'Last,
     Post => Count_Zero_Length_Strings (Strings, Up_To_Idx_1) <=
       Count_Zero_Length_Strings (Strings, Up_To_Idx_2),
       Subprogram_Variant => (Decreases => Up_To_Idx_2)
   is
   begin
      if Up_To_Idx_1 = Up_To_Idx_2 then
         null;
      else
         Prove_Length (Strings, Up_To_Idx_1, Up_To_Idx_2 - 1);
      end if;

   end Prove_Length;

   function Count_Calories (Items : Str_Arr) return Elf_Calories_Arr is
      Number_Of_Elves : constant Positive :=
        Count_Zero_Length_Strings (Items, Items'Last) + 1;
      Calories_Arr : Elf_Calories_Arr (1 .. Number_Of_Elves) := (others => 0);
      cal_count    : Elf_Calories_T                          := 0;
      Elf_Idx      : Positive                                := 1;
   begin
      for Idx in Items'Range loop
         if Length (Items (Idx)) > 0 then
            cal_count := @ + Item_Calories_T'Value (To_String (Items (Idx)));
            pragma Annotate (GNATProve, Intentional, "", "TODO: Fixme" );
         else
            Prove_Length (Items, Idx, Items'Last);
            Calories_Arr (Elf_Idx) := cal_count;
            cal_count              := 0;
            Elf_Idx                := @ + 1;
         end if;
         pragma Loop_Invariant
           (Count_Zero_Length_Strings (Items, Idx) = Elf_Idx - 1);
      end loop;
      Calories_Arr (Elf_Idx) := cal_count;
      return Calories_Arr;

   end Count_Calories;

   function Find_Max_Calories
     (Calories_Arr : Elf_Calories_Arr) return Elf_Calories_T
   is
      Max_Calories : Elf_Calories_T := 0;
   begin
      for Idx in Calories_Arr'Range loop
         Max_Calories := Elf_Calories_T'Max (Max_Calories, Calories_Arr (Idx));
         pragma Loop_Invariant
           (for all Calories of Calories_Arr (Calories_Arr'First .. Idx) =>
                Calories <= Max_Calories);
      end loop;
      return Max_Calories;
   end Find_Max_Calories;

   function Find_Max_3_Calories
     (Calories_Arr : Elf_Calories_Arr) return Base_Calories_T
   is
      Top_Calories : Elf_Calories_Arr(1..3) := (others => 0);
      Max_Calories : Base_Calories_T := 0;
      begin
         for Idx in Calories_Arr'Range loop

            if Calories_Arr(Idx) >= Top_Calories(1) then
               Top_Calories(2..3) := Top_Calories(1..2);
               Top_Calories(1) := Calories_Arr(Idx);
            elsif Calories_Arr(Idx) >= Top_Calories(2) then
               Top_Calories(3) := Top_Calories(2);
               Top_Calories(2) := Calories_Arr(Idx);
            elsif Calories_Arr(Idx) >= Top_Calories(3) then
               Top_Calories(3) := Calories_Arr(Idx);
            end if;
         end loop;

         for Calories of Top_Calories loop
            Max_Calories := @ + Calories;
         end loop;

         return Max_Calories;
      end Find_Max_3_Calories;

   end Calories;
