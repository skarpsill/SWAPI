---
title: "ModelDoc2::SaveAs3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SaveAs3.htm"
---

# ModelDoc2::SaveAs3

This method is obsolete and has been superseded
by[ModelDoc2::SaveAs4](ModelDoc2__SaveAs4.htm).

Description

This method saves the document under a different
name.

Syntax (OLE Automation)

retval = ModelDoc2.SaveAs3 ( newName, saveAsVersion,
options )

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion
that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Input: | (long) saveAsVersion | Version as defined in swSaveAsVersion_e |
| Input: | (long) options | Option as defined in swSaveAsOptions_e |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |

Syntax (COM)

status = ModelDoc2->SaveAs3 ( newName, saveAsVersion,
options, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion
that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Input: | (long) saveAsVersion | Version as defined in swSaveAsVersion_e |
| Input: | (long) options | Option as defined in swSaveAsOptions_e |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The options argument is a bitmask containing various
BOOLEANS that affect the outcome of saving the document.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

If the file was saved without errors, retvalhas a value of 0. Otherwise, it contains
a bitwise OR of the error codes that were generated when saving the document.
However, not all of the File,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Save
return codes are fatal errors. It is a bitmask of different conditions
that can occur during the operation; some of which are fatal, some are
informational or warnings. Check the masks in swFileSaveError_e.

This method:

- Overwrites
  existing files on disk unless they are read-only.
- Results in
  FileSaveAsNotify being sent to any application listening.

To save the referenced part files when using this
method on an assembly document, you must specify these enumerators for
the Options argument:

- swSaveAsOptions_Silent
- swSaveAsOptions_Copy
- swSaveAsOptions_SaveReferenced

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__SaveAs3.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__SaveAs3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
