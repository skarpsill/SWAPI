---
title: "ModelDoc::Save2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Save2.htm"
---

# ModelDoc::Save2

This
method is obsolete and has been superseded by[ModelDoc2::Save2](../ModelDoc2/ModelDoc2__Save2.htm).

Description

This method saves the document using its current
name.

Syntax (OLE Automation)

retval = ModelDoc.Save2 (silent)

(Table)=========================================================

| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs,
FALSE if you want the dialogs displayed |
| --- | --- | --- |
| Return: | (long) retval | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e
for a list of possible errors and warnings |

Syntax (COM)

status = ModelDoc->Save2 ( silent, &retval
)

(Table)=========================================================

| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs,
FALSE if you want the dialogs displayed |
| --- | --- | --- |
| Output: | (long) retval | 0 for no error or a bitwise OR of the errors encountered; see to swFileSaveError_e
for a list of possible errors and warnings |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method results in FileSaveNotify being sent
to any application listening.

If this is an unsaved document or to save a
file with a new name. See ModelDoc::SaveAs2.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__Save2.htm" >
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
<param name="Items" value="AssemblyDoc::Notifications$$**$$DrawingDoc::Notifications$$**$$PartDoc::Notifications$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__Save2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
