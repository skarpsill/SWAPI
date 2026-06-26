---
title: "Use Presentation Transforms to Move Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Presentation_Transforms_to_Move_Component_Example_VB.htm"
---

# Use Presentation Transforms to Move Component Example (VBA)

This example shows how to use presentation transforms.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a fully resolved assembly.
' 2. Select a component.
'
' Postconditions: Moves the component.
'
' NOTES:
' * When the graphics area is redrawn, the display
'   reverts to how it was at the before running the
'   macro, that is, the selected component
'   appears to move back to its original
'   position. This is by design because
'   presentation transforms are disabled
'   at the end of the macro. If presentation transforms
'   are not disabled, then the component would
'   remain in its moved position.
' * When presentation transforms are enabled,
'   access to most of the menus is blocked.
'   This is by design because selections cannot
'   be made because the graphics area is not the
'   same as the model data.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const MaxSteps As Long = 100
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim vXform As Variant
    Dim arr(15) As Double
    Dim swMathUtil As SldWorks.MathUtility
    Dim swMathXform As SldWorks.MathTransform
    Dim swModelView as SldWorks.ModelView
    Dim i As Long
    Dim rect as Variant
```

```
    Set swApp = Application.SldWorks
    Set swMathUtil = swApp.GetMathUtility()
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
```

```
    ' Block access to menus
    swAssy.EnablePresentation = True
```

```
    ' Set up unit matrix - no rotation, translation, or scaling
```

```
    ' Unit rotation matrix
    arr(0) = 1#:    arr(1) = 0#:    arr(2) = 0#
    arr(3) = 0#:    arr(4) = 1#:    arr(5) = 0#
    arr(6) = 0#:    arr(7) = 0#:    arr(8) = 1#
```

```
    ' No translation
    arr(9) = 0#:    arr(10) = 0#:   arr(11) = 0#
```

```
    ' Unit scaling
    arr(12) = 1#
```

```
    ' Not used, so pad with zeros
    arr(13) = 0#:   arr(14) = 0#:   arr(15) = 0#
```

```
    For i = 1 To MaxSteps
        ' Change rotation
        arr(2) = 1.2 * (i / MaxSteps)
        arr(3) = 1.2 * (i / MaxSteps):  arr(4) = 0.8 * (i / MaxSteps):  arr(5) = 0.9 * (i / MaxSteps)
        arr(6) = 0.8 * (i / MaxSteps)
```

```
        ' Change translation
        arr(9) = 0.1 * (i / MaxSteps):  arr(10) = 0.2 * (i / MaxSteps)
```

```
        ' Should really check that matrix is valid,
        ' especially rotation matrix
        vXform = arr
```

```
        Set swMathXform = swMathUtil.CreateTransform((vXform))
```

```
        swComp.RemovePresentationTransform
        swComp.PresentationTransform = swMathXform
```

```
        ' Redraw so it is shown immediately
        Set swModelView = swModel.ActiveView
        Set rect = Nothing
        swModelView.GraphicsRedraw (rect)
    Next i
```

```
    ' Re-enable access to menus
    ' Comment out to leave component in its moved position
    swAssy.EnablePresentation = False
```

```
End Sub
```
