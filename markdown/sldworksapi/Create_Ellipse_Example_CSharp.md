---
title: "Create Ellipse Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ellipse_Example_CSharp.htm"
---

# Create Ellipse Example (C#)

This example shows how to create an ellipse circumscribing two sketch points.

```vb
 //---------------------------------------------------------------------------
 // Preconditions: Open a part document that contains
 // an active sketch that has two sketch points.
 //
 // Postconditions:
 // 1. Creates an ellipse circumscribing the two sketch points.
 // 2. Inspect Immediate window for ellipse point data, theta, and equation.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Windows.Forms;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CreateEllipse_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             MathUtility swMath = default(MathUtility);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swMath = (MathUtility)swApp.GetMathUtility();

             // Check whether document is active
             if (swModel == null)
             {
                 swApp.SendMsgToUser2("A part document must be active.", (int)swMessageBoxIcon_e.swMbWarning, (int)swMessageBoxBtn_e.swMbOk);
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

             // Select a plane on which to sketch
             if (SelectPlane(swModel) == false)
             {
                 MessageBox.Show("Could not select plane.");
                 return;
             }

             SketchManager swSkMgr = default(SketchManager);
             swSkMgr = swModel.SketchManager;

             Sketch swSketch = default(Sketch);
             swSketch = swSkMgr.ActiveSketch;

             // Check whether a sketch is active
             if (swSketch == null)
             {
                 MessageBox.Show("Please sketch a point for the center point, sketch another point to define the major axis, and run the macro again.");
                 return;
             }

             const double pi = 3.1415926;

             // Get data from the points
             SketchPoint CtrPt = null;
             SketchPoint MajPt = null;

             swSkMgr = swModel.SketchManager;
             swSketch = swSkMgr.ActiveSketch;

             object[] vPoint = null;

             int i = 0;

             // Make sure the sketch is active
             if (swSketch == null)
             {
                 MessageBox.Show("Please place the sketch in edit mode and run the macro again.");
                 return;
             }

             // Make sure that at least two sketch points exist to define the position of the ellipse and its major axis
             vPoint = (Object[])swSketch.GetSketchPoints2();
             if (vPoint.GetUpperBound(0) == 0)
             {
                 MessageBox.Show("Please sketch a point for the center point, sketch another point to define the major axis, and run the macro again.");
                 return;
             }

             for (i = 0; i <= vPoint.GetUpperBound(0); i++)
             {
                 if (i == 0)
                 {
                     CtrPt = (SketchPoint)vPoint[i];
                 }

                 if (i == 1)
                 {
                     MajPt = (SketchPoint)vPoint[i];
                 }
             }

             MathVector MajVec = default(MathVector);
             double[] dirArr = new double[3];

             dirArr[0] = MajPt.X - CtrPt.X;
             dirArr[1] = MajPt.Y - CtrPt.Y;
             dirArr[2] = 0;

             MajVec = (MathVector)swMath.CreateVector((dirArr));
             MathVector MajVecunit = default(MathVector);

             MajVecunit = (MathVector)MajVec.Normalise();
             MathVector normVec = default(MathVector);

             dirArr[0] = 0;
             dirArr[1] = 0;
             dirArr[2] = 1;

             normVec = (MathVector)swMath.CreateVector((dirArr));

             MathVector MinVecunit = default(MathVector);
             MathVector MinVec = default(MathVector);
             double u = 0.0;

             MinVecunit = (MathVector)normVec.Cross(MajVecunit);

             double minlength = 50.0;
             u = minlength / 1000.0;

             MinVec = (MathVector)MinVecunit.Scale(u);

             // Ensure that the minor axis is less than the major axis so that
             // the equation returned is correct
             if (MajVec.GetLength() < MinVec.GetLength())
             {
                 MessageBox.Show("The length of the minor axis must be less than that of the major axis.");
                 return;
             }

             double[] pointvar;
             Object pointobj;
             pointobj = MinVec.ArrayData;
             pointvar = (Double[])pointobj;

             if (!(CtrPt.Z == 0) | !(MajPt.Z == 0) | !(pointvar[2] == 0))
             {
                 MessageBox.Show("Only 2D sketch is allowed.");
                 return;
             }

             // Sketch the ellipse
             SketchEllipse SkEllipse = default(SketchEllipse);
             SkEllipse = (SketchEllipse)swModel.SketchManager.CreateEllipse(CtrPt.X, CtrPt.Y, 0, MajPt.X, MajPt.Y, 0, CtrPt.X + pointvar[0], CtrPt.Y + pointvar[1], 0);

             swModel.ViewZoomtofit2();

             // Check that the sketch is an ellipse
             Object vEllipse = null;
             vEllipse = swSketch.GetEllipses3();

             if (swSketch.GetEllipseCount() == 0)
             {
                 MessageBox.Show("An ellipse was not created. Please make sure that the sketch contains two points.");
                 return;
             }

             // Extract information about the ellipse
             SketchPoint swStartPt = default(SketchPoint);
             SketchPoint swEndPt = default(SketchPoint);
             SketchPoint swCtrPt = default(SketchPoint);
             SketchPoint swMajPt = default(SketchPoint);
             SketchPoint swMinPt = default(SketchPoint);

             swStartPt = (SketchPoint)SkEllipse.GetStartPoint2();
             swEndPt = (SketchPoint)SkEllipse.GetEndPoint2();
             swCtrPt = (SketchPoint)SkEllipse.GetCenterPoint2();
             swMajPt = (SketchPoint)SkEllipse.GetMajorPoint2();
             swMinPt = (SketchPoint)SkEllipse.GetMinorPoint2();

             Debug.Print("Sketch points");
             Debug.Print("      Start Point   = (" + swStartPt.X * 1000.0 + ", " + swStartPt.Y * 1000.0 + ", " + swStartPt.Z * 1000.0 + ") mm");
             Debug.Print("      End Point     = (" + swEndPt.X * 1000.0 + ", " + swEndPt.Y * 1000.0 + ", " + swEndPt.Z * 1000.0 + ") mm");
             Debug.Print("      Center Point  = (" + swCtrPt.X * 1000.0 + ", " + swCtrPt.Y * 1000.0 + ", " + swCtrPt.Z * 1000.0 + ") mm");
             Debug.Print("      Major Point   = (" + swMajPt.X * 1000.0 + ", " + swMajPt.Y * 1000.0 + ", " + swMajPt.Z * 1000.0 + ") mm");
             Debug.Print("      Minor Point   = (" + swMinPt.X * 1000.0 + ", " + swMinPt.Y * 1000.0 + ", " + swMinPt.Z * 1000.0 + ") mm");

             // Algebraic equation for the ellipse
             double h = 0;
             double k = 0;
             double a = 0;
             double b = 0;
             double theta = 0;

             h = swCtrPt.X;
             k = swCtrPt.Y;
             a = 1 / (Math.Pow((swMajPt.X - swCtrPt.X), 2) + Math.Pow((swMajPt.Y - swCtrPt.Y), 2));
             b = 1 / (Math.Pow((swMinPt.X - swCtrPt.X), 2) + Math.Pow((swMinPt.Y - swCtrPt.Y), 2));

             // Return the tipping angle, theta; avoid divide by zero
             if (swMajPt.X != swCtrPt.X)
             {
                 theta = Math.Atan((swMajPt.Y - swCtrPt.Y) / (swMajPt.X - swCtrPt.X));
             }
             else
             {
                 theta = pi / 2;
             }

             Debug.Print("Theta of ellipse: " + theta);

             double c1 = 0;
             double c2 = 0;
             double c3 = 0;
             double c4 = 0;
             double c5 = 0;
             double c6 = 0;

             c1 = Math.Round((a * Math.Pow((Math.Cos(theta)), 2)) + (b * Math.Pow((Math.Sin(theta)), 2)), 2);
             c2 = Math.Round((a - b) * Math.Sin(2 * theta), 2);
             c3 = Math.Round((b * Math.Pow((Math.Cos(theta)), 2)) + (a * Math.Pow((Math.Sin(theta)), 2)), 2);
             c4 = Math.Round((-2 * a * h * Math.Cos(theta)) + (2 * b * k * Math.Sin(theta)), 2);
             c5 = Math.Round((-2 * a * h * Math.Sin(theta)) - (2 * b * k * Math.Cos(theta)), 2);
             c6 = Math.Round(1 - (b * (Math.Pow(k, 2))) - (a * (Math.Pow(h, 2))), 2);

             Debug.Print("Equation of the ellipse: " + c1 +  "x^2 + " + c2 + "xy + " + c3 + "y^2 + " + c4 + "x + " + c5 + "y = " + c6);

             // NOTE: The coefficients of x and y in this
             //       equation represent a translation in the x-y plane.
             //       If they are 0, then the ellipse was not translated.
             //       Similarly the coefficient of xy represents
             //       a rotation. If it is 0, then the ellipse
             //       was not rotated.
             //
             //       The units on each axis are in meters.

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
