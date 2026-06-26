---
title: "Get Reference Point Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Reference_Point_Data_Example_CSharp.htm"
---

# Get Reference Point Data Example (C#)

This example shows how to get reference point data.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part, assembly, or drawing document that has a
 //    reference point.
 // 2. Select the reference point.
 //
 // Postconditions:
 // 1. Selects the feature used to create the reference point.
 // 2. Press F5 after each feature selection to continue.
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
 namespace ReferencePointFeatDataType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             RefPoint swRefPt = default(RefPoint);
             RefPointFeatureData swRefPtData = default(RefPointFeatureData);
             MathPoint swMathPt = default(MathPoint);
             object[] vEntArr = null;
             object vEnt = null;
             Entity swEnt = default(Entity);
             SketchPoint swSkPt = default(SketchPoint);
             SketchSegment swSkSeg = default(SketchSegment);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swRefPt = (RefPoint)swFeat.GetSpecificFeature2();
             swRefPtData = (RefPointFeatureData)swFeat.GetDefinition();
             swMathPt = swRefPt.GetRefPoint();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  " + swFeat.Name);
             Debug.Print("    Pt = (" + ((double[])swMathPt.ArrayData)[0] * 1000.0 + ", " + ((double[])swMathPt.ArrayData)[1] * 1000.0 + ", " + ((double[])swMathPt.ArrayData)[2] * 1000.0 + ") mm");
             Debug.Print("    AlongCurveOption   = " + swRefPtData.AlongCurveOption);
             Debug.Print("    Distance           = " + swRefPtData.Distance * 1000.0 + " mm");
             Debug.Print("    Type               = " + swRefPtData.Type);

             bRet = swRefPtData.AccessSelections(swModel,  null);
             vEntArr = (object[])swRefPtData.Selections;

             foreach (object vEnt_loopVariable in vEntArr)
             {
                 vEnt = vEnt_loopVariable;
                 if ((null != vEnt))
                 {
                     if (vEnt is Entity)
                     {
                         swEnt = (Entity)vEnt;
                         bRet = swEnt.Select4(true, null);
                         Debug.Print("Entity used to create reference point selected.");
                         System.Diagnostics.Debugger.Break();
                     }
                     else if (vEnt is  SketchPoint)
                     {
                         swSkPt = (SketchPoint)vEnt;
                         bRet = swSkPt.Select4(true, null);
                         Debug.Print("SketchPoint used to create reference point selected.");
                         System.Diagnostics.Debugger.Break();
                     }
                     else if (vEnt is  SketchSegment)
                     {
                         swSkSeg = (SketchSegment)vEnt;
                         bRet = swSkSeg.Select4(true, null);
                         Debug.Print("SketchSegment used to create reference point selected.");
                         System.Diagnostics.Debugger.Break();
                     }
                     else
                     {
                     }
                 }
             }

             swRefPtData.ReleaseSelectionAccess();

         }

         public SldWorks swApp;

     }
 }
```
