with Array_Stuff; use Array_Stuff;

package Calories with SPARK_Mode is

   function Count_Calories(calories: Str_Arr) return Nat_Arr;
   
   function Find_Max_Calories(calories_arr: Nat_Arr) return Natural;

end Calories;
