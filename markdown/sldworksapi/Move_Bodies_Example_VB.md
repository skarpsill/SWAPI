---
title: "Move Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Bodies_Example_VB.htm"
---

# Move Bodies Example (VBA)

This example shows how to move all of the bodies in a part document.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Specified part document to open exists.
' 2. Run the macro.
'
' Postconditions: All of the bodies in the part document
' are moved to the specified location.
'
' NOTE: Because this part is used elsewhere, do not save
' any changes when closing it.
'--------------------------------------------------------------
```

```
Option Explicit
```

```
Sub SelectBodies(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, bodyArr As Variant)
' Select and mark the bodies to move
```

```
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim body As Variant
    Dim swBody As SldWorks.Body2
    Dim status  As Boolean
```

```
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
```

```
    If IsEmpty(bodyArr) Then Exit Sub
    For Each body In bodyArr
        Set swBody = body
        swSelData.Mark = 1
        status = swBody.Select2(True, swSelData)
    Next body
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim bodyArr As Variant
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swFeat As SldWorks.Feature
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swPart = swModel
    Set swFeatMgr = swModel.FeatureManager
```

```
    swModel.ClearSelection2 True
```

```
    ' Get the bodies to move
    bodyArr = swPart.GetBodies2(swAllBodies, false)
    SelectBodies swApp, swModel, bodyArr
```

```
    ' Move the bodies
    Set swFeat = swFeatMgr.InsertMoveCopyBody2(0.1, 0.2, 0.3, 0#, 0#, 0#, 0#, 0#, 0#, 0#, False, 1)
```

```
  End Sub
```
