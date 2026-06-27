---
title: "Create Curve Through Reference Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Curve_Through_Reference_Points_Example_VB.htm"
---

# Create Curve Through Reference Points Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim feat As SldWorks.Feature
 Dim featData As SldWorks.ReferencePointCurveFeatureData
 Dim selMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "block20", False, longstatus
     Set Part = swApp.ActiveDoc
     Set selMgr = Part.SelectionManager

    boolstatus = Part.Extension.SelectByID2("", "VERTEX", 6.46002912861796E-02, 0, 4.93456023787655E-02, False, 1, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "VERTEX", 6.46002912861796E-02, 0.039624, 4.93456023787655E-02, True, 1, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "VERTEX", -6.24778997860176E-02, 0.039624, 4.93456023787655E-02, True, 1, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "VERTEX", -6.24778997860176E-02, 0, 4.93456023787655E-02, True, 1, Nothing, 0)

     Part.Insert3DSplineCurve False
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, False, 0, Nothing, 0)
     Set feat = selMgr.GetSelectedObject6(1, -1)
     Set featData = feat.GetDefinition

    featData.AccessSelections Part, Nothing
     Debug.Print feat.Name
     Debug.Print "  Closed curve? " & featData.ClosedCurve
     Debug.Print "  Number of through points: " & featData.GetThroughPointCount

    featData.ReleaseSelectionAccess

End Sub
```
