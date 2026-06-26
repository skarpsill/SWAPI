---
title: "ModelDoc2::HoleWizard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__HoleWizard.htm"
---

# ModelDoc2::HoleWizard

This method is obsolete and has been superseded
by[FeatureManager::HoleWizard](sldworksAPI.chm::/FeatureManager/FeatureManager__HoleWizard.htm).

Description

This method invokes the hole wizard to create a new hole.

Syntax (OLE Automation)

void ModelDoc2.HoleWizard
( depth, endType, flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9,
d10, d11, d12)

(Table)=========================================================

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type as defined in swEndConditions_e |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE to not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE to not |
| Input: | (long) hType | Hole type |
| Input: | (double) d1 | Dimension value |
| Input: | (double) d12 | Dimension value |

Syntax (COM)

status = ModelDoc2->HoleWizard
( depth, endType, flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9,
d10, d11, d12 )

(Table)=========================================================

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type as defined in swEndConditions_e |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE to not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE to not |
| Input: | (long) hType | Hole type, see below |
| Input: | (double) d1 | Dimension value |
| Input: | (double) d12 | Dimension value |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The hType argument controls the type of hole that is created:

- 0 -
  Simple
- 1 -
  Tapered
- 2 -
  Counter Bore
- 3 -
  Counter Sunk
- 4 -
  Counter Drilled
- 5 -
  Simple Drilled
- 6 -
  Tapered Drilled
- 7 -
  C-Bored Drilled
- 8 -
  C-Sunk Drilled
- 9 -
  C-Drilled Drilled

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc2\ModelDoc2__HoleWizard.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc2\ModelDoc2__HoleWizard.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
