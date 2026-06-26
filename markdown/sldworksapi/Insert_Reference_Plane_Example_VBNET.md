---
title: "Insert Reference Plane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Reference_Plane_Example_VBNET.htm"
---

# Insert Reference Plane Example (VB.NET)

This example shows how to create a constraint-based angle reference
plane.

```
'-----------------------------------------------------------
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a constraint-based reference plane.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatureManager As FeatureManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeature As Feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swRefPlane As RefPlane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swRefPlaneFeatureData As RefPlaneFeatureData
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim fileerror As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim filewarning As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim planeType As Long

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\plate.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", fileerror, filewarning)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatureManager = swModel.FeatureManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create a constraint-based reference plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.028424218552, 0.07057725774359, 0, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.05976462601598, 0.0718389621656, 0.0001242036435087, True, 1, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swRefPlane = swFeatureManager.InsertRefPlane(16, 0.7853981633975, 4, 0, 0, 0)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get type of the just-created reference plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeature = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swRefPlaneFeatureData = swFeature.GetDefinition

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}planeType = swRefPlaneFeatureData.Type2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type2: ")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case planeType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 0
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Invalid")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Undefined")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 2
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Line Point")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 3
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Three Points")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 4
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Line Line")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 5
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Distance")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 6
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Parallel")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 7
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Angle")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 8
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Normal")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 9
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}On Surface")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 10
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Standard")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 11
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Constraint-based")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}planeType = swRefPlaneFeatureData.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type: ")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case planeType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 0
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Invalid")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Undefined")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 2
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Line Point")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 3
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Three Points")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 4
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Line Line")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 5
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Distance")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 6
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Parallel")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 7
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Angle")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 8
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Normal")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 9
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}On Surface")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 10
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Standard")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 11
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Constraint-based")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
