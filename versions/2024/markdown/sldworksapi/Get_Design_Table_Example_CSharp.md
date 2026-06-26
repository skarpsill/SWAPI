---
title: "Get Design Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Design_Table_Example_CSharp.htm"
---

# Get Design Table Example (C#)

```vb
This example shows how to get a design table and its contents.
//---------------------------------------
 // Preconditions:
 // 1. Open a part or assembly document that
 //    contains a design table.
 // 2. Verify that a design table exists by
 //    expanding Tables in the ConfigurationManager.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Prints the design table contents to the
 //    Immediate window.
 // 2. Examine the Immediate window.
 //----------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace GetTitleDesignTableCSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DesignTable swDesTable = default(DesignTable);
             int nTotRow = 0;
             int nTotCol = 0;
             string sRowStr = null;
             int i = 0;
             int j = 0;
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;

             swDesTable = (DesignTable)swModel.GetDesignTable();
             bRet = swDesTable.Attach();

             nTotRow = swDesTable.GetTotalRowCount();
             nTotCol = swDesTable.GetTotalColumnCount();
             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  Title        = " + swDesTable.GetTitle());
             Debug.Print("  Row          = " + swDesTable.GetRowCount());
             Debug.Print("  Col          = " + swDesTable.GetColumnCount());
             Debug.Print("  TotRow       = " + nTotRow);
             Debug.Print("  TotCol       = " + nTotCol);
             Debug.Print("  VisRow       = " + swDesTable.GetVisibleRowCount());
             Debug.Print("  VisCol       = " + swDesTable.GetVisibleColumnCount());
             Debug.Print("");

             for (i = 0; i <= nTotRow; i++)
             {
                 sRowStr = "  |";
                 for (j = 0; j <= nTotCol; j++)
                 {
                     sRowStr = sRowStr + swDesTable.GetEntryText(i, j) + "|";
                 }
                 Debug.Print(sRowStr);
             }
             swDesTable.Detach();
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
