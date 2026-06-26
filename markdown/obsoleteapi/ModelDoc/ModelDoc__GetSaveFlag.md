---
title: "ModelDoc::GetSaveFlag"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetSaveFlag.htm"
---

# ModelDoc::GetSaveFlag

This
method is obsolete and has been superseded by[ModelDoc2::GetSaveFlag](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetSaveFlag.htm).

Description

This method determines whether the document is currently
dirty and needs to be saved.

Syntax (OLE Automation)

retval = ModelDoc.GetSaveFlag
( )

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if this document needs to be saved, FALSE if
not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetSaveFlag
( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if this document needs to be saved, FALSE if
not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This flag is used by SolidWorks to determine if
theDo you wish to save changesdialog should be displayed when the user tries to close the document.
Many operations in SolidWorks cause this flag to be set, and ModelDoc::SetSaveFlag
can also be used to set this flag.

If you use this method to check the state of an
assembly, SolidWorks sets this flag to TRUE for assemblies only when a
sub-assembly has been saved. Even if this flag is set to TRUE for a subassembly,
SolidWorks does not mark the assembly as dirty until the subassembly is
saved.

After the user has saved the file, this flag is
reset to FALSE.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetSaveFlag.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
