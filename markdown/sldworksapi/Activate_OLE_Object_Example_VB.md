---
title: "Activate OLE Object Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_OLE_Object_Example_VB.htm"
---

# Activate OLE Object Example (VBA)

This example shows how to activate an OLE object on the active document.

```
'-------------------------------------
' Preconditions:
' 1. Open a model document that contains
'    Microsoft OLE object.
' 2. Select the Microsoft OLE object.
'
' Postconditions: Opens the worksheet in
' Microsoft Excel.
'--------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swOleObj As SldWorks.SwOLEObject
Dim xlObj As Object
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Get selected Microsfot Excel worksheet
    Set swOleObj = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Open the worksheet in Microsoft Excel
    Set xlObj = swOleObj.SetActive(True)
```

```
End Sub
```
