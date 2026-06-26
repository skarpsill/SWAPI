---
title: "Flip Sketch Picture Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Flip_Sketch_Picture_Example_CSharp.htm"
---

# Flip Sketch Picture Example (C#)

This example shows how to flip a sketch picture.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified document template exists.
 // 2. Copy an image file (i.e., .bmp, .gif, .jpg, .jpeg, .tif, .wmf) to
 //    c:\temp.
 // 3. Replace image_file in the ISketchManager::InsertSketchPicture parameter
 //    with the name of the copied file.
 // 4. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a new model document.
 // 2. Creates Sketch1 and Sketch Picture1 in the graphics area and the
 //    FeatureManager design tree.
 // 3. Selects Sketch Picture1 and flips it top to bottom.
 // 4. Inspect the Immediate window.
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

 namespace FlipSketchPicture_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         Feature swFeat;
         SketchPicture swSketchPicture;
         SelectionMgr swSelMgr;
         bool boolstatus;
         double width;
         double height;
         double angle;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2020\\templates\\Part.prtdot", 0, 0, 0);
             swModel = (ModelDoc2)swApp.ActiveDoc;

             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swModel.SketchManager.InsertSketch(true);
             swSketchPicture = swModel.SketchManager.InsertSketchPicture2("c:\\temp\\image_file", false);
             swModel.SketchManager.InsertSketch(true);

             boolstatus = swModel.Extension.SelectByID2("Sketch Picture1", "SKETCHBITMAP", 0, 0, 0, false, 0, null, 0);
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

             Debug.Print("Feature name = " + swFeat.Name);

             boolstatus = swSketchPicture.Flip(false);
             Debug.Print("  Sketch picture flipped? " + swSketchPicture.Flipped);

             swSketchPicture.GetSize(ref width, ref height);
             Debug.Print("  Width: " + width * 1000 + " mm");
             Debug.Print("  Height: " + height * 1000 + " mm");

             angle = swSketchPicture.Angle;
             //1 radian = 180º/p = 57.295779513º or approximately 57.3º
             Debug.Print("  Angle: " + angle * 57.3 + " degrees");

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
