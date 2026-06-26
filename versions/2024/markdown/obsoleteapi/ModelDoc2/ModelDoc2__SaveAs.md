---
title: "ModelDoc2::SaveAs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SaveAs.htm"
---

# ModelDoc2::SaveAs

This method is obsolete and has been superseded
by[ModelDoc2::SaveAs2](ModelDoc2__SaveAs2.htm).

Description

This method saves the document with a new name.

Syntax (OLE Automation)

retval = ModelDoc2.SaveAs ( newName)

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion
that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE for success, FALSE for failure |

Syntax (COM)

status = ModelDoc2->SaveAs ( newName,
&retval )

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion
that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE for success, FALSE for failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method overwrites existing files on disk unless
they are read-only.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__SaveAs.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__SaveAs.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
