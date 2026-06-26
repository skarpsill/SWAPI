---
title: "Create Derived or Underived Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_or_Underived_Sketch_Example_VBNET.htm"
---

# Create Derived or Underived Sketch Example (VB.NET)

This example shows how to create a derived or underived sketch.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open a part that contains at least one sketch.
' 2. Select a sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. If the selected sketch is not derived, then a
'    derived sketch is created.
'    - or -
'    If the selected sketch is derived, then the
'    sketch is changed to underived.
' 2. Examine the FeatureManager design tree and Immediate
'    window.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Diagnostics
Imports System
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro
```

```vb
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeat As Feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketch As Sketch

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Interactively select a sketch
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeat = swSelMgr.GetSelectedObject6(1, -1)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketch = swFeat.GetSpecificFeature2

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Is the selected sketch derived? " & swSketch.IsDerived)

 kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}' If the selected sketch is a derived sketch,
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' then create a derived sketch; else, underive the
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' selected sketch
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swSketch.IsDerived Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.UnderiveSketch
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Selected sketch was derived; sketch is now underived.")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.DeriveSketch
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Selected sketch was not derived; a derived sketch has been created.")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(False)

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
