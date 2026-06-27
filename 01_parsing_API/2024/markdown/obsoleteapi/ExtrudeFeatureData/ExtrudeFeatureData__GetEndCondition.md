---
title: "ExtrudeFeatureData::GetEndCondition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetEndCondition.htm"
---

# ExtrudeFeatureData::GetEndCondition

This
method is obsolete and has been superseded by ExtrudeFeatureData2::GetEndCondition .

Description

This method gets the end condition type of
the extrusion feature for forward or reverse direction.

Syntax (OLE Automation)

endCondition= ExtrudeFeatureData.GetEndCondition
(forward)

(Table)=========================================================

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for
reverse |
| --- | --- | --- |
| Return: | (int) endCondition | End condition type as defined in swEndConditions_e |

Syntax (COM)

status = ExtrudeFeatureData->GetEndCondition (
forward, &endCondition )

(Table)=========================================================

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for
reverse |
| --- | --- | --- |
| Output: | (int) endCondition | End condition type as defined in swEndConditions_e |
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
<param name="Items" value="ZReleaseNotes2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\ExtrudeFeatureData2000\ExtrudeFeatureData__GetEndCondition.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\ExtrudeFeatureData2000\ExtrudeFeatureData__GetEndCondition.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
