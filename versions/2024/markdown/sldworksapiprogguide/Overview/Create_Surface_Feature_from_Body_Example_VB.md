---
title: "Create Surface Feature from Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapiprogguide/Overview/Create_Surface_Feature_from_Body_Example_VB.htm"
---

# Create Surface Feature from Body Example (VBA)

This example shows how to create a surface feature from a body.

'---------------------------------------

'

' Preconditions: Part document is open and contains one
solid body.

'

' Postconditions: A new part document is created and a
surface feature

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}is
created using the body in the open part document.

'

'----------------------------------------

Option Explicit

Public Enum swCreateFacesBodyAction_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateFacesBodyActionCap
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateFacesBodyActionGrow
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateFacesBodyActionGrowFromParent
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateFacesBodyActionLeaveRubber
= 4

End Enum

Public Enum swCreateFeatureBodyOpts_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateFeatureBodyCheck
= &H1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCreateFeatureBodySimplify
= &H2

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Modeler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPartkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.PartDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swNewPartkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.PartDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swNewModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBodykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swTempBodykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFace()kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDelFace()kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFirstFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vFeatArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bLocChkkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModeler = swApp.GetModeler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPart = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBody = swPart.Body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swNewPart = swApp.NewPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swNewModel = swNewPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
swFace(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace(0) = swBody.GetFirstFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While Not swFace(UBound(swFace)) Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
Preserve swFace(UBound(swFace) + 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace(UBound(swFace)) = swFace(UBound(swFace) - 1).GetNextFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
Preserve swFace(UBound(swFace))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFace
= swFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swTempBody = swModeler.CreateBodyFromFaces2(UBound(vFace),
vFace, swCreateFacesBodyActionCap, True, bLocChk): Debug.Assert bLocChk

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFeatArr
= swNewPart.CreateSurfaceFeatureFromBody(swTempBody,
swCreateFeatureBodyCheck)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vFeat In vFeatArr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = vFeat

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swFeat.Select2(False, 0): Debug.Assert
bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swNewModel.EditSuppress2: Debug.Assert
bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swFeat.Select2(False, 0): Debug.Assert
bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swNewModel.EditUnsuppress2:
Debug.Assert bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
vFeat

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

'---------------------------------
