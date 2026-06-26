---
title: "ModelDoc::FontUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FontUnits.htm"
---

# ModelDoc::FontUnits

This
method is obsolete and has been superseded by[ModelDoc2::FontUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FontUnits.htm).

Description

This method changes the height, specified in current
system units, of the font in the selected notes, dimensions, and Gtols.

Syntax (OLE Automation)

(void) ModelDoc.FontUnits
( units )

(Table)=========================================================

| Input: | (double) units | Specifies the height, in current system units (for
example, inches, millimeters, and so on) of the font |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->FontUnits
( units )

(Table)=========================================================

| Input: | (double) units | Specifies the height, in current system units (for
example, inches, millimeters, and so on) of the font |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also use the TextFormat object for full
control of text formatting. You can obtain this object by using the GetTextFormat
interfaces.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZModifyNote$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__FontUnits.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
