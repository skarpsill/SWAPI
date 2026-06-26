---
title: "Select All Faces on Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Faces_on_Part_Example_VB.htm"
---

# Select All Faces on Part Example (VBA)

This example shows how to get all of the faces in a part.

```
'------------------------------------------
' Preconditions: Open a part document containing one part.
'
' Postconditions:
' 1. Selects all faces on the part.
' 2. Examine the graphics area.
'------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim swFace As SldWorks.Face
    Dim swEnt As SldWorks.Entity
    Dim bRet As Boolean
    Dim vBodies As Variant
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    vBodies = swPart.GetBodies2(swAllBodies, True)
    Set swBody = vBodies(0)
    Set swFace = swBody.GetFirstFace
```

```
    swModel.ClearSelection2 True
```

```
    Do While Not swFace Is Nothing
        Set swEnt = swFace
        ' Select using IEntity
        bRet = swEnt.Select4(True, swSelData)
        Set swFace = swFace.GetNextFace
    Loop
```

```
End Sub
```
