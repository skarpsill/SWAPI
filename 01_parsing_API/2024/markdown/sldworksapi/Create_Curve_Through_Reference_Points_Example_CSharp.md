---
title: "Create Curve Through Reference Points Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Curve_Through_Reference_Points_Example_CSharp.htm"
---

# Create Curve Through Reference Points Example (C#)

This example shows how to create a curve through reference points.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Opens the part document.
 // 2. Selects four reference points.
 // 3. Creates Curve1 through the selected points.
 // 4. Inspect the FeatureManager design tree, the graphics area, and the
 //    Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // ---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace InsertCurveThroughPoints_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Feature feat;
         ReferencePointCurveFeatureData featData;
         SelectionMgr selMgr;
         bool boolstatus;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("block20", false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;
             selMgr = (SelectionMgr)Part.SelectionManager;

             boolstatus = Part.Extension.SelectByID2("", "VERTEX", 0.0646002912861796, 0, 0.0493456023787655, false, 1, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "VERTEX", 0.0646002912861796, 0.039624, 0.0493456023787655, true, 1, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "VERTEX", -0.0624778997860176, 0.039624, 0.0493456023787655, true, 1, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "VERTEX", -0.0624778997860176, 0, 0.0493456023787655, true, 1, null, 0);

             Part.Insert3DSplineCurve(false);
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, false, 0, null, 0);
             feat = (Feature)selMgr.GetSelectedObject6(1, -1);
             featData = (ReferencePointCurveFeatureData)feat.GetDefinition();

             featData.AccessSelections(Part, null);
             Debug.Print(feat.Name);
             Debug.Print("  Closed curve? " + featData.ClosedCurve);
             Debug.Print("  Number of through points: " + featData.GetThroughPointCount());

             featData.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
