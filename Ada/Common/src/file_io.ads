with Ada.Text_IO, Array_Stuff;
use Ada.Text_IO, Array_Stuff;

package File_IO with SPARK_Mode is
   function Read_File(filename: in String:="input.txt") return Str_Arr;
end File_IO;
