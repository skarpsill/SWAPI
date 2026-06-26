---
title: "RevolveFeatureData::GetRevolutionAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RevolveFeatureData/RevolveFeatureData__GetRevolutionAngle.htm"
---

# RevolveFeatureData::GetRevolutionAngle

This
method is obsolete and has been superseded by RevolveFeatureData2::GetRevolutionAngle .

Description

This method gets the revolution angle of the
feature in forward or reverse direction.

Syntax (OLE Automation)

angle = RevolveFeatureData.GetRevolutionAngle (forward)

(Table)=========================================================

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for
reverse |
| --- | --- | --- |
| Return: | (double) angle | Revolution angle of the feature in radians |

Syntax (COM)

status = RevolveFeatureData->GetRevolutionAngle
( forward, &angle )

(Table)=========================================================

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for
reverse |
| --- | --- | --- |
| Output: | (double) angle | Revolution angle of the feature in radians |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\RevolveFeatureData\RevolveFeatureData__GetRevolutionAngle.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
