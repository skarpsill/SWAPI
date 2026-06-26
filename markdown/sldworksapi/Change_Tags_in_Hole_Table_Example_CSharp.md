---
title: "Change Tags in Hole Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Tags_in_Hole_Table_Example_CSharp.htm"
---

# Change Tags in Hole Table Example (C#)

This example shows how to change the tags in a hole table.

```
//-----------------------------------------------------
// Preconditions:
// 1. Open a drawing document that contains
//    a hole table named Hole Table1 that has
//    has four columns (TAG, X LOC, Y LOC, and SIZE)
//    and at least five rows.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Disables updating hole table tags.
// 2. Changes tag in column 1, row 2 to Test1.
// 3. Changes tag in column 1, row 5 to Test2.
// 4. Enables updating of hole table and model view
//    and shows new tags.
// 5. Examine the Immediate window and hole table.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace RenameHoleTableTag_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial
 class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public
 void Main()
```

```
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}HoleTable swHoleTable = default(HoleTable);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModel.Extension.SelectByID2("Hole Table1", "HOLETABLE",
 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTable = (HoleTable)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTable.EnableUpdate = false;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Disable
 updating hole table tags
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Original name of tag in column1, row 2: " + swHoleTable.get_HoleTag(1));

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTable.set_HoleTag(1, "Test1");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("New name of tag in column1, row 2: " + swHoleTable.get_HoleTag(1));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Original name of tag in column1, row 5: " + swHoleTable.get_HoleTag(4));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTable.set_HoleTag(4, "Test1");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//
 Fails because same name is used in row 2
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTable.set_HoleTag(4, "Test2");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("New name of tag in column1, row 2: " + swHoleTable.get_HoleTag(4));

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Enable
 updating hole table tags
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTable.EnableUpdate = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
