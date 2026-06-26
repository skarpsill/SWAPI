---
title: "ModelDoc::HoleWizard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__HoleWizard.htm"
---

# ModelDoc::HoleWizard

This
method is obsolete and has been superseded by[ModelDoc2::HoleWizard](../ModelDoc2/ModelDoc2__HoleWizard.htm).

Description

This method invokes the hole wizard to create a new hole.

Syntax (OLE Automation)

void ModelDoc.HoleWizard ( depth, endType,
flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12)

(Table)=========================================================

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE to not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE to not |
| Input: | (long) hType | Hole type |
| Input: | (double) d1...d12 | Dimension values |

Syntax
(COM)

status = ModelDoc->HoleWizard (
depth, endType, flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9,
d10, d11, d12 )

(Table)=========================================================

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE if not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE if not |
| Input: | (long) hType | Hole type |
| Input: | (double) d1...d12 | Dimension values |
| Input: | (double) d12 | Dimension value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The hType argument controls the type of hole that is created:

0 Simple

1 Tapered

2 Counter Bore

3 Counter Sunk

4 Counter Drilled

5 Simple Drilled

6 Tapered Drilled

7 C-Bored Drilled

8 C-Sunk Drilled

9 C-Drilled Drilled

For a complete and up-to-date list of available hole types, seeHoleWzd.idxlocated in the./lang/<language>folder of your SolidWorks installation.

Termination type may be any of the values in swEndConditions_e.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__HoleWizard.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
