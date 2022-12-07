with Set_Stuff; use Set_Stuff;
with Ada.Containers; use Ada.Containers;

package body Rucksacks with SPARK_Mode is
   use Char_Hash_Sets;   

   function Get_Value(Item: Item_T) return Item_Value_T is
      ASCII_Val : Natural := Item_T'Pos(Item);
   begin
      case ASCII_Val is
         when ASCII_Upper_Vals'Range => return Item_Value_T(ASCII_Val - ASCII_Val_Upper_Offset);
         when ASCII_Lower_Vals'Range => return Item_Value_T(ASCII_Val - ASCII_Val_Lower_Offset);
         when others => return Item_Value_T'First;
      end case;
   end;
   
   
   function Find_Poorly_Sorted_Item(Rucksack: Rucksack_T) return Item_T is
      Midpoint : Positive := Length(Rucksack) / 2;
      First_Half: Set := To_Char_Set(Slice(Rucksack, Positive'First, Midpoint), Max_Items);
      Second_Half: Set := To_Char_Set(Slice(Rucksack, Midpoint + 1, Length(Rucksack)), Max_Items);
      Intersect: Set := First_Half and Second_Half;
   begin
      if Length(Intersect) = 1 then
         return Element(Intersect, First(Intersect));
      end if;
      return ' '; -- null character
   end;
   
   function Find_Common_Item(Rucksacks: Rucksack_Group) return Item_T is
      Common_Items: Set := To_Char_Set(Rucksacks(Rucksacks'First), Max_Items);
   begin
      for Idx in Rucksacks'First + 1 .. Rucksacks'Last loop
         Intersection(Common_Items, To_Char_Set(Rucksacks(Idx), Max_Items));
      end loop;
      
      if Length(Common_Items) = 1 then
         return Element(Common_Items, First(Common_Items));
      end if;
      return ' '; -- null character
   end;
   
   function Calculate_Total_Value(Items: Item_Arr) return Base_Value_T is
      Total : Base_Value_T := 0;
   begin
      for Idx in Items'Range loop
         Total := @ + Get_Value(Items(Idx));
         pragma Loop_Invariant(Total <= Base_Value_T(Idx) * Item_Value_T'Last);
      end loop;
      return Total;
   end;
   
   function Star_1(Rucksacks: Rucksack_Arr) return Base_Value_T is
      Poorly_Sorted_Items: Item_Arr(Rucksacks'Range);
   begin
      for Idx in Poorly_Sorted_Items'Range loop
         Poorly_Sorted_Items(Idx) := Find_Poorly_Sorted_Item(Rucksacks(Idx));
      end loop;
      return Calculate_Total_Value(Poorly_Sorted_Items);
   end;
     
end Rucksacks;
