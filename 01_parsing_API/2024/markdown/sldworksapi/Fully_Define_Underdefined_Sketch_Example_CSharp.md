---
title: "Fully Define Under Defined Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fully_Define_Underdefined_Sketch_Example_CSharp.htm"
---

# Fully Define Under Defined Sketch Example (C#)

This example shows how to fully define an under defined sketch.

```
//---------------------------------------------------------------------------
// Preconditions: Open a part document containing an under defined sketch.
//
// Postconditions:
// 1. Fully defines the under defined sketch.
// 2. Open the sketch to verify.
//---------------------------------------------------------------------------
```

```vb
using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace FullyDefineSketch_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             Feature swFeature = default(Feature);
             bool bValue = false;
             SketchManager swSketchManager = default(SketchManager);
             ModelDocExtension swModelExtension = default(ModelDocExtension);
             int lStatus = 0;
             int lMarkHorizontal = 0;
             int lMarkVertical = 0;
             SelectionMgr swSelectionManager = default(SelectionMgr);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelExtension = swModel.Extension;
             swSketchManager = swModel.SketchManager;
             swSelectionManager = (SelectionMgr)swModel.SelectionManager;

             swModel.ClearSelection2(true);

             // These are the marks expected for the dimension datums
             lMarkHorizontal = 2;
             lMarkVertical = 4;

             swFeature = (Feature)swModel.FirstFeature();

             while (((swFeature != null)))
             {
                 if ((swFeature.GetTypeName() == "ProfileFeature"))
                 {
                     break;
                 }
                 swFeature = (Feature)swFeature.GetNextFeature();
             }

             if (((swFeature != null)))
             {
                 bValue = swFeature.Select2(false, 0);
                 swSketchManager.InsertSketch(false);

                 // OR together the marks for the vertical and horizontal datums;
                 // You cannot select the same point twice with different marks
                 bValue = swModelExtension.SelectByID2("Point1@Origin", "EXTSKETCHPOINT", 0, 0, 0, false, lMarkHorizontal | lMarkVertical, null, 0);
                 lStatus = swSketchManager.FullyDefineSketch(true, true, (int)swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Vertical | (int)swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Horizontal, true, 1, null, 1, null, 1, 1);

                 swSketchManager.InsertSketch(true);
             }

         }

         public SldWorks swApp;
     }
 }
```
