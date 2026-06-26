---
title: "Get Direction of Bendline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Direction_of_Bendline_Example_VB.htm"
---

# Get Direction of Bendline Example (VBA)

This example shows how to get the direction of the selected bendline.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Unsuppresses the Flat-Pattern1 feature.
' 2. Selects a bendline.
' 3. Gets the direction of the bendline.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketchLine As SldWorks.SketchLine
Dim status As Boolean

Sub main()
```

```
Set swApp = Application.SldWorks
```

```
' Open a sheet metal part
Set swModel = swApp.ActiveDoc
```

```
' Select the flat-pattern feature
Set swModelDocExt = swModel.Extension
status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
```

```
' Unsuppress the flat-pattern feature
status = swModel.EditUnsuppress2
swModel.ClearSelection2 True
```

```
' Select a bendline
status = swModelDocExt.SelectByID2("Line12@Bend-Lines1", "EXTSKETCHSEGMENT", 1.36749256504085E-02, -8.42517000103271E-03, 0, False, 0, Nothing, 0)
Set swSelMgr = swModel.SelectionManager
Set swSketchLine = swSelMgr.GetSelectedObject6(1, -1)
```

```
' Print to the Immediate window the direction of the selected bend line
Debug.Print "Direction of bend line (0= not a bendline; 1 = bendline has up direction; 2 = bendline has down direction): " & swSketchLine.GetBendLineDirection
```

```
End Sub
```
