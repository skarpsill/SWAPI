---
title: "Translate Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Translate_Sketch_Example_CSharp.htm"
---

# Translate Sketch Example (C#)

This example shows how to move a sketch.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Verify that the specified template exists.
 '
 ' Postconditions:
 ' 1. Creates a sketch.
 ' 2. Creates a parabola.
 ' 3. While observing the graphics area, press F5 at
 '    System.Diagnostics.Debugger.Break   to move the sketch.
 '----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 namespace TranslateSketch_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2017\\templates\\Part.prtdot", 0, 0, 0);

             if (swModel == null)
             {
                 swApp.SendMsgToUser2("A part document must be active.", (int)swMessageBoxIcon_e.swMbWarning, (int)swMessageBoxBtn_e.swMbOk);
                 return;
             }

             int modelType = 0;
             modelType = swModel.GetType();

             if (modelType != (int)swDocumentTypes_e.swDocPART)
             {
                 swApp.SendMsgToUser2("A part document must be active.", (int)swMessageBoxIcon_e.swMbWarning, (int)swMessageBoxBtn_e.swMbOk);
                 return;
             }

             //Select a plane on which to sketch
             if (SelectPlane(swModel) == false)
             {
                 MessageBox.Show("Could not select plane.");
                 return;
             }

             //Get point data
             SketchPoint pFocal = default(SketchPoint);
             SketchPoint pApex = default(SketchPoint);
             SketchPoint pStart = default(SketchPoint);
             SketchPoint pEnd = default(SketchPoint);
             SketchManager swSkMgr = default(SketchManager);
             swSkMgr = swModel.SketchManager;

             SelectionMgr swSelMgr = default(SelectionMgr);
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             Sketch swSketch = default(Sketch);
             swSkMgr.InsertSketch(true);
             swSketch = swSkMgr.ActiveSketch;

             // Focal point
             pFocal = swSkMgr.CreatePoint(0, -0.025930732990048, 0);
             // Apex point
             pApex = swSkMgr.CreatePoint(0.0110754938634727, -0.0485199777778575, 0);
             // Start point
             pStart = swSkMgr.CreatePoint(0.057136404168939, 0.0869770346454566, 0);
             // End point
             pEnd = swSkMgr.CreatePoint(-0.120690397734139, -0.00465528735997846, 0);

             object[] vPoint = null;

             // Make sure a sketch is active
             if (swSketch == null)
             {
                 MessageBox.Show("Please sketch a focal point, apex point, start point, and end point.");
                 return;
             }

             vPoint = (object[])swSketch.GetSketchPoints2();

             SketchParabola SkParabola = default(SketchParabola);
             SkParabola = (SketchParabola)swModel.SketchManager.CreateParabola(pFocal.X, pFocal.Y, 0, pApex.X, pApex.Y, 0, pStart.X, pStart.Y, 0, pEnd.X,
             pEnd.Y, 0);

             swModel.ViewZoomtofit2();
             swSkMgr.InsertSketch(true);

             System.Diagnostics.Debugger.Break();

             swModel.SketchModifyTranslate(pApex.X, pApex.Y, 0.06, -0.01);

         }

         public bool SelectPlane(ModelDoc2 Plane)
         {
             bool functionReturnValue = false;

             Feature featureTemp = default(Feature);
             featureTemp = (Feature)Plane.FirstFeature();

             while ((featureTemp != null))
             {
                 string sFeatureName = null;
                 sFeatureName = featureTemp.GetTypeName2();

                 if (sFeatureName == "RefPlane")
                 {
                     featureTemp.Select2(true, 0);
                     functionReturnValue =  true;
                     return functionReturnValue;
                 }

                 featureTemp = (Feature)featureTemp.GetNextFeature();

             }
             return functionReturnValue;

         }

         public SldWorks swApp;

     }
 }
```
