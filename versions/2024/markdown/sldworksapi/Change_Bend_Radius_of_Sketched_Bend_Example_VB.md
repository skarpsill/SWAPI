---
title: "Change Bend Radius of Sketched Bend Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm"
---

# Change Bend Radius of Sketched Bend Example (VBA)

This example shows how to change the bend radius of a sketched bend.

'--------------------------------------------
' Preconditions:
' 1. Open a model document containing a sketched bend.
' 2.
Sketched bend is selected.
'
' Postconditions: Increases the size of bend radius
' of the selected
sketched bendkadov_tag{{</spaces>}}is
increased by 1.5 times.

'---------------------------------------------

Option Explicit

Public Enum swFlangePositionTypes_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFlangePositionTypeMaterialInside
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFlangePositionTypeMaterialOutside
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFlangePositionTypeBendOutside
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFlangePositionTypeBendCenterLine
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFlangePositionTypeBendSharp
= 5

End Enum

Public Enum swBendAllowanceTypes_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBendAllowanceBendTable
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBendAllowanceKFactor
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBendAllowanceDirect
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBendAllowanceDeduction
= 4

End Enum

Sub DumpCustomBendAllowanceInfo _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sPadStr
As String, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCustBendAllow
As SldWorks.CustomBendAllowance _

)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "Typekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCustBendAllow.Type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "BendAllowancekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCustBendAllow.BendAllowance* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "BendDeductionkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCustBendAllow.BendDeduction* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "BendTableFilekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCustBendAllow.BendTableFile

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sPadStr & "KFactorkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCustBendAllow.KFactor

End Sub

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
swSelDatakadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketchBendkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchedBendFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBendFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.BendsFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCustBendAllowkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.CustomBendAllowance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEntkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Entity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nFace_Xkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nFace_Ykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nFace_Zkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{</spaces>}}Set
swSelData = swSelMgr.CreateSelectData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketchBend = swFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCustBendAllow = swSketchBend.GetCustomBendAllowance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swFeat.Name

'1
radian = 180º/ p = 57.295779513º or approximately
57.3º

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BendAnglekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swSketchBend.BendAngle* 57.3 & " deg"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BendRadiuskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swSketchBend.BendRadius* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PositionTypekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swSketchBend.PositionType

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReverseDirectionkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swSketchBend.ReverseDirection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UseDefaultBendAllowancekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swSketchBend.UseDefaultBendAllowance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UseDefaultBendRadiuskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swSketchBend.UseDefaultBendRadius

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Roll back to get to fixed face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swSketchBend.AccessSelections(swModel,
Nothing): Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swSketchBend.GetFixedFace(nFace_X,
nFace_Y, nFace_Z)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEnt = swFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Fixed
Facekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & nFace_X * 1000# & ", " & nFace_Y * 1000#
& ", " & nFace_Z * 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Custom
Bend Allowance:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DumpCustomBendAllowanceInfo
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}",
swCustBendAllow

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swEnt.Select4(True, swSelData):
Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Make some changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchBend.UseDefaultBendRadius= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchBend.BendRadius
= swSketchBend.BendRadius* 1.5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Apply changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swFeat.ModifyDefinition(swSketchBend,
swModel, Nothing): Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

'--------------------------------------------
