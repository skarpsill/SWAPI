---
title: "ModelDoc2::FeatureRevolveCut2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureRevolveCut2.htm"
---

# ModelDoc2::FeatureRevolveCut2

This method is obsolete and has been superseded
by[FeatureManager::FeatureRevolveCut.](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureRevolveCut.htm)

Description

This method creates a revolved feature cut.

Syntax (OLE Automation)

retval = ModelDoc2.FeatureRevolveCut2
( angle, reverseDir, angle2, revType, Options)

(Table)=========================================================

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | TRUE if angle is positive, FALSE if negative |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution: 1 = MidPlane revolution. For this type of revolve,
the angle argument specifies the full revolution. The angle to revolve
is (angle/2) on either side of the sketch. The reverseDir argument has
no effect. 2 = Two-direction revolution. For a two direction
revolve, the angle argument is the angle to revolve in Direction1 and
the angle2 argument is the angle to revolve in Direction2. |
| Input: | (long) Options | Additional control as defined in swAutoCloseSketch;
close the sketch if it is open |
| Return: | (long) retval | 0 if no error, 1 if error |

Syntax (COM)

status = ModelDoc2->FeatureRevolveCut2(
angle, reverseDir, angle2, revType, Options, &retval )

(Table)=========================================================

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | TRUE if angle is positive, FALSE if negative |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution: 1 = MidPlane revolution. For this type of revolve,
the angle argument specifies the full revolution. The angle to revolve
is (angle/2) on either side of the sketch. The reverseDir argument has
no effect. 2 = Two-direction revolution. For a two direction
revolve, the angle argument is the angle to revolve in Direction1 and
the angle2 argument is the angle to revolve in Direction2. |
| Input: | (long) Options | Additional control as defined in swAutoCloseSketch;
close the sketch if it is open |
| Output: | (long) retval | 0 if no error, 1 if error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc2\ModelDoc2__FeatureRevolveCut2.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc2\ModelDoc2__FeatureRevolveCut2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
