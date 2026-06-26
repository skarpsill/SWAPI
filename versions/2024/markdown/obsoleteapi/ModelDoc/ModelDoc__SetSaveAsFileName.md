---
title: "ModelDoc::SetSaveAsFileName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetSaveAsFileName.htm"
---

# ModelDoc::SetSaveAsFileName

This method is obsolete
and has been superseded by[ModelDoc2::SetSaveAsFileName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetSaveAsFileName.htm).

Description

This method sets theSave
Asfile name from within the FileSaveAsNotify2 event handlers,
allowing the Solidworks fileSavedialog to be bypassed.

Syntax (OLE Automation)

void ModelDoc.SetSaveAsFileName (fileName)

(Table)=========================================================

| Input: | ( BSTR ) fileName | Filename to use |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetSaveAsFileName ( fileName
)

(Table)=========================================================

| Input: | ( BSTR ) fileName | Fielname to use |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use this method should from within the FileSaveAsNotify2
event handler. When setting the filename using this method, S_FALSE should
be returned from the FileSaveAsNotify2 event handler. See AssemblyDoc::FileSaveAsNotify2,
DrawingDoc::FileSaveAsNotify2, and PartDoc::FileSaveAsNotify2 notifications.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SetSaveAsFileName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
