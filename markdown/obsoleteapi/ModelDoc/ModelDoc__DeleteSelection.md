---
title: "ModelDoc::DeleteSelection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteSelection.htm"
---

# ModelDoc::DeleteSelection

This
method is obsolete and has been superseded by[ModelDoc2::DeleteSelection](../ModelDoc2/ModelDoc2__DeleteSelection.htm).

Description

This method deletes the selected items without prompting for user confirmation.

Syntax (OLE Automation)

retval = ModelDoc.DeleteSelection (
confirmFlag)

(Table)=========================================================

| Input: | (BOOL) confirmFlag | TRUE if you want a confirmation dialog to appear, FALSE if not |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the item was deleted successfully, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteSelection
( confirmFlag, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) confirmFlag | TRUE if you want a confirmation dialog to appear, FALSE if not |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the item was deleted successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZDeleting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\ModelDoc\ModelDoc__DeleteSelection.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
