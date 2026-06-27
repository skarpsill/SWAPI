---
title: "ModelDoc::SaveAs2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveAs2.htm"
---

# ModelDoc::SaveAs2

This method is now obsolete and has been
superseded by[ModelDoc::SaveAs3](ModelDoc__SaveAs3.htm)

Description

This method saves the document with a new name.

Syntax (OLE Automation)

retval = ModelDoc.SaveAs2 (newName,
unused, saveAsCopy, silent)

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document; the file extension
will indicate any conversion that should be performed for example, Part1.igs
to save to IGES) |
| --- | --- | --- |
| Input: | (long) unused | Not used, pass 0 for this argument |
| Input: | (BOOL) saveAsCopy | TRUE to save the document to a new filename without
replacing the name in the active session; documents that reference the
document will continue to reference the original file |
| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs,
FALSE if you want the dialogs displayed |
| Return: | (long) retval | 0 if no errors during save; otherwise, errors
occurred |

Syntax (COM)

status = ModelDoc->SaveAs2 (newName,
unused, saveAsCopy, silent, &retval )

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document; the file extension
will indicate any conversion that should be performed (for example, Part1.igs
to save to IGES) |
| --- | --- | --- |
| Input: | (long) unused | Not used; pass 0 for this argument |
| Input: | (VARIANT_BOOL) saveAsCopy | TRUE to save the document to a new filename without
replacing the name in the active session; documents that reference the
document will continue to reference the original file |
| Input: | (VARIANT_BOOL) silent | TRUE if you want to avoid error and warning dialogs,
FALSE if you want the dialogs displayed |
| Output: | (long) retval | 0 if no errors during s; otherwise, errors occurred |
| Return: | (HRESULT)status | S_OK if successful; S_FALSE otherwise |

Remarks

The name of the document must be the filename and
the file extension. The file path is optional. If the path is not specified,
then the file ise saved in the current working directory.

If the file was saved successfully, then retvalwill have the value 0;otherwise it
will contain a bitwise OR of the error codes that were generated in saving
the document. The masks to check against can be found in the swFileSaveError_e
enumeration.

This method overwrites existing files on disk unless
they are read-only.

This method results in FileSaveAsNotify being sent
to any application listening.

To save a file using its current name, see ModelDoc::Save2.

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
<param name="Items" value="ModelDoc_Object$$**$$SldWorks::GetCurrentWorkingDirectory$$**$$SldWorks::SetCurrentWorkingDirectory$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SaveAs2.htm" >
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
<param name="Items" value="Save_As_Tiff Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SaveAs2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="Items" value="AssemblyDoc::Notifications$$**$$DrawingDoc::Notifications$$**$$PartDoc::Notifications$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SaveAs2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
