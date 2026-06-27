---
title: "Insert Weldment Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Features_Example_VB.htm"
---

# Insert Weldment Features Example (VBA)

This example shows how to insert the following weldment
features into the FeatureManager design tree:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End cap
feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Fillet
bead feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Gusset
feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Structural
weldment

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub weld
folder

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Weldment
trim feature

'----------------------------------------------------------------------------
' Preconditions:
'kadov_tag{{<spaces>}}1. Open`public_documents`\samples\tutorial\weldments\weldment_box2.sldprt'kadov_tag{{<spaces>}}2.
Expand the Cut list folder in the FeatureManager design tree
' and observe
its contents.
'kadov_tag{{<spaces>}}3.
Delete End cap1 from the FeatureManager design tree.
' 4. Change the path specified for**profilePathName**, if necessary.
'
' Postconditions:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Observe
the following in the FeatureManager design tree:
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Gusset1 moves to Sub Folder1 in the Cut list folder
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Trim/Extend8 feature appears at the bottom of the design tree
' and at the
end of the Cut list folder
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Structural Member6 feature appears at the bottom of the design tree
' and
at the end of the Cut list folder
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
End cap5 feature appears at the bottom of the design tree
' and in the Cut
list folder
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Gusset5 feature appears at the bottom of the design tree
' and in the Cut
list folder
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Fillet Bead5 feature appears at the bottom of the design tree
' and in the
Cut list folder
'
'kadov_tag{{<spaces>}}**NOTE**:
Because this part is used elsewhere,
' do not save
any changes when you close it.
'----------------------------------------------------------------------------

Option Explicit

Dim swApp As Object

Dim fm As FeatureManager

Dim selMgr As SelectionMgr

Dim Part As ModelDoc2

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
myFeature As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
obj(0) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
v As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
myModelView As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
myModelView = Part.ActiveView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myModelView.FrameState
= swWindowState_e.swWindowMaximized

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
selMgr = Part.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'InsertSubWeldFolder2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Gusset1", "SOLIDBODY",
0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
obj(0) = selMgr.GetSelectedObject6(1, -1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v
= obj

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
fm = Part.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
myFeature = fm.InsertSubWeldFolder2((v))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'InsertWeldmentTrimFeature2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
obj1(0) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
obj2(0) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Options As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
v1 As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
v2 As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY",
0, 0, 0, True, 2, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY",
0, 0, 0, True, 1, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
selMgr = Part.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Count As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= selMgr.GetSelectedObjectCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Count = 2 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
obj1(0) = selMgr.GetSelectedObject2(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v1
= obj1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
obj2(0) = selMgr.GetSelectedObject2(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v2
= obj2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options
=swWeldmentTrimExtendOption_AllowTrimmedExtensionTrim
+ swWeldmentTrimExtendOption_AllowTrimmingExtensionTrim + swWeldmentTrimExtendOption_CopedCut
+ swWeldmentTrimExtendOption_WeldGap

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
myFeature = fm.InsertWeldmentTrimFeature2(1,
Options, 0.01, (v1), (v2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'InsertFilletBeadFeature3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
fbFaceObj1(0) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
fbFaceObj2(1) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.0412896304482,
0.02548020566445, 0, True, 1, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.09804264728081,
0.01499999999999, 8.069730266129E-04, True, 2, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.01364526875011,
0.08738481720087, 0.01330055827532, True, 4, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= selMgr.GetSelectedObjectCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Face Set 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
fbFaceObj1(0) = selMgr.GetSelectedObject6(1, 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Face Set 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
fbFaceObj2(0) = selMgr.GetSelectedObject6(1, 2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
fbFaceObj2(1) = selMgr.GetSelectedObject6(1, 4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v1
= fbFaceObj1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v2
= fbFaceObj2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
fbEdges() As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
fbEdges(0 To 0) As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}fbEdges(0)
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
myFeature = fm.InsertFilletBeadFeature3(0,
0.003, 0.003, 2, 0.003, 0.006, 0, 0.003, 0.003, 2, 0.003, 0, 1, fbEdges,
0, Nothing, v1, v2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'InsertStructuralWeldment3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
errors As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
warnings As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sketchSegments As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
profilePathName As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
structuralMember As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
group As StructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
GroupArray2(0) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vGroups2 As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errors
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}warnings
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.InsertSketch2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sketchSegments
= Part.SketchManager.CreateCornerRectangle(0, 0, 0, 1#, 2#, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
group = fm.CreateStructuralMemberGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}group.Segments
= (sketchSegments)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
GroupArray2(0) = group

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vGroups2
= GroupArray2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ViewZoomtofit2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.InsertSketch2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}profilePathName
= "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi
inch\s section\5 X 10.SLDLFP"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
structuralMember = fm.InsertStructuralWeldment3(profilePathName,
swSolidworksWeldmentEndCondOptions_e.swEndConditionButt1, 0#, False, (vGroups2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'InsertEndCapFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
endCapFeature As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
y As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
faceECObj1(0) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
face As Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
selMgr = Part.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.6023443450227,
0.6150000000001, -1.013201139555, True, 1, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
face = selMgr.GetSelectedObject6(1, -1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
faceECObj1(0) = face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y
= faceECObj1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
endCapFeature = fm.InsertEndCapFeature2(0.005,
False, True, 0.003, 0.5, 0.003, y)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'InsertGussetFeature2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
faceGFObj(1) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
z As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.02539999999988,
1.94542628561, 0.00429028534694, True, 1, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.07780718114736,
1.9746, -0.001856983219, True, 2, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= selMgr.GetSelectedObjectCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Count = 2 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
faceGFObj(0) = selMgr.GetSelectedObject6(1, 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
faceGFObj(1) = selMgr.GetSelectedObject6(1, 2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z
= faceGFObj

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
myFeature = fm.InsertGussetFeature2(0.005,
0, 0, False, 0.025, 0.025, 0.015, 0.7853981633975, 0.015, True, 0.005,
0, False, False, False, z)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub
