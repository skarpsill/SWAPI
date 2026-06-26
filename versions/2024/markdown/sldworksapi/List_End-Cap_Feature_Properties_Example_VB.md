---
title: "List End-Cap Feature Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/List_End-Cap_Feature_Properties_Example_VB.htm"
---

# List End-Cap Feature Properties Example (VBA)

This example shows how to list an end-cap feature's properties and select
and then deselect the face used to create the end-cap feature.

'------------------------------------

'

' Preconditions: Model document is open and an end-cap
feature is selected.

'

' Postcondtions: None

'

'------------------------------------

Option Explicit

Public Enum swSketchSegments_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchLINE
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchARC
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchELLIPSE
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchSPLINE
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchTEXT
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchPARABOLA
= 5

End Enum

Public Enum swSolidworksWeldmentEndCondOptions_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndConditionNone
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndConditionMiter
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndConditionButt1
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndConditionButt2
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndConditionTrim
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndConditionUseDefault
= 5

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEndCapkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.EndCapFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEntkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Entity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEndCap = swFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swFeat.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ChamferDistancekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swEndCap.ChamferDistance* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OffsetDistancekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swEndCap.OffsetDistance* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Thicknesskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swEndCap.Thickness* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ThicknessRatioForOffsetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swEndCap.ThicknessRatioForOffset

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UseChamferCornerskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swEndCap.UseChamferCorners

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UseThicknessRatioForOffsetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swEndCap.UseThicknessRatioForOffset

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swEndCap.AccessSelections(swModel,
Nothing): Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swEndCap.Face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEnt = swFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swEnt.Select4(False, Nothing):
Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndCap.ReleaseSelectionAccess

End Sub
