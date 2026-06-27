---
title: "Create Trimmed Curve Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Return_Untrimmed_Curve_Example_CSharp.htm"
---

# Create Trimmed Curve Example (C#)

This example shows how to create a trimmed curve on a selected face.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part and select a face.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a trimmed curve.
 // 2. Inspect the Immediate window.
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
 namespace CreateTrimmedCurve_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
              SketchManager  swSketchMgr = default(SketchManager);
             Face2 swFace = default(Face2);
             Surface swSurf = default(Surface);
             double[] vFaceUV = null;
             SurfaceParameterizationData surfParam = default(SurfaceParameterizationData);
             Curve swCurveU = default(Curve);
             double[] vUIsoStartPt = null;
             double[] vUIsoEndPt = null;
             const double nChordTol = 0.001;
             const double nLengthTol = 0.001;
             double nStartParam = 0;
             double nEndParam = 0;
             bool bIsClosed = false;
             bool bIsPeriodic = false;
             double[] vStartPt = null;
             double[] vEndPt = null;
             double[] vTessPts = null;
             SketchSegment swSketchSeg = default(SketchSegment);
             int i = 0;
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             swSurf = (Surface)swFace.GetSurface();

             vFaceUV = (double[])swFace.GetUVBounds();
             surfParam = swSurf.Parameterization2();

             vUIsoStartPt = (double[])swSurf.Evaluate((vFaceUV[0] + vFaceUV[1]) / 2.0, vFaceUV[2], 0, 0);
             vUIsoEndPt = (double[])swSurf.Evaluate((vFaceUV[0] + vFaceUV[1]) / 2.0, vFaceUV[3], 0, 0);

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  Face:");
             Debug.Print("    uRange   = [" + vFaceUV[0] +  " , " + vFaceUV[1] + "]");
             Debug.Print("    vRange   = [" + vFaceUV[2] +  " , " + vFaceUV[3] + "]");
             Debug.Print("  Surface:");
             Debug.Print("    uRange   = [" + surfParam.UMin +  " , " + surfParam.UMax + "]");
             Debug.Print("    vRange   = [" + surfParam.VMin +  " , " + surfParam.VMax + "]");
             Debug.Print("  U Curve:");
             Debug.Print("    Start Pt = (" + vUIsoStartPt[0] * 1000 +  ", " + vUIsoStartPt[1] * 1000 + ", " + vUIsoStartPt[2] * 1000 + ") mm");
             Debug.Print("    End   Pt = (" + vUIsoEndPt[0] * 1000 +  ", " + vUIsoEndPt[1] * 1000 + ", " + vUIsoEndPt[2] * 1000 + ") mm");

             // Create untrimmed U curve
             double uvValue;
             uvValue = (vFaceUV[0] + vFaceUV[1]) / 2.0;
             swCurveU = swSurf.MakeIsoCurve2(false, ref uvValue);

             // Trim U curve to start and end of U range
             swCurveU = swCurveU.CreateTrimmedCurve2(vUIsoStartPt[0], vUIsoStartPt[1], vUIsoStartPt[2], vUIsoEndPt[0], vUIsoEndPt[1], vUIsoEndPt[2]);

             Debug.Print("  Trimmed U curve:");
             bRet = swCurveU.GetEndParams(out nStartParam, out nEndParam, out bIsClosed, out bIsPeriodic);
             Debug.Print("    Start parameter is " + nStartParam);
             Debug.Print("    End parameter is " + nEndParam);
             Debug.Print("    Is closed? " + bIsClosed);
             Debug.Print("    Is periodic? " + bIsPeriodic);

             vStartPt = (double[])swCurveU.Evaluate2(nStartParam, 0);
             vEndPt = (double[])swCurveU.Evaluate2(nEndParam, 0);

             vTessPts = (double[])swCurveU.GetTessPts(nChordTol, nLengthTol, (vStartPt), (vEndPt));

              swSketchMgr = (SketchManager)swModel.SketchManager;

             swSketchMgr.Insert3DSketch(false);
             swModel.SetAddToDB(true);

             for (i = 0; i <= vTessPts.GetUpperBound(0) - 3; i += 3)
             {
                 swSketchSeg = (SketchSegment)swModel.CreateLine2(vTessPts[i + 0], vTessPts[i + 1], vTessPts[i + 2], vTessPts[i + 3], vTessPts[i + 4], vTessPts[i + 5]);
             }

             swModel.SetAddToDB(false);
             swSketchMgr.Insert3DSketch(true);

             bRet = swModel.EditRebuild3();

         }

         public SldWorks swApp;

     }
 }
```
