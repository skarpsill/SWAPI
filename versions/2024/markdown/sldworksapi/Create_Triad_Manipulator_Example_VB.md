---
title: "Create Triad Manipulator Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Triad_Manipulator_Example_VB.htm"
---

# Create Triad Manipulator Example (VBA)

This example shows how to create a triad manipulator.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Click**Tools > References****>****SolidWorks 2015 exposed type libraries
for ' add-in use**(**swpublished.tlb**) and click**OK**.
' 2. Right-click the project name in the Project Explorer and
click
'**Insert > Class Module**.
' 3. Click**Class1**in the Project Explorer.
' 4. Type**swDragManipHdlr**in**(Name)**in the Properties
window.
' 5. Copy[Module](#Module)to the main module.
' 6. Copy[Class
module](#Class)to the swDragManipHdlr class module.
' 7. Open a model document and select a face.
' 8. Open an Immediate window.
'
' Postconditions:
' 1. Creates a triad manipulator whose origin is the point
' selected on the face.
' 2. Drag a triad manipulator handle and inspect the Immediate window.
'----------------------------------------------------------------------------

#### 'Module

Option Explicit

kadov_tag{{<spaces>}}Dim
swManipkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Manipulator

kadov_tag{{<spaces>}}Dim swTriadkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.TriadManipulator

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDragHdlrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
swDragManipHdlr

kadov_tag{{<spaces>}}Dim swFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathUtilkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModViewMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelViewManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vPickPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPickPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDragHdlr = New swDragManipHdlr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathUtil = swApp.GetMathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swSelMgr.GetSelectedObject6(1,
-1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vPickPt
= swSelMgr.GetSelectionPoint2(1, -1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPickPt = swMathUtil.CreatePoint((vPickPt))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModViewMgr = swModel.ModelViewManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swManip = swModViewMgr.CreateManipulator(swTriadManipulator,
swDragHdlr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swTriad = swManip.GetSpecificManipulator

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTriad.Origin= swPickPt

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swManip.ShowswModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

[Back to top](#top)

#### 'Class module

```vb
Option Explicit
Implements SwManipulatorHandler2

Private Function SwManipulatorHandler2_OnDelete(ByVal pManipulator As Object) As Boolean
    Debug.Print "Manipulator deleted"
End Function

Private Sub SwManipulatorHandler2_OnDirectionFlipped(ByVal pManipulator As Object)
    Debug.Print "Direction flipped"
End Sub

Private Function SwManipulatorHandler2_OnDoubleValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As Double) As Boolean
    Debug.Print "Double value changed "
    Debug.Print "  Value            = " & Value
End Function

Private Sub SwManipulatorHandler2_OnEndNoDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)

     Debug.Print "Mouse button released"
    Debug.Print "  HandleIndex  as defined in swTriadManipulatorControlPoints_e    = " + handleIndex

 End Sub

Private Sub SwManipulatorHandler2_OnEndDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "Mouse button released after dragging a manipulator handle"
End Sub

Private Sub SwManipulatorHandler2_OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "Right-mouse button clicked"
    Debug.Print "  HandleIndex as defined in swTriadManipulatorControlPoints_e     = " + handleIndex
End Sub

Private Sub SwManipulatorHandler2_OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "Manipulator handle selected"
    Debug.Print "  HandleIndex      = " + handleIndex
End Sub

Private Sub SwManipulatorHandler2_OnItemSetFocus(ByVal pManipulator As Object, ByVal Id As Long)
    Debug.Print "Focus set on item"
    Debug.Print "  Item ID               = " & Id
End Sub

Private Function SwManipulatorHandler2_OnHandleLmbSelected(ByVal pManipulator As Object) As Boolean
    Debug.Print "Left-mouse button clicked"
End Function

Private Function SwManipulatorHandler2_OnStringValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As String) As Boolean
    Debug.Print "String value changed"
    Debug.Print "  Value            = " & Value
End Function

Private Sub SwManipulatorHandler2_OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt As Object)
    Debug.Print "Manipulator handle moved while left- or right-mouse button depressed"
    Debug.Print "  HandleIndex as defined in swTriadManipulatorControlPoints_e     = " & handleIndex
End Sub
Back to top
```
