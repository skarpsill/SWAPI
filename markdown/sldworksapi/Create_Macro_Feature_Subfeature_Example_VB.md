---
title: "Create Macro Feature Subfeature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Macro_Feature_Subfeature_Example_VB.htm"
---

# Create Macro Feature Subfeature Example (VBA)

This example shows how to create a macro feature subfeature.

'---------------------------------------------------------------------------

'

' Preconditions: Model document is open and a sketch is
selected.

'

' Postconditions: The sketch becomes a subfeature of the
newly

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}created
macro feature namedEmptyFeature.

'

'NOTE:A bitmap
namedFeatureIcon.bmpfor the
macro feature must exist.

'

'----------------------------------------------------------------------------

'Macro feature Rebuild routine

Function swmRebuild(varApp As Variant, varDoc As Variant,
varFeat As Variant) As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
App As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Doc As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
feat As SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
FeatData As SldWorks.MacroFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Rebuild As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
App = varApp

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Doc = varDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
feat = varFeat

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'MsgBox
"Rebuild called"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rebuild
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'If
an error occurs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Rebuild
= "Error message"

End Function

'Macro feature Edit definition routine

Function swmEditDefinition(varApp As Variant, varDoc As
Variant, varFeat As Variant) As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
App As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Doc As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
feat As SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
FeatData As SldWorks.MacroFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
App = varApp

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Doc = varDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
feat = varFeat

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
"Edit Definition called"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
FeatData = varFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}varFeat.ModifyDefinitionFeatData, varDoc, Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}EditDefinition
= True

End Function

'Macro feature Security routine

Function swmSecurity(varApp As Variant, varDoc As Variant,
varFeat As Variant) As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
App As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Doc As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
feat As SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
FeatData As SldWorks.MacroFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
App = varApp

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Doc = varDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
feat = varFeat

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swmSecurity
= SwConst.swMacroFeatureSecurityOptions_e.swMacroFeatureSecurityByDefault

End Function

'Base routine to create the macro feature

Sub CreateSampleFeature()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Doc As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
feat As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SelMan As SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Doc = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
SelMan = Doc.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ThisFile As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Methods(8) As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Names As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Types As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Values As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vEditBodies As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
options As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dimTypes As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dimValue As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
icons(2) As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Define
the routines to call

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ThisFile
= swApp.GetCurrentMacroPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Methods(0)
= ThisFile: Methods(1) = "FeatureModule": Methods(2) = "swmRebuild"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Methods(3)
= ThisFile: Methods(4) = "FeatureModule": Methods(5) = "swmEditDefinition"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Methods(6)
= "": Methods(7) = "": Methods(8) = ""kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'A
security routine is optional

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
pathname As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pathname
= swApp.GetCurrentMacroPathFolder

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}icons(0)
= pathname + "\FeatureIcon.bmp"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}icons(1)
= pathname + "\FeatureIcon.bmp"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}icons(2)
= pathname + "\FeatureIcon.bmp"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Names
= Empty

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Types
= Empty

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Values
= Empty

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}options
= swMacroFeatureByDefault

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
selFeat As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatMgr As SldWorks.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
selFeat = SelMan.GetSelectedObject6(1,
-1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeatMgr = Doc.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
feat = swFeatMgr.InsertMacroFeature3("EmptyFeature",
"", (Methods), Names, Types, Values, dimTypes, dimValue, vEditBodies,
(icons), options)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= feat.MakeSubFeature(selFeat)

End Sub
