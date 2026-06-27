---
title: "ModelDoc::SetReadOnlyState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetReadOnlyState.htm"
---

# ModelDoc::SetReadOnlyState

This method is obsolete
and has been superseded by[ModelDoc2::SetReadOnlyState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetReadOnlyState.htm).

Description

This method sets the read-only mode for a document.

Syntax (OLE Automation)

Success = ModelDoc.SetReadOnlyState
( ReadOnly )

(Table)=========================================================

| Input: | (BOOL) ReadOnly | TRUE to set this document to be read-only, FALSE otherwise |
| --- | --- | --- |
| Return: | (BOOL) Success | TRUE if the document was set to the desired state, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetReadOnlyState
( ReadOnly, &Success )

(Table)=========================================================

| Input: | (VARIANT_BOOL) ReadOnly | TRUE to set this document to be read-only, FALSE otherwise |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) Success | TRUE if the document was set to the desired state, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If the file is opened as read-write in SolidWorks,
specifying read-only will always work, unless it is a new file in which
case it has not been saved yet)

If the file is opened as read-only in SolidWorks,
then specifying for read-write will only change the internal SolidWorks
state, not the access rights on disk, and will only succeed if it would
be possible to open this file with write access. For example, if the file
is read-only on disk or if another user has it open with write access,
then this method will not change the internal state to writeable; instead,
it will remain read-only and FALSE will be returned to indicate failure.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoModelDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetReadOnlyState.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
