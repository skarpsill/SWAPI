---
title: "SldWorks::NewPart"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__NewPart.htm"
---

# SldWorks::NewPart

This
method is obsolete and has been superseded by[SldWorks::NewDocument](sldworksAPI.chm::/SldWorks/SldWorks__NewDocument.htm)or SldWorks::INewDocument2.

Description

This method opens a new part and names it automatically.

Syntax (OLE Automation)

retval = SldWorks.NewPart ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created part or NULL if the
operation fails |
| --- | --- | --- |

Syntax (COM)

status = SldWorks->INewPart ( &retval
)

(Table)=========================================================

| Output: | (LPPARTDOC) retval | Pointer to the newly created part or NULL if the operation fails. |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If you want to set the document title without saving
the file, use ModelDoc2::SetTitle2.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__NewPart.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SolidWorks_Visible_or_BackGround_Example$$**$$Close_Document_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__NewPart.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
