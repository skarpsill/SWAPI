---
title: "Get Face Hatch Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Face_Hatch_Data_Example_VBNET.htm"
---

# Get Face Hatch Data Example (VB.NET)

This example shows how to get the number of face hatches in a standard
or derived (detail, section, projected, broken, etc.) drawing view and data.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Select Section View A-A in the FeatureManager design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets face hatch data.
' 2. Examine the Immediate window.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public
 Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swView As View
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vFaceHatch As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFaceHatch As FaceHatch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp = CreateObject("SldWorks.Application")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swView = swSelMgr.GetSelectedObject6(1,
 -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("View kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}=
 " & swView.Name)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Type =
 " & swView.Type)
```

```vb
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vFaceHatch = swView.GetFaceHatches
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If IsNothing(vFaceHatch) Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}No face hatches in selected view.")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of face hatches in this view = " & (UBound(vFaceHatch) + 1))
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not IsNothing(vFaceHatch) Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Face hatches =")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For i = 0 To UBound(vFaceHatch)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFaceHatch = vFaceHatch(i)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Get face hatch data
                 ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Angle kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " & swFaceHatch.Angle * 57.3 & " degrees")
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Color kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " & swFaceHatch.Color)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Definition kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}= " + swFaceHatch.Definition)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Layer kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " & swFaceHatch.Layer)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Pattern kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}= " + swFaceHatch.Pattern)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Scale kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " & swFaceHatch.Scale2)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}SolidFill kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}= " & swFaceHatch.SolidFill)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Material crosshatch = " & swFaceHatch.UseMaterialHatch)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}-----------------------")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next i
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
