---
title: "PropertyManagerPageNumberbox::SetRange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPageNumberbox/PROPERTYMANAGERPAGENUMBERBOX__SETRANGE.HTM"
---

# PropertyManagerPageNumberbox::SetRange

This method is obsolete and has been superseded
by[PropertyManagerPageNumberbox::SetRange2](sldworksAPI.chm::/PropertyManagerPageNumberBox/PropertyManagerPageNumberbox__SetRange2.htm).

Description

This method sets the range and increment for
this number box.

Syntax (OLE Automation)

PropertyManagerPageNumberbox.SetRange ( Units, Minimum,
Maximum, Increment )

(Table)=========================================================

| Input: | (long) Units | Number box units as defined in swNumberboxUnitType_e |
| --- | --- | --- |
| Input: | (double) Minimum | Number box minimum value |
| Input: | (double) Maximum | Number box maximum value |
| Input: | (double) Increment | Number box increment |
| Input: | (VARIANT_BOOL) Inclusive | TRUE sets the range as inclusive, FALSE sets it as exclusive |

Syntax (COM)

status = PropertyManagerPageNumberbox->SetRange
( Units, Minimum, Maximum, Increment )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Units | Number box units as defined in swNumberboxUnitType_e |
| --- | --- | --- |
| Input: | (double) Minimum | Number box minimum value |
| Input: | (double) Maximum | Number box maximum value |
| Input: | (double) Increment | Number box increment |
| Input: | (VARIANT_BOOL) Inclusive | TRUE sets the range as inclusive, FALSE sets
it as exclusive |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can only use this method
to set properties on the PropertyManager page before it is displayed or
while it is closed. See PropertyManagerPage2::Show2 and ProperytManagerPage2::Close.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPageNumberbox\PROPERTYMANAGERPAGENUMBERBOX__SETRANGE.HTM" >
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
<param name="Items" value="PropertyManagerPageNumberbox_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPageNumberbox\PROPERTYMANAGERPAGENUMBERBOX__SETRANGE.HTM" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXCutBodyInHalfUsingMacroFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPageNumberbox\PROPERTYMANAGERPAGENUMBERBOX__SETRANGE.HTM" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
