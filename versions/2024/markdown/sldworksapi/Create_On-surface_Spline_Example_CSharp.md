---
title: "Create On-surface Spline Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_On-surface_Spline_Example_CSharp.htm"
---

# Create On-surface Spline Example (C#)

This example shows how to create a spline constrained to a surface.

```vb
  //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 //
 // Postconditions:
 // 1. Creates a 3D sketch of a spline on a face.
 // 2. Inspect the graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace CreateSurfSpline_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {

             Face2 swCurFace = default(Face2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             ModelDoc2 Part = default(ModelDoc2);
             SketchSegment skSegment = default(SketchSegment);
             object pointArray = null;
             double[] points = new double[12];
             object[] surfs = new object[1];
             Surface[] surfaceArr = new Surface[1];
             int selType = 0;
             int surfaceArrUbound = 0;
             object statuses = null;
             bool boolstatus = false;

             Part = (ModelDoc2)swApp.ActiveDoc;

             points[0] = -0.0334270787209949;
             points[1] = 0.0223913424029847;
             points[2] = 0.053671471463652;
             points[3] = 0.0153063989576147;
             points[4] = 0.0478899892864157;
             points[5] = 0.0250019220828396;
             points[6] = 0.0511644715447442;
             points[7] = 0.0272060072570875;
             points[8] = 0.00578476387745854;
             points[9] = 0.00259263831071606;
             points[10] = 0.0262831648993199;
             points[11] = -0.053206707614433;
             pointArray = points;

             boolstatus = Part.Extension.SelectByRay(0.030303902514845, 0.0286262382667246, 0.0385109058888133, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.00178932209693826, 2, false, 0,
             0);

             swSelMgr = (SelectionMgr)Part.SelectionManager;

             selType = swSelMgr.GetSelectedObjectType3(1, -1);
             surfaceArrUbound = -1;
             if (selType == (int)swSelectType_e.swSelFACES)
             {
                 swCurFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
                 surfaceArrUbound = surfaceArrUbound + 1;
                 surfaceArr[surfaceArrUbound] = (Surface)swCurFace.GetSurface();
             }

             surfs = surfaceArr;

             DispatchWrapper[] dispArray = null;
             dispArray = ObjectArrayToDispatchWrapperArray(surfaceArr);

             //Set the Direction parameter to an array of null DispatchWrappers
             //to use the view vector of the current view to project the points in pointArray
             //onto the surface in dispArray
             DispatchWrapper dirArray = default(DispatchWrapper);
             dirArray = new DispatchWrapper(null);

             skSegment = (SketchSegment)Part.SketchManager.CreateSpline3((pointArray), dispArray, dirArray, true, out statuses);
             Part.SketchManager.InsertSketch(true);
         }
         public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(Surface[] Objects)
         {
             int ArraySize = 0;
             ArraySize = Objects.GetUpperBound(0);
             DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];
             int ArrayIndex = 0;
             for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)
             {
                 d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);
             }
             return d;
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
