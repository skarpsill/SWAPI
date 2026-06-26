---
title: "ModelDoc::FeatureRevolveCut2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureRevolveCut2.htm"
---

# ModelDoc::FeatureRevolveCut2

This
method is obsolete and has been superseded by[ModelDoc2::FeatureRevolveCut2](../ModelDoc2/ModelDoc2__FeatureRevolveCut2.htm).

Description

This method creates a revolved feature cut. For extruded feature cuts,
see ModelDoc::FeatureCut.

Syntax (OLE Automation)

retval = ModelDoc.FeatureRevolveCut2
( angle, reverseDir, angle2, revType, Options)

(Table)=========================================================

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution, where: 1 = MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to be revolved
is ( angle /2 ) on either side
of the sketch. The reverseDir argument has no affect. 2 = Two direction revolution. For a two direction revolve, the angle is the angle to be revolved in
direction 1 and angle2 is the
angle to be revolved in direction 2. |
| Input: | (long) Options | Additional control |
| Return: | (long) retval | 0 for no error |

Syntax (COM)

status = ModelDoc->FeatureRevolveCut2(
angle, reverseDir, angle2, revType, Options, &retval )

(Table)=========================================================

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution, where: 1 = MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to be revolved
is ( angle /2 ) on either side
of the sketch. The reverseDir argument has no affect. 2 = Two direction revolution. For a two direction revolve, the angle is the angle to be revolved in
direction 1 and angle2 is the
angle to be revolved in direction 2. |
| Input: | (long) Options | Additional control |
| Output: | (long) retval | 0 for no error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The options argument allows additional control of the feature creation.
Supported values are listed inswoptions.h.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__FeatureRevolveCut2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
