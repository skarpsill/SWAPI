---
title: "Get Components Properties in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_Properties_in_Drawing_View_Example_VB.htm"
---

# Get Components Properties in Drawing View Example (VBA)

## Get Components' Properties in Drawing View Example (VBA)

This example shows how to get the components in a drawing view.

'----------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Drawing document of an assembly is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Drawing view is selected.

'

' Postconditions: None

'

'----------------------------------------------

Option Explicit

Public Enum swLineWeights_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_NONE
= -1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_THIN
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_NORMAL
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_THICK
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_THICK2
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_THICK3
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_THICK4
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_THICK5
= 6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_THICK6
= 7

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_NUMBER
= 8

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLW_LAYER
= 9

End Enum

Public Enum swLineStyles_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLineCONTINUOUS
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLineHIDDEN
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLinePHANTOM
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLineCHAIN
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLineCENTER
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLineSTITCH
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLineCHAINTHICK
= 6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swLineDEFAULT
= 7

End Enum

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
different types of drawing views

Public Enum swDrawingViewTypes_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingSheet
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingSectionView
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingDetailView
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingProjectedView
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingAuxiliaryView
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingStandardView
= 6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingNamedView
= 7

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawingRelativeView
= 8

End Enum

Sub ProcessDrawingComponent _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawComp
As SldWorks.DrawingComponent, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sPadStr
As String _

)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vDrawCompChildArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vDrawCompChildkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawCompChildkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Returns empty strings for root component

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "Namekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDrawComp.component.Name2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Filekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDrawComp.component.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IsRootkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDrawComp.IsRoot

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Layerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDrawComp.Layer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LayerOverridekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= "
& swDrawComp.LayerOverride

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Stylekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDrawComp.Style

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Visiblekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDrawComp.Visible

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Widthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDrawComp.Width

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vDrawCompChildArr
= swDrawComp.GetChildren

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vDrawCompChildArr) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vDrawCompChild In vDrawCompChildArr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDrawCompChild = vDrawCompChild

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ProcessDrawingComponent
swDrawCompChild, sPadStr + "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawCompkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDrawComp = swView.RootDrawingComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swView.Name& "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}["
& swView.Type& "]"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ProcessDrawingComponent
swDrawComp, "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"

End Sub

'---------------------------------------
