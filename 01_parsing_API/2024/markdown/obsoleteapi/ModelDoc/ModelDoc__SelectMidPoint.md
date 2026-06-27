---
title: "ModelDoc::SelectMidPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectMidPoint.htm"
---

# ModelDoc::SelectMidPoint

## ModelDoc::SelectMidpoint

This
method is obsolete and has been superseded by[ModelDoc2::SelectMidPoint](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectMidPoint.htm).

Description

When an edge is selected, this method puts the midpoint (swSelMIDPOINTS)
of that edge on the select list and removes the edge from the select list.

Syntax (OLE Automation)

(void) ModelDoc.SelectMidpoint ( )

Syntax (COM)

status = ModelDoc->SelectMidpoint
( )

(Table)=========================================================

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

If the edge whose midpoint is desired is already
on the select list and ModelDoc::AndSelect is used to select it again,
then ModelDoc::SelectMidpoint leaves both the edge and the point on the
select list.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__SelectMidPoint.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
