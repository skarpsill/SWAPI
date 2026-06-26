---
title: "Create Curve Through Reference Points Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Curve_Through_Reference_Points_Example_VBNET.htm"
---

# Create Curve Through Reference Points Example (VB.NET)

This example shows how to create a curve through reference points.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the part document.
 ' 2. Selects four reference points.
 ' 3. Creates Curve1 through the selected points.
 ' 4. Inspect the FeatureManager design tree, the graphics area, and the
 '    Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim feat As Feature
     Dim featData As ReferencePointCurveFeatureData
     Dim selMgr As SelectionMgr
     Dim boolstatus As Boolean
     Dim longstatus As Integer, longwarnings As Integer

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("block20", False, longstatus)
         Part = swApp.ActiveDoc
         selMgr = Part.SelectionManager

         boolstatus = Part.Extension.SelectByID2("", "VERTEX", 0.0646002912861796, 0, 0.0493456023787655, False, 1, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "VERTEX", 0.0646002912861796, 0.039624, 0.0493456023787655, True, 1, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "VERTEX", -0.0624778997860176, 0.039624, 0.0493456023787655, True, 1, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "VERTEX", -0.0624778997860176, 0, 0.0493456023787655, True, 1, Nothing, 0)

         Part.Insert3DSplineCurve(False)
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, False, 0, Nothing, 0)
         feat = selMgr.GetSelectedObject6(1, -1)
         featData = feat.GetDefinition

         featData.AccessSelections(Part, Nothing)
         Debug.Print(feat.Name)
         Debug.Print("  Closed curve? " & featData.ClosedCurve)
         Debug.Print("  Number of through points: " & featData.GetThroughPointCount)

         featData.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
