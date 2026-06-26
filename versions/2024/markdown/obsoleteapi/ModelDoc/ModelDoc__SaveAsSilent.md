---
title: "ModelDoc::SaveAsSilent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveAsSilent.htm"
---

# ModelDoc::SaveAsSilent

This method is obsolete
and has been superseded by[ModelDoc::SaveAs2](ModelDoc__SaveAs2.htm).

Description

This method saves the current document with a new name. Dialog boxes
are suppressed.

Syntax (OLE Automation)

Errors=
ModelDoc.SaveAsSilent ( newName, saveAsCopy)

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document, which can be a name with suffix or a full
path |
| --- | --- | --- |
| Input: | (BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name
in the active session; documents that reference the document will continue
to reference the original file |
| Return: | (long) Errors | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e |

Syntax (COM)

status = ModelDoc->SaveAsSilent
( newName, saveAsCopy, &Errors)

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document, which can be a name with suffix or a full
path |
| --- | --- | --- |
| Input: | (BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name
in the active session; documents that reference the document will continue
to reference the original file |
| Output: | (long) Errors | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to ModelDoc::SaveAs except
that dialog boxes are suppressed.

If the file was saved successfully then Errors
will have the value 0;otherwise it will contain a bitwise OR of the error
codes that were generated in saving the document. The masks to check against
are the values of the enumerator swFileSaveError_e.

This method overwrites existing files on disk unless
they are read-only.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SaveAsSilent.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
