---
title: "DisplayDimension::GetArrowHeadStyle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetArrowHeadStyle.htm"
---

# DisplayDimension::GetArrowHeadStyle

This method is obsolete and has been superseded
by[DisplayDimension::GetArrowHeadStyle2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetArrowHeadStyle2.htm).

Description

This method gets the arrow head style used
by this display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetArrowHeadStyle ( )

(Table)=========================================================

| Return: | (long) retval | Arrow head style as defined in swArrowStyle_e |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetArrowHeadStyle (
&retval )

(Table)=========================================================

| Output: | (long) retval | Arrow head style as defined in swArrowStyle_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can control the arrow head style for a display
dimension with a value that SolidWorks stores in one of two places: on
the owning document or on the individual display dimension. Use DisplayDimension::GetUseDocArrowHeadStyle
to determine whether the document or the individual display dimension
is controlling the arrow head style.

This method returns the arrow head style for this
display dimension. If this display dimension is set to use the document
settings for arrow head style, then this method might return a value that
different than what is displayed.

Use DisplayDimension::SetArrowHeadStyle to set
the arrow head style.

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
<param name="Items" value="DisplayDimension_Object$$**$$ZGetInfoDisplayDimension$$**$$ZGetInfoDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DisplayDimension\DisplayDimension__GetArrowHeadStyle.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
