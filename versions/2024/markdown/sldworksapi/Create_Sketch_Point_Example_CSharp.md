---
title: "Create a Sketch Point Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sketch_Point_Example_CSharp.htm"
---

# Create a Sketch Point Example (C#)

This example shows how to create a sketch point.

```vb
 //---------------------------------------------------------------------------
 // Preconditions: Verify that the specified part template exists.
 //
 // Postconditions:
  // 1. Opens a new part document and creates a sketch.
 // 2. Creates a sketch point in the sketch.
 // 3. Examine the graphics area.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CreateSketchPoint_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SketchManager swSkMgr = default(SketchManager);
             int longstatus = 0;
             bool boolstatus = false;

             swApp.ResetUntitledCount(0, 0, 0);
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2012\\templates\\Part.prtdot", 0, 0, 0);
             swApp.ActivateDoc2("Part1", false, ref longstatus);
             swModel = (ModelDoc2)swApp.ActiveDoc;

             swSkMgr = swModel.SketchManager;
             swSkMgr.InsertSketch(true);
             boolstatus = swModel.Extension.SelectByID2("Top Plane",  "PLANE", -0.0553489443349025, 0.00330468607538553, 0.0269617286188933,  false, 0,  null, 0);
             swModel.ClearSelection2(true);

             // Check whether document is active
             if (swModel == null)
             {
                 swApp.SendMsgToUser2("A part document must be active.", (int) swMessageBoxIcon_e.swMbWarning, (int) swMessageBoxBtn_e.swMbOk);
                 return;
             }

             // Check whether document is a part
             int modelType = 0;
             modelType = swModel.GetType();

             if (modelType != (int)swDocumentTypes_e.swDocPART)
             {
                 swApp.SendMsgToUser2("A part document must be active.", (int)swMessageBoxIcon_e.swMbWarning, (int)swMessageBoxBtn_e.swMbOk);
                 return;
             }

             SketchPoint skPoint = default(SketchPoint);
             skPoint = swSkMgr.CreatePoint(-0.127443, 0.042892, 0.0);
             swSkMgr.InsertSketch(true);

         }

         public SldWorks swApp;

     }
 }
```
