---
title: "RibFeatureData::NextReference"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__NextReference.htm"
---

# RibFeatureData::NextReference

This
method is obsolete and has been superseded by RibFeatureData2::NextReference .

Description

For ribs with multiple contours, this method cycles through the possible
sketch entities that can be used to define the Draft if it is used.

Syntax (OLE Automation)

Index = RibFeatureData.NextReference(
)

(Table)=========================================================

| Return: | (int) Index | Index of the entity that is used |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData->NextReference(
&Index)

(Table)=========================================================

| Output: | (int) Index | Index of the entity that is used |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method cycles through the entities. It starts at the beginning
again once the last entity is reached.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\RibFeatureData\RibFeatureData__NextReference.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
