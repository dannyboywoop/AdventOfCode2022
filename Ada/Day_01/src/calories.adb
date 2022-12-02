with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

package body Calories with SPARK_Mode is
   
   function Count_Zero_Length_Strings(strings: Str_Arr; up_to_idx: Natural) return Natural is 
     (if up_to_idx < strings'First then 0 else 
        (if Length(strings(up_to_idx))=0 then 1 else 0) + Count_Zero_Length_Strings(strings, up_to_idx - 1))
       with Pre => (up_to_idx <= strings'Last),
       Post => (Count_Zero_Length_Strings'Result <= Natural'Max(0, up_to_idx - strings'First + 1)),
       SubProgram_Variant => (Decreases => up_to_idx);
   
   procedure Prove_Length(strings: Str_Arr; up_to_idx_1, up_to_idx_2: Natural) with 
     Ghost, Pre => up_to_idx_1 <= up_to_idx_2 and up_to_idx_2 <= strings'Last,
     Post => Count_Zero_Length_Strings(strings, up_to_idx_1) <= Count_Zero_Length_Strings(strings, up_to_idx_2),
       SubProgram_Variant => (Decreases => up_to_idx_2)
   is
   begin
      if up_to_idx_1 = up_to_idx_2 then null;
      else Prove_Length(strings, up_to_idx_1, up_to_idx_2 - 1);
      end if;
      
   end Prove_Length;

   function Count_Calories(calories: Str_Arr) return Nat_Arr is
   begin      
      declare
         calories_arr_size: constant Positive := Count_Zero_Length_Strings(calories, calories'Last) + 1;
         calories_arr: Nat_Arr(1..calories_arr_size);
         cal_count: Natural:=0;
         idx: Positive:=1;
      begin
         for cal_str_idx in calories'Range loop
            if Length(calories(cal_str_idx)) = 0 then
               Prove_Length(calories, cal_str_idx, calories'Last);
               calories_arr(idx) := cal_count;
               idx := @ + 1;
               cal_count := 0;
            else
               cal_count := @ + Integer'Value(To_String(calories(cal_str_idx)));
            end if;
            pragma Loop_Invariant(Count_Zero_Length_Strings(calories, cal_str_idx) = idx-1);
         end loop;         
         calories_arr(idx) := cal_count;
         return calories_arr;
      end;
         
      
   end Count_Calories;
   
   
   function Find_Max_Calories(calories_arr: Nat_Arr) return Natural is
      max_calories: Natural := 0;
   begin
      for calories of calories_arr loop
         max_calories := Natural'Max(max_calories, calories);
      end loop;
      return max_calories;
   end Find_Max_Calories;

end Calories;
