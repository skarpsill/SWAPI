---
title: "Insert Weldment Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Features_Example_CSharp.htm"
---

# Insert Weldment Features Example (C#)

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

//---------------------------------------------------------------------------
// Preconditions:
//kadov_tag{{<spaces>}}1.
Open`public_documents`\samples\tutorial\weldments\weldment_box2.sldprt//kadov_tag{{<spaces>}}2.
Expand the Cut list folder in the FeatureManager design tree
// and observe
its contents.
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3.
Delete End cap1 from the FeatureManager design tree.
// 4. Change the path specified for**profilePathName**, if necessary.
//
// Postconditions:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Observe
the following in the FeatureManager design tree:
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Gusset1 moves to the sub weld folder, Sub Folder1, in the Cut list
// folder
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Trim/Extend8 feature appears at the bottom of the design tree and at
// the
end of the Cut list folder
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Structural Member6 feature appears at the bottom of the design tree
// and
at the end of the Cut list folder
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
End cap5 feature appears at the bottom of the design tree and in the
// Cut
list folder
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Gusset5 feature appears at the bottom of the design tree and in the
// Cut
list folder
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
Fillet Bead5 feature appears at the bottom of the design tree and
// in the
Cut list folder
//
//**NOTE**:
Because this part is used elsewhere,
// do not save
any changes when you close it.
//---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

namespace InsertWeldmentFeatures_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FeatureManager
fm;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectionMgr
selMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
Part;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
boolstatus;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object
myFeature = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Body2[]
obj = new Body2[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Array
v = default(Array);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part
= (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object
myModelView = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myModelView
= Part.ActiveView;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}selMgr
= (SelectionMgr)Part.SelectionManager;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//InsertSubWeldFolder2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Gusset1", "SOLIDBODY",
0, 0, 0, false, 0, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}obj[0]
= (Body2)selMgr.GetSelectedObject6(1, -1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v
= obj;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}fm
= Part.FeatureManager;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= fm.InsertSubWeldFolder2(v);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//InsertWeldmentTrimFeature2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Body2[]
obj1 = new Body2[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Body2[]
obj2 = new Body2[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
Options = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Array
v1 = default(Array);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Array
v2 = default(Array);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY",
0, 0, 0, true, 2, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY",
0, 0, 0, true, 1, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
Count = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= selMgr.GetSelectedObjectCount();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(Count == 2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}obj1[0]
= (Body2)selMgr.GetSelectedObject2(1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v1
= obj1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}obj2[0]
= (Body2)selMgr.GetSelectedObject2(2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v2
= obj2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Options
= (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_AllowTrimmedExtensionTrim
+ (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_AllowTrimmingExtensionTrim
+ (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_CopedCut
+ (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_WeldGap;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= fm.InsertWeldmentTrimFeature2(1,
(int)Options, 0.01, v1, v2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//InsertEndCapFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
endCapFeature = default(Feature);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Face2[]
face1 = new Face2[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Array
x = default(Array);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.6023443450227,
0.6150000000001, -1.013201139555, true, 1, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}face1[0]
= (Face2)selMgr.GetSelectedObject6(1, -1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}x
= face1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}endCapFeature
= fm.InsertEndCapFeature2(0.005,
false, true, 0.003, 0.5, 0.003, x);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//InsertStructuralWeldment3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Array
segmentObjects = default(Array);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchSegment[]
sketchSegments = new SketchSegment[4];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
profilePathName = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
structuralMember = default(Feature);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberGroup
@group = default(StructuralMemberGroup);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberGroup[]
GroupArray1 = new StructuralMemberGroup[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
i = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}@group
= fm.CreateStructuralMemberGroup();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.InsertSketch2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segmentObjects
= (System.Array)Part.SketchManager.CreateCornerRectangle(0, 0, 0, 1.0,
2.0, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i <= segmentObjects.GetUpperBound(0); i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sketchSegments[i]
= (SketchSegment)segmentObjects.GetValue(i);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}@group.Segments
= sketchSegments;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GroupArray1[0]
= @group;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ViewZoomtofit2();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.InsertSketch2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}profilePathName
= "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\english\\weldment
profiles\\ansi inch\\square tube\\2 x 2 x 0.25.SLDLFP";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}structuralMember
= fm.InsertStructuralWeldment3(profilePathName,
1, 0.0, false, GroupArray1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//InsertGussetFeature2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Face2[]
faceGFObj = new Face2[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object
z = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.02539999999988,
1.94542628561, 0.00429028534694, true, 1, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.07780718114736,
1.9746, -0.001856983219, true, 2, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= selMgr.GetSelectedObjectCount();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(Count == 2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}faceGFObj[0]
= (Face2)selMgr.GetSelectedObject6(1, 1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}faceGFObj[1]
= (Face2)selMgr.GetSelectedObject6(1, 2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z
= faceGFObj;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= fm.InsertGussetFeature2(0.005,
0, 0, false, 0.025, 0.025, 0.015, 0.7853981633975, 0.015, true,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0.005,
0, false, false, false, z);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//InsertFilletBeadFeature3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Face2[]
fbFaceObj1 = new Face2[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Face2[]
fbFaceObj2 = new Face2[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.0412896304482,
0.02548020566445, 0, true, 1, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.09804264728081,
0.01499999999999, 0.0008069730266129, true, 2, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("", "FACE", 0.01364526875011,
0.08738481720087, 0.01330055827532, true, 4, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= selMgr.GetSelectedObjectCount();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Face Set 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}fbFaceObj1[0]
= (Face2)selMgr.GetSelectedObject6(1, 1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Face Set 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}fbFaceObj2[0]
= (Face2)selMgr.GetSelectedObject6(1, 2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//fbFaceObj2(0)
= selMgr.GetSelectedObject6(1, 4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v1
= fbFaceObj1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v2
= fbFaceObj2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int[]
edges = new int[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Array
edgeArray = default(Array);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}edges[0]
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//edges(1)
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}edgeArray
= edges;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= fm.InsertFilletBeadFeature3(0,
0.003, 0.003, 2, 0.003, 0.006, 0, 0.003, 0.003, 2, 0.003, 0, 1, edgeArray,
0, null, v1, v2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
