---
title: "Create a Structural-Member Group Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Structural_Member_Group_Example_CSharp.htm"
---

# Create a Structural-Member Group Example (C#)

This example shows how to create structural-member groups for weldment features.

//
--------------------------------------------------------------------------
// Preconditions:
//kadov_tag{{<spaces>}}1. Ensure
that the specified weldment profile and path exist.
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. If
necessary, modify the path in both calls to InsertStructuralWeldment3.
//
// Postconditions:
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Two
structural-member features are created.
//kadov_tag{{<spaces>}}2. Each
feature consists of one structural-member group of two
// sketch segments.
//kadov_tag{{<spaces>}}3. Inspect
the Immediate Window for information.
//---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

using System.Diagnostics;

namespace CreateStructureMemberGroup_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
Part;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
boolstatus;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FeatureManager
FeatMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectionMgr
SelMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
swWeldFeat;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberFeatureData
swWeldFeatData;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
MacroFolder = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MacroFolder
= swApp.GetCurrentMacroPathFolder();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SetCurrentWorkingDirectory(MacroFolder);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
Template = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Template
= swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part
= (ModelDoc2)swApp.NewDocument(Template, 0, 0, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FeatMgr
= Part.FeatureManager;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelMgr
= (SelectionMgr)Part.SelectionManager;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object
vSkLines = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkLines
= Part.SketchManager.CreateCornerRectangle(-0.1872393706766, 0.1133237194389,
0, -0.07003610048208, 0.009188409684237, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkLines
= Part.SketchManager.CreateCornerRectangle(0.06513561531715, 0.03369083550887,
0, 0.1807053904567, -0.08106219210316, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.SketchManager.InsertSketch(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ViewZoomtofit2();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
myFeature = default(Feature);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= Part.FeatureManager.InsertWeldmentFeature();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberGroup
Group1 = default(StructuralMemberGroup);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group1
= FeatMgr.CreateStructuralMemberGroup();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchSegment[]
segments1 = new SketchSegment[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberGroup[]
GroupArray1 = new StructuralMemberGroup[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT",
-0.1495427140733, 0.1133237194389, 0, false, 0, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT",
-0.1872393706766, 0.08238014634844, 0, true, 0, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments1[0]
= (SketchSegment)SelMgr.GetSelectedObject6(1, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments1[1]
= (SketchSegment)SelMgr.GetSelectedObject6(2, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group1.Segments= segments1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GroupArray1[0]
= Group1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= Part.FeatureManager.InsertStructuralWeldment3("C:\\Program
Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\c
channel\\3 x 5.sldlfp", 1, 0, false, GroupArray1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberGroup
Group2 = default(StructuralMemberGroup);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group2
= FeatMgr.CreateStructuralMemberGroup();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchSegment[]
segments2 = new SketchSegment[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberGroup[]
GroupArray2 = new StructuralMemberGroup[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT",
0.1185825251083, 0.03369083550887, 0, false, 0, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT",
0.06513561531715, -0.02774616865332, 0, true, 0, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments2[0]
= (SketchSegment)SelMgr.GetSelectedObject6(1, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}segments2[1]
= (SketchSegment)SelMgr.GetSelectedObject6(2, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group2.Segments= segments2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GroupArray2[0]
= Group2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myFeature
= Part.FeatureManager.InsertStructuralWeldment3("C:\\Program
Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\c
channel\\3 x 5.sldlfp", 1, 0, false, GroupArray2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get Group Information

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}StructuralMemberGroup
Group = default(StructuralMemberGroup);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Object[]
vGroups = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Object[]
vSegments = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchSegment
skSegment = default(SketchSegment);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member1", "BODYFEATURE",
0, 0, 0, false, 0, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeat
= (Feature)SelMgr.GetSelectedObject6(1, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData
= (StructuralMemberFeatureData)swWeldFeat.GetDefinition();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.AccessSelections(Part,
null);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Groups
Count : " + swWeldFeatData.GetGroupsCount());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Feature Name : " + swWeldFeat.Name);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vGroups
= (Object[])swWeldFeatData.Groups;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
i = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
j = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = vGroups.GetLowerBound(0); i <= vGroups.GetUpperBound(0); i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group
= (StructuralMemberGroup)vGroups[i];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Segment Count in Group " + i + 1 + " : " + Group.GetSegmentsCount());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Rotational angle of group: " + Group.Angle.ToString());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSegments
= (Object[])Group.Segments;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(j = vSegments.GetLowerBound(0); j <= vSegments.GetUpperBound(0); j++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skSegment
= (SketchSegment)vSegments[j];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skSegment.Select(false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.ReleaseSelectionAccess();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Structural Member2", "BODYFEATURE",
0, 0, 0, false, 0, null, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeat
= (Feature)SelMgr.GetSelectedObject6(1, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData
= (StructuralMemberFeatureData)swWeldFeat.GetDefinition();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.AccessSelections(Part,
null);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Groups
Count : " + swWeldFeatData.GetGroupsCount());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Feature Name : " + swWeldFeat.Name);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vGroups
= (Object[])swWeldFeatData.Groups;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = vGroups.GetLowerBound(0); i <= vGroups.GetUpperBound(0); i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Group
= (StructuralMemberGroup)vGroups[i];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Segment Count in Group " + i + 1 + " : " + Group.GetSegmentsCount());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Rotational angle of group: " + Group.Angle.ToString());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSegments
= (Object[])Group.Segments;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(j = vSegments.GetLowerBound(0); j <= vSegments.GetUpperBound(0); j++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skSegment
= (SketchSegment)vSegments[j];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skSegment.Select(false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swWeldFeatData.ReleaseSelectionAccess();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
