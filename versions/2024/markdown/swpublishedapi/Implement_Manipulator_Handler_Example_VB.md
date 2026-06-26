---
title: "Implement Manipulator Handler Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Implement_Manipulator_Handler_Example_VB.htm"
---

# Implement Manipulator Handler Example (VBA)

This example shows how to implement a manipulator handler.

'-----------------------------------------------------------------------------

Option Explicit

ImplementsSwManipulatorHandler2

______________________________________________________________________________

Private Function SwManipulatorHandler2_OnDelete(ByVal
pManipulator As Object) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnDelete"

End Function

______________________________________________________________________________

Private Sub SwManipulatorHandler2_OnDirectionFlipped(ByVal
pManipulator As Object)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnDirectionFlipped"

End Sub

______________________________________________________________________________

Private Function SwManipulatorHandler2_OnDoubleValueChanged(ByVal
pManipulator As Object, ByVal Id As Long, Value As Double) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Debug.Assert
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnDoubleValueChanged"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IDkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & Id

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Valuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & Value

End Function

______________________________________________________________________________

Private Sub SwManipulatorHandler2_OnEndDrag(ByVal
pManipulator As Object)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnEndDrag"

End Sub

______________________________________________________________________________

Private Sub SwManipulatorHandler2_OnEndDrag(ByVal
pManipulator As Object, ByVal handleIndex As Long)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnEndDrag"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HandleIndexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & handleIndex

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(handleIndex = swDragArrowManipulatorOptions_e.swDragArrowManipulatorDirection2)
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
" Direction1"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
" Direction2"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub

______________________________________________________________________________

Private Sub SwManipulatorHandler2_OnHandleRmbSelected(ByVal
pManipulator As Object, ByVal handleIndex As Long)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnHandleRmbSelected"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}handleIndexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" + handleIndex

End Sub

______________________________________________________________________________

Private Sub SwManipulatorHandler2_OnHandleSelected(ByVal
pManipulator As Object, ByVal handleIndex As Long)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnHandleSelected"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HandleIndexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" + handleIndex

End Sub

______________________________________________________________________________

Private Sub SwManipulatorHandler2_OnItemSetFocus(ByVal
pManipulator As Object, ByVal Id As Long)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnItemSetFocus"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IDkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & Id

End Sub

______________________________________________________________________________

Private Function SwManipulatorHandler2_OnLmbSelected(ByVal
pManipulator As Object) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnLmbSelected"

End Function

______________________________________________________________________________

Private Function SwManipulatorHandler2_OnStringValueChanged(ByVal
pManipulator As Object, ByVal Id As Long, Value As String) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnStringValueChanged"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IDkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & Id

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Valuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & Value

End Function

______________________________________________________________________________

Private Sub SwManipulatorHandler2_OnUpdateDrag(ByVal
pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt
As Object)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SwManipulatorHandler2_OnUpdateDrag"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HandleIndexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & handleIndex

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXCreateTriadManipulator$$**$$EXImplementManipulatorHandler$$**$$TriadManipulator_Object$$**$$DragArrowManipulator_Object$$**$$SwManipulatorHandler2_Object$$**$$Manipulator_Object$$**$$Manipulators$$**$$EXCreateDragArrowManipulator$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\sldworksapi\OVERVIEW\Manipulators.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
