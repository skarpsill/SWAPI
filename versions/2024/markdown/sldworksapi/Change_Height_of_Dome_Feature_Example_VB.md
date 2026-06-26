---
title: "Change Height of Dome Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Height_of_Dome_Feature_Example_VB.htm"
---

# Change Height of Dome Feature Example (VBA)

This example shows how to change the height of a dome feature.

'--------------------------------------

'

' Preconditions: Dome feature for which a distance was
specified is selected.

'

' Postconditions: Height of dome feature is doubled.

'

'--------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPartkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.PartDoc

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
swDomekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DomeFeatureData2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEntkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Entity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPart = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelData = swSelMgr.CreateSelectData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDome = swFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swFeat.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Ellipticalkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDome.Elliptical

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Heightkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDome.Height* 1000#
& " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReverseDirkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDome.ReverseDir

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Roll back to get access to face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swDome.AccessSelections(swModel,
Nothing): Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swDome.Face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEnt = swFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swEnt.Select4(False, swSelData):
Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Make some changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDome.Height= 2# * swDome.Height

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDome.Elliptical= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Apply changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Assert will fire if dome cannot be changed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swFeat.ModifyDefinition(swDome,
swModel, Nothing): Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub
