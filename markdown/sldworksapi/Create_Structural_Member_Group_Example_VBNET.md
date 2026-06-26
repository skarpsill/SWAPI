---
title: "Create a Structural-Member Group Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Structural_Member_Group_Example_VBNET.htm"
---

# Create a Structural-Member Group Example (VB.NET)

This example shows how to create structural-member groups for weldment features.

'
----------------------------------------------------------------------
' Preconditions:
'kadov_tag{{<spaces>}}1. Ensure
that the specified weldment profile and path exist.
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. If
necessary, modify the path in both calls to
' InsertStructuralWeldment3.
'
' Postconditions:
'kadov_tag{{<spaces>}}1. Two
structural-member features are created.
'kadov_tag{{<spaces>}}2. Each
feature consists of one structural-member group of two
' sketch segments.
'kadov_tag{{<spaces>}}3. Inspect
the Immediate Window for information.
'----------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Part As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
FeatMgr As FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SelMgr As SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swWeldFeat As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swWeldFeatData As StructuralMemberFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
MacroFolder As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MacroFolder
= swApp.GetCurrentMacroPathFolder()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SetCurrentWorkingDirectory(MacroFolder)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Template As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Template
= swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part
= swApp.NewDocument(Template, 0, 0, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FeatMgr
= Part.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelMgr
= Part.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSkLines As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkLines
= Part.SketchManager.CreateCornerRectangle(-0.1872393706766, 0.1133237194389,
0, -0.07003610048208, 0.009188409684237, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkLines
= Part.SketchManager.CreateCornerRectangle(0.06513561531715, 0.03369083550887,
0, 0.1807053904567, -0.08106219210316, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.SketchManager.InsertSketch(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ViewZoomtofit2()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
myFeature As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= Part.FeatureManager.InsertWeldmentFeature()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Group1 As StructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group1
= FeatMgr.CreateStructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
segments1(1) As SketchSegment

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
GroupArray1(0) As StructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT",
-0.1495427140733, 0.1133237194389, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT",
-0.1872393706766, 0.08238014634844, 0, True, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments1(0)
= SelMgr.GetSelectedObject6(1, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments1(1)
= SelMgr.GetSelectedObject6(2, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group1.Segments= segments1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GroupArray1(0)
= Group1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= Part.FeatureManager.InsertStructuralWeldment3("C:\Program
Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\c channel\3
x 5.sldlfp", 1, 0, False, GroupArray1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Group2 As StructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group2
= FeatMgr.CreateStructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
segments2(1) As SketchSegment

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
GroupArray2(0) As StructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT",
0.1185825251083, 0.03369083550887, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT",
0.06513561531715, -0.02774616865332, 0, True, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments2(0)
= SelMgr.GetSelectedObject6(1, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments2(1)
= SelMgr.GetSelectedObject6(2, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group2.Segments= segments2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GroupArray2(0)
= Group2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= Part.FeatureManager.InsertStructuralWeldment3("C:\Program
Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\c channel\3
x 5.sldlfp", 1, 0, False, GroupArray2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get Group Information

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Group As StructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vGroups As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSegments As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member1", "BODYFEATURE",
0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeat
= SelMgr.GetSelectedObject6(1, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData
= swWeldFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.AccessSelections(Part,
Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Groups
Count : " & swWeldFeatData.GetGroupsCount)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Feature Name : " & swWeldFeat.Name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vGroups
= swWeldFeatData.Groups

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Long, j As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = LBound(vGroups) To UBound(vGroups)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group
= vGroups(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Segment Count in Group " & i + 1 & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}:
" & Group.GetSegmentsCount)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Rotational angle for group: " + Group.Angle.ToString())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSegments
= Group.Segments

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
j = LBound(vSegments) To UBound(vSegments)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSegments(j).Select(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.ReleaseSelectionAccess()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member2", "BODYFEATURE",
0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeat
= SelMgr.GetSelectedObject6(1, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData
= swWeldFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.AccessSelections(Part,
Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Groups
Count : " & swWeldFeatData.GetGroupsCount)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Feature Name : " & swWeldFeat.Name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vGroups
= swWeldFeatData.Groups

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = LBound(vGroups) To UBound(vGroups)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group
= vGroups(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Segment Count in Group " & i + 1 & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}:
" & Group.GetSegmentsCount)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Rotational angle for group: " + Group.Angle.ToString())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSegments
= Group.Segments

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
j = LBound(vSegments) To UBound(vSegments)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSegments(j).Select(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.ReleaseSelectionAccess()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
