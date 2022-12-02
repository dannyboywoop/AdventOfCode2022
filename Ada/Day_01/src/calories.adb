with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

package body Calories with SPARK_Mode is

   function Count_Calories(calories: Str_Arr) return Nat_Arr is
      number_of_elves : Positive := 1;
   begin
      -- Count elves
      for cal_str of calories loop
         if Length(cal_str) = 0 then
            number_of_elves := @ + 1;
         end if;
      end loop;
      
      declare
         calories_arr_size: constant Positive := number_of_elves;
         calories_arr: Nat_Arr(1..calories_arr_size);
         cal_count: Natural:=0;
         idx: Positive:=1;
      begin
         for cal_str of calories loop
            if Length(cal_str) = 0 then
               calories_arr(idx) := cal_count;
               idx := @ + 1;
               cal_count := 0;
            else
               cal_count := @ + Integer'Value(To_String(cal_str));
            end if;
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
