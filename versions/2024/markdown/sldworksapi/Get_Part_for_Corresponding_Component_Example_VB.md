---
title: "Get Part for Corresponding Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part_for_Corresponding_Component_Example_VB.htm"
---

# Get Part for Corresponding Component Example (VBA)

This example shows how to get the names of the part entity and the corresponding
assembly component entity.

'-----------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Assembly document is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Select the feature whose part's and component's name you want.

'

' Postconditions: None

'

'-----------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelDocCompkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelDocExtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDocExtension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAssyFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPartFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCompkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vFaceArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAssyFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPartFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAssyEntkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.entity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPartEntkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.entity

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
swAssyFeat = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swComp = swSelMgr.GetSelectedObjectsComponent2(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocComp = swComp.GetModelDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModelDocComp.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFaceArr
= swAssyFeat.GetFaces: Debug.Assert
Not IsEmpty(vFaceArr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAssyFace = vFaceArr(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAssyEnt = swAssyFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPartEnt = swModelDocExt.GetCorrespondingEntity(swAssyEnt):
Debug.Assert Not swPartEnt Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPartFace = swPartEnt

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPartFeat = swPartFace.GetFeature:
Debug.Assert Not swPartFeat Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Compkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" + swComp.Name2+ "
[" + swComp.GetPathName+
"]"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AssyFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" + swAssyFeat.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PartFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" + swPartFeat.Name

End Sub

'---------------------------------------------------
