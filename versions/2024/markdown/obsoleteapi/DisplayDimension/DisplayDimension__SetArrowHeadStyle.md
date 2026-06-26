---
title: "DisplayDimension::SetArrowHeadStyle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__SetArrowHeadStyle.htm"
---

# DisplayDimension::SetArrowHeadStyle

This method is obsolete and has been superseded
by[DisplayDimension::SetArrowHeadStyle2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__SetArrowHeadStyle2.htm).

Description

This method sets the arrow head style of this
display dimension.

Syntax (OLE Automation)

void DisplayDimension.SetArrowHeadStyle ( useDoc,
arrowHeadStyle)

(Table)=========================================================

| Input: | (BOOL) useDoc | TRUE uses the document setting for arrow head
style, FALSE uses the setting on this display dimension |
| --- | --- | --- |
| Input: | (BOOL) arrowHeadStyle | Arrow head style as defined in swArrowStyle_e
if useDoc is FALSE |

Syntax (COM)

status = DisplayDimension->SetArrowHeadStyle (
useDoc, arrowHeadStyle )

(Table)=========================================================

| Input: | (VARIANT_BOOL) useDoc | TRUE uses the document setting for arrow head
style, FALSE uses the setting on this display dimension |
| --- | --- | --- |
| Input: | (VARIANT_BOOL)
arrowHeadStyle | Arrow head style as defined in swArrowStyle_e
if useDoc is FALSE |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The arrow head style for a display dimension is
controlled by a value stored in one of two places: on the owning document
or on the individual display dimension. Use DisplayDimension::GetUseDocArrowHeadStyle
and DisplayDimension::GetArrowHeadStyle to get the current values for
these settings.

TheuseDocargument indicates if the document default setting for arrow head style
should be used. If you set useDoc to FALSE, thearrowHeadStyleargument indicates the arrow head style used for this display dimension.

When you change the arrow head style, use ModelDoc2::GraphicsRedraw2
to redraw the graphics window and see your changes .

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
<param name="Items" value="DisplayDimension_Object$$**$$ZModifyDisplayDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DisplayDimension\DisplayDimension__SetArrowHeadStyle.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
