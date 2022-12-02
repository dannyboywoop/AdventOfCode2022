with Ada.Strings.Unbounded, Array_Stuff;
use Ada.strings.Unbounded, Array_Stuff;

package body String_Stuff is
   
   function Split(input: Unbounded_String; delim: String) return Str_Arr is
      result: Str_Arr(1..Count(input, delim)+1);
      pointer: Natural:=1;
      delim_index: Natural:=Index(input, delim);
      count: Natural:=1;
   begin
      while count <= result'Length loop
         --if no delim found, set index to end of input
         if delim_index = 0 then
            delim_index := Length(input) + 1;
         end if;
         
         --record token
         result(count) := Unbounded_Slice(input, pointer, delim_index - 1);
         
         --iterate
         pointer := delim_index + delim'Length;
         delim_index:=Index(input, delim, From => pointer);
         count := count + 1;
         
      end loop;
         
      return result;
   end Split;

end String_Stuff;
