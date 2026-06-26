---
title: "Select the Midpoint of an Edge Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Put_a_Midpoint_on_an_Edge_Example_CSharp.htm"
---

# Select the Midpoint of an Edge Example (C#)

This example shows how to select the midpoint of an edge.

```vb
 //-------------------------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Select an edge.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Puts a midpoint on the selected edge.
 // 2. Place the cursor on the selected edge to see the
 //    midpoint.
 // 3. Examine the Immediate window.
 //------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace PlaceMidPointOnEdge_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         const long swSelEDGES = 1;
         const long swSelREFERENCECURVES = 26;
         const long swSelPOINTREFS = 41;
         const long swSelREFEDGES = 51;

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             PartDoc swPart = default(PartDoc);
             SelectionMgr swSelMgr = default(SelectionMgr);
             long nSelType = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swPart = (PartDoc)swModel;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             nSelType = swSelMgr.GetSelectedObjectType3(1, -1);
             Debug.Print("SelType (before) = " + nSelType);

             swModel.SelectMidpoint();

             nSelType = swSelMgr.GetSelectedObjectType3(1, -1);
             Debug.Print("SelType (after ) = " + nSelType);

         }

         public SldWorks swApp;

     }

 }
```
