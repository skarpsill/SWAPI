---
title: "Insert Weld Symbol Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weld_Symbol_Example_CSharp.htm"
---

# Insert Weld Symbol Example (C#)

This example shows how to insert a weld symbol into a model.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
  // 2. Select a face, edge, or sketch segment for Weld Symbol insertion.
 // 3. Open an Immediate window.
 //
 // Postconditions:
 // 1. Inserts the specified ISO Weld Symbol.
 // 2. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace InsertWeldSymbol_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             WeldSymbol swWeldSymbol = default(WeldSymbol);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swWeldSymbol = (WeldSymbol)swModel.InsertWeldSymbol3();

             swWeldSymbol.SetFieldWeld((int)swWeldSymbolField_e.swFieldWeldNone);
             swWeldSymbol.SetPeripheral(false);
             swWeldSymbol.SetProcess(true, "Process", true);
             swWeldSymbol.SetStagger(true);
             swWeldSymbol.SetSymmetric((int)swWeldSymbolSymmetric_e.swWeldSymmetric);
             swWeldSymbol.SetText(true, "Left", "BUTT", "Right", "Stagger", (int)swWeldSymbolContourTypes_e.swWeldContourNone);

             Debug.Print("Arc count: " + swWeldSymbol.GetArcCount());
             Debug.Print("Arrow head count: " + swWeldSymbol.GetArrowHeadCount());
             Debug.Print("Contour setting as defined in swWeldSymbolContourTypes_e: " + swWeldSymbol.GetContour(true));
             Debug.Print("Field weld setting as defined in swWeldSymbolField_e: " + swWeldSymbol.GetFieldWeld());
             Debug.Print("Number of leaders on this weld symbol: " + swWeldSymbol.GetLeaderCount());
             Debug.Print("Number of line segments in this weld symbol: " + swWeldSymbol.GetLineCount());
             Debug.Print("Weld all around the contour? " + swWeldSymbol.GetPeripheral());
             Debug.Print("Welding process indicated? " + swWeldSymbol.GetProcess());
             Debug.Print("Reference box around the specification process text? " + swWeldSymbol.GetProcessReference());
             Debug.Print("Stagger symbols above and below the line? " + swWeldSymbol.GetStagger());
             Debug.Print("Weld symbol symmetry as defined in swWeldSymbolSymmetric_e: " + swWeldSymbol.GetSymmetric());
             Debug.Print("Number of text items in this weld symbol: " + swWeldSymbol.GetTextCount());
             Debug.Print("Number of triangles in this weld symbol: " + swWeldSymbol.GetTriangleCount());
             Debug.Print("Extra leader line? " + swWeldSymbol.HasExtraLeader());
             Debug.Print("Weld symbol is attached to a leaderline? " + swWeldSymbol.IsAttached());

         }

         public SldWorks swApp;

     }
 }
```
