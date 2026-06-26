---
title: "Get and Set Spline Handles Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Spline_Handles_Example_CSharp.htm"
---

# Get and Set Spline Handles Example (C#)

This example shows how to get and set the properties of spline handles in a 2D spline.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified document template exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates Sketch1 in the graphics area and FeatureManager design tree.
 // 2. Modifies some of the spline handles of Sketch1.
 // 3. Inspect the Immediate window.
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
 namespace GetSetSplineHandle_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         ModelDocExtension swModelDocExt;
         SketchSpline swSpline;
         SketchSegment skSegment;
         object[] objSplineHandle;
         SplineHandle swSplineHandle;
         bool boolstatus;

         int i;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swModelDocExt = swModel.Extension;

             object pointArray = null;
             double[] points = new double[18];
             points[0] = -0.0725658847190971;
             points[1] = -0.0284590725570979;
             points[2] = 0;
             points[3] = -0.0437940929359115;
             points[4] = 0.0215374317625674;
             points[5] = 0;
             points[6] = -0.0245140262770747;
             points[7] = -0.026920232075895;
             points[8] = 0;
             points[9] = 0.0273938454967038;
             points[10] = -0.0414386885537397;
             points[11] = 0;
             points[12] = 0.0413348167730874;
             points[13] = 0.0386761654855832;
             points[14] = 0;
             points[15] = 0.101251331620574;
             points[16] = 0.0438481259864147;
             points[17] = 0;
             pointArray = points;

             skSegment = swModel.SketchManager.CreateSpline((pointArray));
             swModel.SketchManager.InsertSketch(true);

             boolstatus = swModelDocExt.SelectByID2("Spline1@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
             swSpline = (SketchSpline)swSelMgr.GetSelectedObject6(1, 0);

             // Get the handles on the spline
             objSplineHandle = (object[])swSpline.GetSplineHandles();

             for (i = 0; i <= objSplineHandle.GetUpperBound(0); i++)
             {
                 swSplineHandle = (SplineHandle)objSplineHandle[i];
                 Debug.Print("Spline handle " + swSplineHandle.SplinePointNumber);
                 Debug.Print(" X: " + swSplineHandle.X * 1000);
                 Debug.Print(" Y: " + swSplineHandle.Y * 1000);
                 Debug.Print(" Z: " + swSplineHandle.Z * 1000);

                 if ((i == 0))
                 {
                     swSplineHandle.X = -62.33246528 / 1000;
                     swSplineHandle.Y = -14.71944444 / 1000;

                 }

                 Debug.Print(" Tangent magnitude: " + swSplineHandle.get_TangentMagnitude((int)swTangentMagnitudeDirection_e.swTangentMagnitudeDirection1));
                 Debug.Print(" Tangent radial direction: " + swSplineHandle.TangentRadialDirection);

                 if ((i == 2))
                 {
                     swSplineHandle.set_TangentMagnitude((int)swTangentMagnitudeDirection_e.swTangentMagnitudeDirection1, swSplineHandle.get_TangentMagnitude((int)swTangentMagnitudeDirection_e.swTangentMagnitudeDirection1) + 0.02);
                     swSplineHandle.TangentRadialDirection = swSplineHandle.TangentRadialDirection + 0.5;

                 }

                 Debug.Print(" Curvature: " + swSplineHandle.Curvature);
                 Debug.Print(" Radius of curvature: " + swSplineHandle.RadiusOfCurvature);

                 if ((i == 3))
                 {
                     swSplineHandle.RadiusOfCurvature = swSplineHandle.RadiusOfCurvature / 2;

                 }

                 if ((i == 3))
                 {
                     Debug.Print(" Tangent driving? " + swSplineHandle.TangentDriving);

                     if ((swSplineHandle.TangentDriving))
                     {
                         swSplineHandle.TangentDriving = false;
                     }
                     else
                     {
                         swSplineHandle.TangentDriving = true;
                     }

                     swSplineHandle.Reset();

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
