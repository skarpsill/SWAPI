---
title: "ModelDoc::SaveBMP"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveBMP.htm"
---

# ModelDoc::SaveBMP

This
method is obsolete and has been superseded by[ModelDoc2::SaveBMP](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SaveBMP.htm).

Description

This method saves the current view as bitmap
file.

Syntax (OLE Automation)

retval = ModelDoc.SaveBMP (filenameIn,
widthIn, heightIn)

(Table)=========================================================

| Input: | ( BSTR) filenameIn | Complete filename and path of the new bitmap
file |
| --- | --- | --- |
| Input: | ( long) widthIn | Width of the bitmap |
| Input: | ( long) heightIn | Height of the bitmap |
| Return: | ( BOOL) retval | TRUE if file was created successfully |

Syntax (COM)

status = ModelDoc->SaveBMP (filenameIn, widthIn,
heightIn, &retval )

(Table)=========================================================

| Input: | ( BSTR) filenameIn | Complete filename and Path of the new bitmap
file |
| --- | --- | --- |
| Input: | ( long) widthIn | Width of the bitmap |
| Input: | ( long) heightIn | Height of the bitmap |
| Output: | (VARIANT_ BOOL) retval | TRUE if file was created successfully |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The filenameIn argument should include the full
path to the file to be created. The extension should be.bmp.

If the widthIn or the heightIn argument is less
than or equal to 0, the view size is based on the current window size.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SaveBMP.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SaveBMP.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
