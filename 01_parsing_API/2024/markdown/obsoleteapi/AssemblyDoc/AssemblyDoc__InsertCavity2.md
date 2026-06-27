---
title: "AssemblyDoc::InsertCavity2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__InsertCavity2.htm"
---

# AssemblyDoc::InsertCavity2

This method is obsolete and has been superseded
by[AssemblyDoc::InsertCavity3](AssemblyDoc__InsertCavity3.htm).

Description

This method inserts a cavity to the active part using a selected component.
This operation is performed in the context of an assembly document. The
component being edited in the context of the assembly will receive the
new Cavity feature.

Syntax (OLE Automation)

void AssemblyDoc.InsertCavity2 ( scaleFactor,
scaleType)

(Table)=========================================================

| Input: | (double) scaleFactor | Scaling factor |
| --- | --- | --- |
| Input: | (long) scaleType | Type of scaling |

Syntax
(COM)

status = AssemblyDoc->InsertCavity2
( scaleFactor, scaleType )

(Table)=========================================================

| Input: | (double) scaleFactor | Scaling factor |
| --- | --- | --- |
| Input: | (long) scaleType | Type of scaling |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Set the scaleFactor parameter appropriately for your casting material.
Express the scaling factor as a percent (+/- 20%) of the size of the cavity
part, passing a value between -20 and +20.

The formula used to determine the size of the cavity is:

cavitysize = partsize * (1 + scaleFactor/100)

The scaleType parameter specifies the type of scaling. Options include:

(Table)=========================================================

| 0 | About component centroids |
| --- | --- |
| 1 | About component origins |
| 2 | About mold base origin |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDoc\AssemblyDoc__InsertCavity2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
