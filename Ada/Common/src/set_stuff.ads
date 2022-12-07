with Ada.Containers.Formal_Hashed_Sets; use Ada.Containers;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

package Set_Stuff is
   
   -- Char Set
   function Char_Hash(Char: Character) return Hash_Type is (Hash_Type(Character'Pos(Char)));
   package Char_Hash_Sets is new Formal_Hashed_Sets(Element_Type => Character, Hash => Char_Hash);
   function To_Char_Set(Str: String; Capacity: Count_Type) return Char_Hash_Sets.Set;
   function To_Char_Set(Str: Unbounded_String; Capacity: Count_Type) return Char_Hash_Sets.Set is
     (To_Char_Set(To_String(Str), Capacity));

end Set_Stuff;
