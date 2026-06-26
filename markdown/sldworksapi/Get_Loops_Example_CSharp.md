---
title: "Get Loops Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loops_Example_CSharp.htm"
---

# Get Loops Example (C#)

This example shows how to get loop data for the selected face.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Model document is open, and a face is selected.
 //
 // Postconditions: Inspect the Immediate window.
 //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace GetLoopEdgeCount_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Face2 swFace = default(Face2);
             Loop2 swLoop = default(Loop2);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             swLoop = (Loop2)swFace.GetFirstLoop();

             Debug.Print("LoopCount = " + swFace.GetLoopCount());

             while ((swLoop != null))
             {
                 Debug.Print("  IsOuter      = " + swLoop.IsOuter());
                 Debug.Print("  IsSingular   = " + swLoop.IsSingular());
                 Debug.Print("  EdgeCount    = " + swLoop.GetEdgeCount());
                 Debug.Print("  VertexCount  = " + swLoop.GetVertexCount());
                 Debug.Print("");

                 swLoop = (Loop2)swLoop.GetNext();
             }

         }

         public SldWorks swApp;

     }
 }
```
