---
title: "Get Area Hatch Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Area_Hatch_Data_Example_CSharp.htm"
---

# Get Area Hatch Data Example (C#)

This example shows how to get the data for an area hatch in a drawing.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified drawing exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the drawing.
 // 2. Hatches a face in the drawing.
 // 3. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
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
 namespace Macro1CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         DrawingDoc swDraw;
         SelectionMgr swSelMgr;
         View swView;
         Sketch swSketch;
         object[] vSketchHatch;
         SketchHatch swSketchHatch;
         Face2 swFace;
         int[] vID;
         int i;
         bool bRet;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.slddrw", (int)swDocumentTypes_e.swDocDRAWING, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("box - Sheet1", false, ref longstatus);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;

             bRet = swDraw.ActivateView("Drawing View1");

             bRet = swModel.Extension.SelectByID2("", "FACE", 0.246685509728212, 0.236217308689246, 0.0149999999999864, true, 0, null, 0);
             swModel.InsertHatchedFace();
             swModel.ClearSelection2(true);

             bRet = swModel.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);

             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swView = (View)swSelMgr.GetSelectedObject6(1, -1);
             swView.ScaleHatchPattern = true;
             swSketch = (Sketch)swView.GetSketch();
             swModel.EditSketch();

             swModel.ClearSelection2(true);

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  " + swView.Name);

             vSketchHatch = (object[])swSketch.GetSketchHatches();

             if ((vSketchHatch != null))
             {

                 for (i = 0; i <= vSketchHatch.GetUpperBound(0); i++)
                 {
                     swSketchHatch = (SketchHatch)vSketchHatch[i];
                     swFace = (Face2)swSketchHatch.GetFace();

                     bRet = swSketchHatch.Select4(true, null);
                     vID = (int[])swSketchHatch.GetID();

                     Debug.Print("    HatchID(" + i + "): [" + vID[0] + "," + vID[1] + "]");
                     Debug.Print("      Angle: " + swSketchHatch.Angle);
                     Debug.Print("      Color: " + swSketchHatch.Color);
                     Debug.Print("      Layer: " + swSketchHatch.Layer);
                     Debug.Print("      Layer override? " + swSketchHatch.LayerOverride);
                     Debug.Print("      Pattern: " + swSketchHatch.Pattern);
                     Debug.Print("      Scale: " + swSketchHatch.Scale2);
                     Debug.Print("      Solid fill? " + swSketchHatch.SolidFill);

                 }

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
