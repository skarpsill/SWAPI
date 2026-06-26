---
title: "Display Temporary Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Temporary_Body_Example_VB.htm"
---

# Display Temporary Body Example (VBA)

This example shows how to display a temporary body.

```
'-------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to
'    open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Selects a component for the temporary body.
' 3. Displays the temporary body.
' 4. Examine the graphics area and the Immediate
'    window.
'
' NOTE: Because the assembly is used elsewhere, do
' not save changes.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim Part As SldWorks.ModelDoc2
    Dim Body As SldWorks.Body2
    Dim BodyCopy As SldWorks.Body2
    Dim status As Boolean
    Dim Component As SldWorks.Component2
    Dim MathUtility As SldWorks.MathUtility
    Dim MathXform As SldWorks.MathTransform
    Dim Xform(15) As Double
    Dim vXform As Variant
    Dim retval As Long
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Xform(0) = 1#
    Xform(1) = 0#
    Xform(2) = 0#
    Xform(3) = 0#
    Xform(4) = 1#
    Xform(5) = 0#
    Xform(6) = 0#
    Xform(7) = 0#
    Xform(8) = 1#
    Xform(9) = 0.15
    Xform(10) = 0#
    Xform(11) = 0#
    Xform(12) = 1#
    Xform(13) = 0#
    Xform(14) = 0#
    Xform(15) = 0#
    vXform = Xform
```

```
    Set swApp = Application.SldWorks
    Set MathUtility = swApp.GetMathUtility
    Set MathXform = MathUtility.CreateTransform(vXform)
```

```
    'Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem1.sldasm"
    Set Part = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select component and create temporary body
    status = Part.Extension.SelectByID2("TestPart1-1@assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set Component = Part.SelectionManager.GetSelectedObjectsComponent3(1, 0)
    Set Body = Component.GetBody
    Set BodyCopy = Body.Copy
    BodyCopy.ApplyTransform MathXform
```

```
    'Display temporary body
    retval = BodyCopy.Display3(Component, 255, swTempBodySelectable)
    Debug.Print "Temporary body displayed (0 = success)? " & retval
```

```
    Part.ViewZoomtofit2
```

```
End Sub
```
