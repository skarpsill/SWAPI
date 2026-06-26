---
title: "Add Ordinate Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Ordinate_Dimension_Example_VB.htm"
---

# Add Ordinate Dimension Example (VBA)

This example shows how to add an ordinate dimension.

'------------------------------------------

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1)
Drawing document is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2)
Two horizontal parallel edges are selected.

'

' Postconditions: Ordinate dimension added.

'-------------------------------------------

Option Explicit

Public Enum swAddOrdinateDims_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swOrdinate
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swVerticalOrdinate
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swHorizontalOrdinate
= 3

End Enum

Public Enum swCreateOrdDimError_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_Undefined
= -1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If encountered,
report as SPR.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_Success
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_GenFailure
= 1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_SDIM_BAD_DIM

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_GenNoInternalDims
= 2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_NO_INTERNAL_DIMS_IN_DSKETCH

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_GenBadSel
= 3kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_DIM_REF_NOCREATE

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_GenNeedModelLoaded
= 4kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_CANNOT_DIM_GHOST_IN3D

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_GenSamePartOnly
= 5kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_DIM_EDIT_PART

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_GenExtraSelection
= 6kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_DIM_TOO_MANY_SELECT

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_OrdFailure
= 7kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_BAD_ORDINATE_DIM0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_OrdDupInGroup
= 8kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_BAD_ORDINATE_DIM1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateOrdDimErr_OrdBadDir
= 9kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MSG_BAD_ORDINATE_DIM2

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.modelDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nRetvalkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Horizontal ordinate ignores X placement

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nRetval
= swDraw.AddOrdinateDimension2(swHorizontalOrdinate,
-0.1, 0.02, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
