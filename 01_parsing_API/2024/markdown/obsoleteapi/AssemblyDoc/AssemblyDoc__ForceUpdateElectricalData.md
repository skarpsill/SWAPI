---
title: "AssemblyDoc::ForceUpdateElectricalData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__ForceUpdateElectricalData.htm"
---

# AssemblyDoc::ForceUpdateElectricalData

This method is obsolete and has been superseded
by[AssemblyDoc::ForeUpdateElectricalData2](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__ForceUpdateElectricalData2.htm).

Description

This method forces an update
of electrical data.

Syntax (OLE Automation)

void = AssemblyDoc.ForceUpdateElectricalData ( stream)

(Table)=========================================================

| Input: | (long) stream | 0
= All streams 2
= From-To list stream 3
= Segment data stream 4
= Wire list stream |
| --- | --- | --- |

Syntax (COM

status = AssemblyDoc->ForceUpdateElectricalData
( stream)

Parameters Table Start

(Table)=========================================================

| Input: | (long) stream | 0
= All streams 2
= From-To list stream 3
= Segment data stream 4
= Wire list stream |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Third-party applications call
this method to tell the SolidWorks software that they have changed the
electrical data. The SolidWorks software then re-reads the data to get
the updates.

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
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\AssemblyDoc\AssemblyDoc__ForceUpdateElectricalData.htm" >
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
<param name="Items" value="AssemblyDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\AssemblyDoc\AssemblyDoc__ForceUpdateElectricalData.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
