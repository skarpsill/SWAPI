---
title: "Rotate Move Face Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Move_Face_Feature_Example_VBNET.htm"
---

# Rotate Move Face Feature Example (VB.NET)

This example shows how to rotate (draft) a Move Face feature by changing
the XYZ origin and rotation angles.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document that kadov_tag{{</spaces>}}contains a Move Face feature kadov_tag{{</spaces>}}named Move Face1.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Rotates (drafts) the Move Face feature.
 ' 2. Examine the Immediate window.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Math

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeat As Feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swMoveFaceFeatData As MoveFaceFeatureData
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim varPara As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim newPara(5) As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim newVarPara As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim PI As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set PI
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}PI = 4 * Atan(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select, get, and access Move Face feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Move Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeat = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swMoveFaceFeatData = swFeat.GetDefinition
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swMoveFaceFeatData.AccessSelections(swModel, Nothing)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get current XYZ location and rotation angles of Move Face feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Before rotating Move Face feature...")
        ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Draft angle of Move Face feature: " & swMoveFaceFeatData.Angle * 57.3 & " degrees")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}XYZ origin (first 3) and rotation angles (last 3)")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}varPara = swMoveFaceFeatData.TriadRotationParameters
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = LBound(varPara) To UBound(varPara)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}" & (varPara(i)))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' New XYZ location and rotation angle values
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newPara(0) = 0.0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newPara(1) = 0.0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newPara(2) = 0.0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newPara(3) = 2 * PI / 180 ' Convert radians to degrees
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newPara(4) = 2 * PI / 180 ' Convert radians to degrees
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newPara(5) = 0.0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newVarPara = newPara

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Rotate the MoveFace feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swMoveFaceFeatData.TriadRotationParameters = newVarPara
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("After rotating Move Face feature...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Draft angle of Move Face feature: " & swMoveFaceFeatData.Angle * 57.3 & " degrees")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}XYZ origin (first 3) and rotation angles (last 3)")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}newVarPara = swMoveFaceFeatData.TriadRotationParameters
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = LBound(newVarPara) To UBound(newVarPara)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}" & (newVarPara(i)))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Modify the Move Face feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeat.ModifyDefinition(swMoveFaceFeatData, swModel, Nothing)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
