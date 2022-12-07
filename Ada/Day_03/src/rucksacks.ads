with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

package Rucksacks with SPARK_Mode is
   Group_Size : constant := 3;
   Max_Rucksacks : constant := 500;
   Max_Items : constant := 52;
      
   subtype Rucksack_Idx_T is Positive range 1..Max_Rucksacks;
   type Base_Value_T is range 0..Max_Items*Max_Rucksacks;
   subtype Item_Value_T is Base_Value_T range 0..Max_Items;
      
   subtype Rucksack_T is Unbounded_String;
   subtype Item_T is Character;
   type Item_Arr is array (Rucksack_Idx_T range <>) of Item_T;
   type Rucksack_Arr is array (Rucksack_Idx_T range <>) of Rucksack_T;
   subtype Rucksack_Group is Rucksack_Arr(1..Group_Size);
   
   function Get_Value(Item: Item_T) return Item_Value_T;
   function Find_Poorly_Sorted_Item(Rucksack: Rucksack_T) return Item_T with
     Pre => Length(Rucksack) >= 2;
   function Find_Common_Item(Rucksacks: Rucksack_Group) return Item_T;
   function Star_1(Rucksacks: Rucksack_Arr) return Base_Value_T with
     Pre => (for all Idx in Rucksacks'Range => Length(Rucksacks(Idx)) >= 2);
   function Calculate_Total_Value(Items: Item_Arr) return Base_Value_T;
private
   ASCII_Val_Upper_Offset : constant := 38;
   ASCII_Val_Lower_Offset : constant := 96;
   subtype ASCII_Upper_Vals is Natural range 65..90;
   subtype ASCII_Lower_Vals is Natural range 97..122;
end Rucksacks;
