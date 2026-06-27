---
title: "SimpleFilletFeatureData::GetRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__GetRadius.htm"
---

# SimpleFilletFeatureData::GetRadius

This
method is obsolete and has been superseded by SimpleFilletFeatureData2::GetRadius .

Description

This method gets the radius value for specified
fillet item.

Syntax (OLE Automation)

radius= SimpleFilletFeatureData.GetRadius
(pFilletItem)

(Table)=========================================================

| Input: | (LPDISPATCH) pFilletItem | Pointer to a dispatch object, the fillet item
for which the radius value is desired |
| --- | --- | --- |
| Return: | ( double ) radius | Radius value |

Syntax (COM)

status = SimpleFilletFeatureData->IGetRadius (
pFilletItem, &radius )

(Table)=========================================================

| Input: | (LPUNKNOWN) pFilletItem | Pointer to an unknown object, the fillet item
for which the radius value is desired |
| --- | --- | --- |
| Output: | ( double ) radius | Radius value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To obtain a pointer to a fillet Item, see SimpleFilletFeatureData::GetFilletItemAtIndex
and the SimpleFilletFeatureData::FilletItemsCount. Fillets can be made
from multiple edges or faces and these methods get a pointer to any of
the entities that helped to create the particular fillet and pass it into
pFilletItem of this method.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SimpleFilletFeatureData\SimpleFilletFeatureData__GetRadius.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
