---
title: "Create Sheet Body From Faces and Feature from Sheet Body Example (VB)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sheet_Body_From_Faces_and_Feature_from_Sheet_Body_Example_VB.htm"
---

# Create Sheet Body From Faces and Feature from Sheet Body Example (VB)

This example shows how to create a sheet body from the faces of a solid
body and how to create a feature from the sheet body.

'-------------------------------------------------------

'

' Preconditions: Part document is open that contains

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a
solid body named Extrude1.

'

' Postconditions: Surface-Imported feature is created
from

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
sheet body.

'

'-------------------------------------------------------

Option Explicit

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Modeler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBodykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swWorkPieceBodykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swWorkPieceFacesBodykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swWorkPieceBodyCopykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aFaces()kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swThickenedBodykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatureManagerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aBodies(0)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vBodieskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPartkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
PartDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeaturekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bValuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
lErrorskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
lWarningskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vFaceskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
lIdxkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
retvalkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeatureManager = swModel.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get Modeler object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModeler = swApp.GetModeler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Clear selection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bValue
= swModel.Extension.SelectByID2("Extrude1",
"SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swWorkPieceBody = swModel.SelectionManager.GetSelectedObject6(1,
-1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create temporary body by copying the selected body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Boolean operations consume bodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swWorkPieceBodyCopy = swWorkPieceBody.Copy

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Clear the selection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Collect the faces on the selected body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lIdx
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swWorkPieceBodyCopy.GetFirstFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While (Not (swFace Is Nothing))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
Preserve aFaces(lIdx)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
aFaces(lIdx) = swFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lIdx
= lIdx + 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swFace.GetNextFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create a sheet body from the faces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFaces
= aFaces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swWorkPieceFacesBody = swModeler.CreateSheetFromFaces(vFaces)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create a feature from the sheet body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
aBodies(0) = swWorkPieceFacesBody

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodies
= aBodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPart = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeature = swPart.CreateFeatureFromBody3(vBodies(0),
False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Rebuild the model; a Surface-Imported feature shouldkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
appear in the FeatureManager design tree after the rebuild

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.EditRebuild3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub
