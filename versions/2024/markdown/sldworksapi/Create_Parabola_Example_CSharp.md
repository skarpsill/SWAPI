---
title: "Create Parabola Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Parabola_Example_CSharp.htm"
---

# Create Parabola Example (C#)

This example shows how to create a parabola and get its corresponding equation.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Verify that the specified template exists.
 //
 // Postconditions:
 // 1. Inserts a sketch.
 // 2. Creates a parabola.
 // 3. Inspect the Immediate window for the parabolic equation.
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
 using System.Windows.Forms;
 namespace CreateParabola_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         const double pi = 3.14159265;

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);

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

             // Make sure the sketch has the necessary points
             if (vPoint.GetUpperBound(0) <= 2)
             {
                 MessageBox.Show("                            You did not sketch enough points to define the parabola. Please sketch a focal point, apex point, start point, and end point.");
                 return;
             }

             SketchParabola SkParabola = default(SketchParabola);
             SkParabola = (SketchParabola)swModel.SketchManager.CreateParabola(pFocal.X, pFocal.Y, 0, pApex.X, pApex.Y, 0, pStart.X, pStart.Y, 0, pEnd.X,
             pEnd.Y, 0);

             swModel.ViewZoomtofit2();

             //Extract information about the parabola
             pApex = (SketchPoint)SkParabola.GetApexPoint2();
             pStart = (SketchPoint)SkParabola.GetStartPoint2();
             pEnd = (SketchPoint)SkParabola.GetEndPoint2();
             pFocal = (SketchPoint)SkParabola.GetFocalPoint2();

             Debug.Print("      Apex  Point   = (" + pApex.X * 1000 +  ", " + pApex.Y * 1000 + ", " + pApex.Z * 1000 + ") mm");
             Debug.Print("      Start Point   = (" + pStart.X * 1000 + ", " + pStart.Y * 1000 + ", " + pStart.Z * 1000 + ") mm");
             Debug.Print("      End Point   = (" + pEnd.X * 1000 + ", " + pEnd.Y * 1000 + ", " + pEnd.Z * 1000 + ") mm");
             Debug.Print("      Focal Point   = (" + pFocal.X * 1000 + ", " + pFocal.Y * 1000 + ", " + pFocal.Z * 1000 + ") mm");

             // Define point parameters
             if (!(pFocal.Z == 0) | !(pApex.Z == 0) | !(pStart.Z == 0) | !(pEnd.Z == 0))
             {
                 MessageBox.Show("Need a 2D sketch.");
                 return;
             }

             // Algebraic equation of parabola
             double h = 0;
             double p = 0;
             double k = 0;

             h = pApex.X;
             k = pApex.Y;

             // Correct anomalies when the parabola is aligned with the x and y axes
             if (pFocal.Y == pApex.Y)
             {
                 if (pFocal.X > pApex.X)
                 {
                     p = Math.Sqrt(Math.Pow((pFocal.Y - pApex.Y), 2) + Math.Pow((pFocal.X - pApex.X), 2));
                 }
                 else
                 {
                     p = -(Math.Sqrt(Math.Pow((pFocal.Y - pApex.Y), 2) + Math.Pow((pFocal.X - pApex.X), 2)));
                 }
             }

             if (pFocal.X == pApex.X)
             {
                 if (pFocal.Y > pApex.Y)
                 {
                     p = Math.Sqrt(Math.Pow((pFocal.Y - pApex.Y), 2) + Math.Pow((pFocal.X - pApex.X), 2));
                 }
                 else
                 {
                     p = -(Math.Sqrt(Math.Pow((pFocal.Y - pApex.Y), 2) + Math.Pow((pFocal.X - pApex.X), 2)));
                 }
             }

             if (pFocal.X != pApex.X & pFocal.Y != pApex.Y)
             {
                 p = (Math.Sqrt(Math.Pow((pFocal.Y - pApex.Y), 2) + Math.Pow((pFocal.X - pApex.X), 2)));
             }

             double a = 0;
             double b = 0;
             double c = 0;
             double c1 = 0;
             double c2 = 0;
             double c3 = 0;
             double c4 = 0;
             double c5 = 0;
             double c6 = 0;
             double theta = 0;

             // Obtain the correct value for theta as the parabola rotates
             if (pFocal.X != pApex.X & pFocal.Y != pApex.Y)
             {
                 a = 1 / (4 * p);
                 b = -k / (2 * p);
                 c = (k * k / (4 * p)) + h;

                 // Theta in first quadrant
                 if (pFocal.Y > pApex.Y & pFocal.X > pApex.X)
                 {
                     theta = Math.Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X));
                 }

                 // Theta in second quadrant
                 if (pFocal.Y > pApex.Y & pFocal.X < pApex.X)
                 {
                     theta = (Math.Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X))) + pi;
                 }

                 // Theta in the third quadrant
                 if (pFocal.Y < pApex.Y & pFocal.X < pApex.X)
                 {
                     theta = (Math.Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X))) + pi;
                 }

                 // Theta in the fourth quadrant
                 if (pFocal.Y < pApex.Y & pFocal.X > pApex.X)
                 {
                     theta = (Math.Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X))) + (2 * pi);
                 }

                 c1 = Math.Round(a * Math.Pow((Math.Sin(theta)), 2), 2);
                 c2 = Math.Round(-a * Math.Sin(2 * theta), 2);
                 c3 = Math.Round(a * Math.Pow((Math.Cos(theta)), 2), 2);
                 c4 = Math.Round((-b * Math.Sin(theta)) - Math.Cos(theta), 2);
                 c5 = Math.Round((b * Math.Cos(theta)) - Math.Sin(theta), 2);
                 c6 = Math.Round(c, 2);

                 Debug.Print("Equation of the parabola: " + c1 +  "x^2 + " + c2 + "xy + " + c3 + "y^2 + " + c4 + "x + " + c5 + "y + " + c6 + " = 0");

             }

             // If the parabola has a vertical axis of symmetry
             if (pFocal.X == pApex.X)
             {
                 a = 1 / (4 * p);
                 b = -h / (2 * p);
                 c = (Math.Pow(h, 2) / (4 * p)) + k;
                 c1 = Math.Round(a, 2);
                 c4 = Math.Round(b, 2);
                 c6 = Math.Round(c, 2);
                 Debug.Print("Equation of the parabola: y = " + c1 +  "x^2 + " + c4 + "x + " + c6);
             }

             // If the parabola has a horizontal axis of symmetry
             if (pFocal.Y == pApex.Y)
             {
                 a = 1 / (4 * p);
                 b = -k / (2 * p);
                 c = (k * k / (4 * p)) + h;
                 c3 = Math.Round(a, 2);
                 c5 = Math.Round(b, 2);
                 c6 = Math.Round(c, 2);
                 Debug.Print("Equation of the parabola: x =" + c3 +  "y^2 + " + c5 + "y + " + c6);
             }

             swSkMgr.InsertSketch(true);

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
