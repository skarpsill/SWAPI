---
title: "Get Break Line Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Break_Line_Data_Example_CSharp.htm"
---

# Get Break Line Data Example (C#)

This example shows how to get information on all break lines in a view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Create or open a drawing with one or more views that contain
 //    one or more break lines.
 // 2. Open an Immediate Window.
 //
 // Postconditions: Inspect the Immediate Window.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetBreakline_CSharp.csproj
 {
     partial class  SolidWorksMacro
     {

         DrawingDoc Draw;
         View swActiveView;
         int Size;
         int Breaks;
         object info;
         Double[] infoArray;

         public void Main()
         {
             Draw = (DrawingDoc)swApp.ActiveDoc;
             long count = 0;
             count = Draw.GetViewCount();
             Debug.Print("There are " + count +  " views in this drawing including the sheet view.");
             long i = 0;
             long j = 0;
             swActiveView = (View)Draw.GetFirstView();
             // get the sheet
             swActiveView = (View)swActiveView.GetNextView();
             // get the first view
             for (i = 0; i <= count - 2; i++)
             {
                 Debug.Print("View " + (i + 1));
                 Breaks = swActiveView.GetBreakLineCount2(out Size);
                 Debug.Print("   Number of breaks is " + Breaks);
                 Debug.Print("   Size of break line data array is " + Size);

                 if (!(Breaks == 0))
                 {
                     info = swActiveView.GetBreakLineInfo2();
                     infoArray = (Double[])info;

                     // General break line information
                     Debug.Print("   General break line info:");
                     Debug.Print("     Style as defined in swBreakLineStyle_e: " + infoArray[0]);
                     Debug.Print("     Color (0 or -1 for default color): " + infoArray[1]);
                     Debug.Print("     Line type as defined in swLineTypes_e: " + infoArray[2]);
                     Debug.Print("     Line style as defined in swLineStyles_e: " + infoArray[3]);
                     Debug.Print("     Line weight as defined in swLineWeights_e: " + infoArray[4]);
                     Debug.Print("     Layer id: " + infoArray[5]);
                     Debug.Print("     Layer override as defined in swLayerOverride_e: " + infoArray[6]);
                     Debug.Print("     Number of line segments: " + infoArray[7]);
                     Debug.Print("     Number of arcs: " + infoArray[8]);
                     Debug.Print("     Number of jagged lines: " + infoArray[9]);

                     // Straight, zigzag, arc, or jagged break line data
                     Debug.Print("");
                     Debug.Print("     Straight, zigzag, arc, or jagged break line data");

                     for (j = 10; j <= Size - 1; j++)
                     {
                         Debug.Print("      " + infoArray[j]);
                     }

                 }
                 swActiveView = (View)swActiveView.GetNextView();
             }

         }

         public SldWorks swApp;

     }
 }
```
