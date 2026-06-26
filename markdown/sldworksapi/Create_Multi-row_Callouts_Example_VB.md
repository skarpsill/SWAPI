---
title: "Create Multi-row Callouts Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multi-row_Callouts_Example_VB.htm"
---

# Create Multi-row Callouts Example (VBA)

This example shows how to create multi-row callouts.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Copy and paste this code in the main module.
' 2. Click Insert > Class module and copy and paste
'    this code in the class module.
' 3. Click Tools > References > SOLIDWORKS version
'    exposed type libraries for add-in use.
' 4. Open a part or a fully resolved assembly.
' 5. Select one or more geometric entities in
'    the graphics area.
'
' Postconditions: Observe the graphics area while stepping
'    through the macro (put your cursor in the main module
'    in the IDE and press F8 repeatedly) to verify that callouts
'    are attached to each geometric entity selected in
'    Preconditions step 5.
'
' NOTE: Selecting features in FeatureManager design tree is
' not currently supported.
'-----------------------------------------------------------------
'Main module
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim vSelPos() As Variant
    Dim swCallout() As SldWorks.Callout
    Dim nSelCount As Long
    Dim i As Long
    Dim bRet As Boolean
    Dim callH As New Class1
    Dim boolstatus As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swModelExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    nSelCount = swSelMgr.GetSelectedObjectCount2(-1)
```

```
    ReDim vSelPos(nSelCount)
    ReDim swCallout(nSelCount)
```

```
    For i = 0 To nSelCount - 1
        vSelPos(i) = swSelMgr.GetSelectionPoint2((i + 1), -1)
    Next i
```

```
    swModel.ClearSelection2 True
```

```
    For i = 0 To nSelCount - 1
        Set swCallout(i) = swSelMgr.CreateCallout2(4, callH)
        swCallout(i).Label2(0) = "Project"
        swCallout(i).Label2(1) = "Product"
        swCallout(i).Label2(2) = "Radius"
        swCallout(i).Label2(3) = "Number"
        swCallout(i).Value(0) = "10685"
        swCallout(i).Value(1) = "Washer"
        swCallout(i).Value(2) = "30"
        swCallout(i).Value(3) = "1"
        swCallout(i).SetTargetPoint 0, vSelPos(i)(0), vSelPos(i)(1), vSelPos(i)(2)
        swCallout(i).SetTargetPoint 1, vSelPos(i)(0), vSelPos(i)(1), vSelPos(i)(2)
        swCallout(i).SetTargetPoint 2, vSelPos(i)(0), vSelPos(i)(1), vSelPos(i)(2)
        swCallout(i).SetTargetPoint 3, vSelPos(i)(0), vSelPos(i)(1), vSelPos(i)(2)
        swCallout(i).TextColor(0) = swSystemColorsRefTriadX
        swCallout(i).TextColor(1) = swSystemColorsRefTriadY
        swCallout(i).TextColor(2) = swSystemColorsRefTriadZ
        swCallout(i).TextColor(3) = swSystemColorsRefTriadX
        swCallout(i).OpaqueColor = swSystemColorsSelectedItem4
        swCallout(i).MultipleLeaders = False
	swCallout(i).EnablePushPin = True
        bRet = swModelExt.SelectByID2("", "", vSelPos(i)(0), vSelPos(i)(1), vSelPos(i)(2), True, 0, swCallout(i), 0)
        swCallout(i).ValueInactive(3) = True
    Next i
```

```
End Sub
```

[Back to top](#Top)

```
'Class module
```

```
Option Explicit
```

```
Implements SwCalloutHandler
```

```
Dim m_pCallout As SldWorks.Callout
```

```
Public Sub Init(clout As SldWorks.Callout)
    Set m_pCallout = clout
End Sub
```

```
Private Sub Class_Initialize()
    Debug.Print "Class_Initialize"
End Sub
```

```
Private Sub Class_Terminate()
    Debug.Print "Class_Terminate"
End Sub
```

```
Public Function SwCalloutHandler_OnStringValueChanged(ByVal pManipulator As Object, ByVal Index As Long, ByVal Text As String) As Boolean
    Debug.Print Index
    Debug.Print Text
    Dim retval As Boolean
End Function
```

[Back to top](#Top)
