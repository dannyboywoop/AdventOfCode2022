package body Set_Stuff is

   function To_Char_Set(Str: String; Capacity: Count_Type) return Char_Hash_Sets.Set is
      Char_Set: Char_Hash_Sets.Set(Capacity => Capacity, Modulus => Char_Hash_Sets.Default_Modulus(Capacity));
   begin
      for Char of Str loop
         Char_Hash_Sets.Include (Container => Char_Set, New_Item => Char);
      end loop;
      return Char_Set;
   end To_Char_Set;

end Set_Stuff;
