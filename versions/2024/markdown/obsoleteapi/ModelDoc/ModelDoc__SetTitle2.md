---
title: "ModelDoc::SetTitle2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetTitle2.htm"
---

# ModelDoc::SetTitle2

This
method is obsolete and has been superseded by[ModelDoc2::SetTitle2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetTitle2.htm).

Description

This method sets the title of a new document.
This title appears in the active window title bar.

Syntax (OLE Automation)

retval = ModelDoc.SetTitle2 ( newTitle )

(Table)=========================================================

| Input: | Input: (BSTR) | New title to give to the document window |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successfully renamed, FALSE otherwise |

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Syntax (COM)

status = ModelDoc->SetTitle2 ( newTitle, &retval
)

(Table)=========================================================

| Input: | Input: (BSTR) | New title to give to the document window |
| --- | --- | --- |
| OUTPUT | (VARIANT_BOOL) retval | TRUE if successfully renamed, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method does not save this ModelDoc object
to disk; it only renames the document window.

This method is only valid when called on a new
document that has not yet been saved. It will not change the title of
a document that has been saved and already exists on disk. If you want
to rename an existing document, use ModelDoc::SaveAs2.

To retrieve the title of a document, use ModelDoc::GetTitle.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetTitle2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
