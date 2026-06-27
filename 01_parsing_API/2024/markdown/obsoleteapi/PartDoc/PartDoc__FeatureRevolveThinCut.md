---
title: "PartDoc::FeatureRevolveThinCut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__FeatureRevolveThinCut.htm"
---

# PartDoc::FeatureRevolveThinCut

This method is obsolete and has been superseded
by[FeatureManager::FeatureRevolveThinCut](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureRevolveThinCut.htm).

Description

This method creates a feature by revolving a profile about an axis.
A constant thickness is given to the profile when revolving. The result
is then removed from the existing work piece

Syntax (OLE Automation)

(void) PartDoc.FeatureRevolveThinCut
( angle, reverseDir, angle2, revType, thickness1, thickness2, thinType
)

(Table)=========================================================

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Angle is positive or negative (TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (double) thickness1 | Wall thickness 1 (thinType = 2 uses (thickness1 ) /2
for each direction) |
| Input: | (double) thickness2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (long) thinType | Thin feature type: 0 = One direction 1 = One direction reverse 2 = Midplane 3 = Two direction |

Syntax (COM)

status = PartDoc->FeatureRevolveThinCut
( angle, reverseDir, angle2, revType, thickness1, thickness2, thinType
)

(Table)=========================================================

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Angle is positive or negative (TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (double) thickness1 | Wall thickness 1 (thinType = 2 uses (thickness1 ) /2
for each direction) |
| Input: | (double) thickness2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (long) thinType | Thin feature type: 0 = One direction 1 = One direction reverse 2 = Midplane 3 = Two direction |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Type of revolution:

- 0= one direction
- 1= midPlane
- 2=two direction

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PartDoc_Object$$**$$ZCreateBody$$**$$ZModifyBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\PartDoc\PartDoc__FeatureRevolveThinCut.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
