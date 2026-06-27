---
title: "ModelDoc::FontFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FontFace.htm"
---

# ModelDoc::FontFace

This
method is obsolete and has been superseded by[ModelDoc2::FontFace](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FontFace.htm).

Description

This method changes font face in the selected notes,
dimensions, and Gtols.

Syntax (OLE Automation)

(void) ModelDoc.FontFace
( face )

(Table)=========================================================

| Input: | (BSTR) face | Points to a null-terminated string that specifies
the font face name (for example, Times New Roman) |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->FontFace
( face )

(Table)=========================================================

| Input: | (BSTR) face | Points to a null-terminated string that specifies
the font face name (for example, Times New Roman) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

You can also refer to the TextFormat object for
full control of text formatting. You obtain this object bykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}using
the GetTextFormat interfaces.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__FontFace.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
