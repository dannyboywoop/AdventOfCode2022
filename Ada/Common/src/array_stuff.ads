with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

package Array_Stuff with
   SPARK_Mode
is

   type Int_Arr is array (Positive range <>) of Integer with
      Predicate => Int_Arr'First = 1 and Int_Arr'Last >= Int_Arr'First;
   type Pos_Arr is array (Positive range <>) of Positive with
      Predicate => Pos_Arr'First = 1 and Pos_Arr'Last >= Pos_Arr'First;
   type Nat_Arr is array (Positive range <>) of Natural with
      Predicate => Nat_Arr'First = 1 and Nat_Arr'Last >= Nat_Arr'First;
   type Str_Arr is array (Positive range <>) of Unbounded_String with
      Predicate => Str_Arr'First = 1 and Str_Arr'Last >= Str_Arr'First;
   function Str_To_Int_Array (strings : Str_Arr) return Int_Arr;

   generic
      type T is private;
      with function Transform (X : T) return T;
      type T_Arr is array (Positive range <>) of T;
   function Transform_Elements (input : T_Arr) return T_Arr;

   generic
      type T is private;
      type T_Arr is array (Positive range <>) of T;
      with function "+" (X, Y : T) return T is <>;
   function Sum_Elements (input : T_Arr; zero : T) return T;

end Array_Stuff;
