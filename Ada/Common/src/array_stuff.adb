package body Array_Stuff is

   function Str_To_Int_Array(strings: Str_Arr) return Int_Arr is
      integers : Int_Arr(strings'Range);
   begin
      for i in strings'Range loop
         integers(i):=Integer'Value(To_String(strings(i)));
      end loop;
      return integers;
   end Str_To_Int_Array;


   function Transform_Elements(input: T_Arr) return T_Arr is
      output : T_Arr(input'Range);
   begin
      for i in input'Range loop
         output(i) := Transform(input(i));
      end loop;
      return output;
   end Transform_Elements;


   function Sum_Elements(input: T_Arr; zero: T) return T is
      output: T:= zero;
   begin
      for item of input loop
         output := output + item;
      end loop;
      return output;
   end Sum_Elements;

end Array_Stuff;
