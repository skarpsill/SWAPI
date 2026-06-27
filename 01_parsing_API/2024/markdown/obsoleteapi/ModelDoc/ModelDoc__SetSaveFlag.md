---
title: "ModelDoc::SetSaveFlag"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetSaveFlag.htm"
---

# ModelDoc::SetSaveFlag

This method is obsolete
and has been superseded by[ModelDoc2::SetSaveFlag](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetSaveFlag.htm).

Description

This method flags the document as dirty. If the user tries to close
the part, SolidWorks pops up theDo you
wish to save changesdialog.

Syntax (OLE Automation)

void ModelDoc.SetSaveFlag ()

Syntax (COM)

status = ModelDoc->SetSaveFlag (
)

(Table)=========================================================

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

If your application data has changed, this method allows you to mark
the SolidWorks document as dirty so that the user is prompted if he or
she tries to close it. This could be used, for example, with applications
that use the IGet3rdPartyStorage mechanism to save stream data in SolidWorks
files.

This method is not needed when you have programmatically changed the
SolidWorks model because doing so automatically flags the document as
dirty.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SetSaveFlag.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
