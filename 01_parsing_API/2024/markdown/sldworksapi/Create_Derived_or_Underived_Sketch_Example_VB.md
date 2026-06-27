---
title: "Create Derived or Underived Sketch Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_or_Underived_Sketch_Example_VB.htm"
---

# Create Derived or Underived Sketch Example VB

## Create Derived or Underived Sketch Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swSketch As SldWorks.Sketch
```

```
Sub main()
```

```
        Set swApp = Application.SldWorks
        Set swModel = swApp.ActiveDoc
```

```
        ' Interactively select a sketch
        Set swSelMgr = swModel.SelectionManager
        Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
        Set swSketch = swFeat.GetSpecificFeature2
```

```
        ' Is the selected sketch derived?
        Debug.Print ("Is the selected sketch derived? " & swSketch.IsDerived)
```

```
        ' If the selected sketch is a derived sketch,
        ' then create a derived sketch; else underive the
        ' selected sketch
        If swSketch.IsDerived Then
            swModel.UnderiveSketch
            Debug.Print ("  Selected sketch was derived; sketch is now underived.")
        Else
            swModel.DeriveSketch
            Debug.Print ("  Selected sketch was not derived; a derived sketch has been created.")
        End If
```

```
        swModel.ForceRebuild3 (False)
```

```
End Sub
```
